#!/usr/bin/env python3
"""
Extract flashcards from an Anki .apkg file into organized Markdown files.

Usage:
    python3 extract-cards.py path/to/your-deck.apkg

Supports any Anki deck — KMK, OptoPrep, class notes, or your own.
Cards are written to the cards/ directory, organized by deck/subject.
"""

import sqlite3
import json
import re
import os
import sys
import html
import shutil
import tempfile
import zipfile


def clean_html(text):
    text = re.sub(r'<img[^>]*src="([^"]*)"[^>]*>', r'[IMAGE: \1]', text)
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<div[^>]*>', '\n', text)
    text = re.sub(r'</div>', '', text)
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract(apkg_path):
    if not os.path.exists(apkg_path):
        print(f"Error: File not found: {apkg_path}")
        sys.exit(1)

    cards_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cards')
    os.makedirs(cards_dir, exist_ok=True)

    tmp_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(apkg_path, 'r') as z:
            z.extractall(tmp_dir)

        db_path = os.path.join(tmp_dir, 'collection.anki21')
        if not os.path.exists(db_path):
            db_path = os.path.join(tmp_dir, 'collection.anki2')
        if not os.path.exists(db_path):
            print("Error: No Anki database found in the .apkg file.")
            sys.exit(1)

        conn = sqlite3.connect(db_path)

        col = conn.execute("SELECT decks FROM col").fetchone()[0]
        decks = json.loads(col)
        deck_map = {int(k): v['name'] for k, v in decks.items()}

        col_models = conn.execute("SELECT models FROM col").fetchone()[0]
        models = json.loads(col_models)
        model_fields = {}
        for k, v in models.items():
            model_fields[int(k)] = {
                'name': v['name'],
                'fields': [f['name'] for f in v['flds']]
            }

        cards = conn.execute("""
            SELECT n.id, n.mid, n.flds, n.tags, c.did
            FROM notes n
            JOIN cards c ON c.nid = n.id
        """).fetchall()

        seen_notes = set()
        unique_cards = []
        for card in cards:
            if card[0] not in seen_notes:
                seen_notes.add(card[0])
                unique_cards.append(card)

        subjects = {}
        for note_id, mid, flds, tags, did in unique_cards:
            deck_name = deck_map.get(did, 'Unknown')

            parts = deck_name.split('::')
            # Use the deepest meaningful deck levels as subject and unit
            meaningful = [p.strip() for p in parts if p.strip() and p.strip() != 'Default']

            if len(meaningful) >= 2:
                subject = meaningful[-2] if len(meaningful) >= 2 else meaningful[-1]
                unit = meaningful[-1]
            elif len(meaningful) == 1:
                subject = meaningful[0]
                unit = 'General'
            else:
                subject = 'General'
                unit = 'General'

            model_info = model_fields.get(mid, {'name': 'Unknown', 'fields': []})
            fields = flds.split('\x1f')
            model_name = model_info['name']

            if 'Cloze' in model_name:
                raw_text = clean_html(fields[0]) if fields else ''
                extra = clean_html(fields[1]) if len(fields) > 1 else ''
                answers = re.findall(r'\{\{c\d+::([^}|]+)(?:\|[^}]*)?\}\}', raw_text)
                question_text = re.sub(r'\{\{c\d+::([^}|]+)(?:\|[^}]*)?\}\}', '________', raw_text)
                card_data = {
                    'type': 'cloze',
                    'question': question_text,
                    'answer': '; '.join(answers),
                    'extra': extra
                }
            elif 'Image Occlusion' in model_name:
                card_data = {
                    'type': 'image_occlusion',
                    'header': clean_html(fields[1]) if len(fields) > 1 else '',
                    'image': fields[2] if len(fields) > 2 else '',
                    'note': 'Image-based card — refer to original Anki deck'
                }
            else:
                q = clean_html(fields[0]) if fields else ''
                a = clean_html(fields[1]) if len(fields) > 1 else ''
                if 'Quizlet' in model_name and len(fields) > 2 and fields[2].strip():
                    a = clean_html(fields[2])
                card_data = {
                    'type': 'basic',
                    'question': q,
                    'answer': a
                }

            if subject not in subjects:
                subjects[subject] = {}
            if unit not in subjects[subject]:
                subjects[subject][unit] = []
            subjects[subject][unit].append(card_data)

        conn.close()

        total = 0
        for subject, units in sorted(subjects.items()):
            safe_name = re.sub(r'[^\w\s-]', '', subject).strip().replace(' ', '_')
            safe_name = re.sub(r'_+', '_', safe_name)
            filepath = os.path.join(cards_dir, f"{safe_name}.md")

            card_count = sum(len(c) for c in units.values())
            total += card_count

            with open(filepath, 'w') as f:
                f.write(f"# {subject}\n\n")
                f.write(f"**Total cards: {card_count}**\n\n")

                for unit_name, cards_list in sorted(units.items()):
                    f.write(f"## {unit_name}\n\n")
                    f.write(f"*{len(cards_list)} cards*\n\n")

                    for i, card in enumerate(cards_list, 1):
                        if card['type'] == 'image_occlusion':
                            f.write(f"### Card {i} (Image)\n")
                            f.write(f"**Topic:** {card['header']}\n\n")
                            f.write(f"*{card['note']}*\n\n")
                        else:
                            f.write(f"### Card {i}\n")
                            f.write(f"**Q:** {card['question']}\n\n")
                            f.write(f"**A:** {card['answer']}\n\n")
                            if card.get('extra'):
                                f.write(f"*Note: {card['extra']}*\n\n")

                    f.write("---\n\n")

            print(f"  {subject}: {card_count} cards -> {os.path.basename(filepath)}")

        print(f"\nDone. Extracted {total} cards into {len(subjects)} files in cards/")

    finally:
        shutil.rmtree(tmp_dir)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 extract-cards.py path/to/your-deck.apkg")
        print("\nSupports any Anki .apkg export file.")
        sys.exit(1)
    extract(sys.argv[1])
