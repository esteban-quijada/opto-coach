# Opto-Coach

An AI-powered study coach for the NBEO Part I (ABS) exam, built on evidence-based learning science. You supply your own study content — from your optometry textbooks, class notes, board review courses, or Anki decks — and the system applies a structured methodology grounded in cognitive science research to help you actually retain it.

This is not a flashcard app. It's a study system that forces active retrieval, builds conceptual frameworks before drilling details, and interleaves subjects to mirror how boards actually test you.

## How It Works

The study methodology is built on decades of cognitive science research and applies these principles:

- **Conceptual Frameworking** — extracting the organizational skeleton of a topic before touching any details (Gernsbacher, 1997)
- **Retrieval Practice** — forcing yourself to produce answers from memory rather than passively reviewing, repeated 4x in 48 hours (Roediger & Karpicke, 2006)
- **Spaced & Interleaved Practice** — short sessions across multiple subjects, not marathon single-topic grinds (Cepeda et al., 2006; Rohrer & Taylor, 2007)
- **Memory Palaces** — spatial mnemonics for high-density fact clusters (method of loci)
- **Metacognitive Monitoring** — recognizing the difference between "I've seen this" and "I can produce this cold" (Bjork & Bjork, 2011)

The full methodology reference with citations is in `method/study-methodology.md`.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated
- A terminal (macOS, Linux, or WSL on Windows)
- Your own study content (see [Loading Your Cards](#loading-your-cards) below)

## Quick Start

```bash
git clone <repo-url>
cd opto-coach

# Load your study content (from an Anki deck)
python3 extract-cards.py path/to/your-deck.apkg

# Start studying
claude
```

Claude reads the `CLAUDE.md` prompt automatically and becomes your study coach.

## Loading Your Cards

The `cards/` directory starts empty. You supply the content from your own sources.

### From an Anki Deck (.apkg)

The included script extracts any Anki deck into the format the coach expects:

```bash
python3 extract-cards.py path/to/your-deck.apkg
```

This works with decks from any source — board review courses, class exports, community decks, or your own.

### Manually

Add cards to any Markdown file in `cards/` using this format:

```markdown
# Subject Name

## Unit or Topic

### Card 1
**Q:** Your question here

**A:** Your answer here

### Card 2
**Q:** Next question

**A:** Next answer
```

### Supported Sources

The system works with content from any optometry study source:
- Board review course notes
- Optometry textbook summaries
- Class lecture notes
- Community Anki decks
- Your own question banks

## How to Use

Once inside the Claude session, you can interact naturally or use these commands:

| Command | What It Does |
|---|---|
| `quiz me on [topic]` | Starts a retrieval practice round on a subject or unit |
| `framework [topic]` | Builds the organizational skeleton before drilling |
| `interleave [topic A] and [topic B]` | Mixed drilling across two subjects |
| `boards question` | Generates a boards-style clinical vignette from card content |
| `palace [topic]` | Builds a memory palace for a difficult fact cluster |
| `connect [A] to [B]` | Explores cross-subject connections |
| `weak spots` | Reviews concepts you've missed during the session |
| `session plan` | Gets a recommended study plan based on subject priority |
| `status` | Shows what's been covered and what needs work |

### Example Session

```
You: quiz me on ocular pharmacology unit 1

Coach: Before we drill autonomic drugs, let's framework this.
       The autonomic nervous system splits into sympathetic and
       parasympathetic. Cholinergic agonists act on which branch?
       And what are the two receptor subtypes?

You: parasympathetic... muscarinic and nicotinic

Coach: Correct. Now — direct vs. indirect cholinergic agonists.
       Name one of each and their mechanism.

You: pilocarpine is direct... it binds muscarinic receptors directly.
     indirect... I don't remember

Coach: Indirect cholinergic agonists inhibit acetylcholinesterase,
       preventing ACh breakdown. Echothiophate (Phospholine Iodide)
       is the classic one — irreversible AChE inhibitor used for
       accommodative esotropia. Restate that back to me.
```

Notice the pattern: framework first, then retrieval (you have to produce the answer), then correction with explanation, then restatement to encode it.

## NBEO Part I Subject Areas

### Big 8 (Highest Exam Weight)

| Subject | Approx. Exam Weight |
|---|---|
| Ocular Disease | ~18-22% |
| Ocular Anatomy | ~12-15% |
| Ocular Physiology | ~10-12% |
| Systemic Disease | ~8-10% |
| Ocular Pharmacology | ~8-10% |
| Systemic Pharmacology | ~8-10% |
| Physiological Optics | ~8-10% |

### Non-Big 8

Visual Perception, Geometric Optics, General Physiology, Biochemistry, Human Development, Neuroscience, Histology, Immunology, Ocular Embryology, Microbiology

## Repo Structure

```
opto-coach/
├── CLAUDE.md                        # Study coach prompt (read automatically by Claude)
├── README.md                        # You are here
├── extract-cards.py                 # Script to extract Anki decks into cards/
├── method/
│   └── study-methodology.md         # Full methodology reference with research citations
├── reference/
│   └── nbeo-part1-blueprint.md      # NBEO exam blueprint, subject weights, cross-subject connections
└── cards/                           # Your study content goes here (gitignored)
```

## Study Strategy Recommendations

### If You Have 8+ Weeks

1. **Week 1-2:** Framework all Big 8 subjects. No drilling yet — just build the skeletons.
2. **Week 3-6:** Retrieval practice rounds, 2-3 subjects per session, interleaved. Hit Tier 1 subjects (Ocular Disease, Anatomy, Pharmacology) most frequently.
3. **Week 7-8:** Boards-style vignettes, cross-subject connections, targeted review of weak spots.

### If You Have 2-4 Weeks

1. **Days 1-3:** Framework the Big 8 rapidly.
2. **Days 4-21:** Heavy interleaved retrieval. Focus 70% on Tier 1-2 subjects, 30% on Tier 3-4.
3. **Final days:** Boards questions only. No new material.

### Every Session

- Start with framework, not cards
- Retrieve before you review — struggle is the point
- Mix subjects — never grind one topic for a whole session
- End by recalling 3-5 things from the session without looking
- Come back to missed items next session, not immediately

## Customization

### Adjusting the Coach

Edit `CLAUDE.md` to change:
- Session length and round sizes
- Interleaving frequency
- How strict the coach is about retrieval-only
- Which subjects to prioritize
- Whether to include memory palace prompts

### Updating the Methodology

Edit `method/study-methodology.md` to add techniques, adjust protocols, or incorporate methods from courses you've taken.

## Research Foundation

This system is built on established cognitive science, not study tips. Key references:

- Roediger & Karpicke (2006) — retrieval practice produces more learning than restudying
- Bjork & Bjork (2011) — desirable difficulties improve long-term retention
- Cepeda et al. (2006) — distributed practice beats massed practice
- Rohrer & Taylor (2007) — interleaving improves discrimination and transfer
- Brown, Roediger, & McDaniel (2014) — *Make It Stick: The Science of Successful Learning*

## Disclaimer

This tool supplements your board preparation — it does not replace a structured review course, clinical experience, or professional guidance. The study methodology is derived from published cognitive science research. Users are responsible for supplying their own study content in compliance with any applicable terms of use from their content providers. Always verify clinical information against current authoritative sources.

## Acknowledgments

- Learning science research cited above
- The optometry education community
- Built with [Claude Code](https://claude.ai/code)
