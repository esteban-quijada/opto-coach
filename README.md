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

## Getting Started

There are two ways to use Opto-Coach: through **Claude Code** (CLI/desktop) or **claude.ai** (browser). Both use the same methodology and content — pick whichever fits your workflow.

### Option A: Claude Code (CLI)

Best if you already use Claude Code or prefer a terminal-based workflow.

**Prerequisites:** [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed and authenticated, a terminal (macOS, Linux, or WSL on Windows)

```bash
git clone <repo-url>
cd opto-coach

# Load your study content (from an Anki deck)
python3 extract-cards.py path/to/your-deck.apkg

# Start studying
claude
```

Claude reads the `CLAUDE.md` prompt automatically and becomes your study coach.

### Option B: Claude.ai (Browser)

Best if you want to study from any device without installing anything.

1. Go to [claude.ai](https://claude.ai) and open **Projects** (left sidebar)
2. Create a new project (e.g., "NBEO Study Coach")
3. In the project's **Custom Instructions**, paste the contents of `CLAUDE.md` from this repo
4. Under **Project Knowledge**, upload these files:
   - `method/study-methodology.md`
   - `reference/nbeo-part1-blueprint.md`
   - Your card files (see [Loading Your Cards](#loading-your-cards) below) — either upload the `.md` files from `cards/`, or paste/upload your own content directly
5. Start a new conversation inside the project and begin studying

**Note:** If you're using the Anki extraction script, run it locally first (`python3 extract-cards.py path/to/deck.apkg`), then upload the generated `.md` files from `cards/` as project knowledge.

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

### First Time: Setup

When you first start a session, say **`start`**. This triggers the diagnostic evaluation — the coach assesses your learning process (not your knowledge) across five areas: structure building, retrieval vs. recognition, encoding ability, study habits, and metacognitive awareness. Based on the results, it will:

1. Build your **learning profile** (saved to `profile/learning-profile.md`, not tracked by git)
2. Create a **study timeline** based on your exam date and current level
3. Generate your first **session plan** based on subject priority and your profile

This only happens once. After that, your profile persists across sessions and is updated as you progress.

### Returning: Continue

When you come back for a new session, say **`continue`**. The coach reads your learning profile, reviews where you left off (topics covered, weak areas, session history), and picks up accordingly — recommending what to work on next based on your progress and the spacing protocol.

### Commands

Once inside a session, you can interact naturally or use these commands:

| Command | What It Does |
|---|---|
| `start` | First-time setup: diagnostic evaluation, learning profile, study timeline |
| `continue` | Resume studying from where you left off using your profile |
| `quiz me on [topic]` | Starts a retrieval practice round on a subject or unit |
| `framework [topic]` | Builds the organizational skeleton before drilling |
| `interleave [topic A] and [topic B]` | Mixed drilling across two subjects |
| `boards question` | Generates a boards-style clinical vignette from card content |
| `palace [topic]` | Builds a memory palace for a difficult fact cluster |
| `connect [A] to [B]` | Explores cross-subject connections |
| `weak spots` | Reviews concepts you've missed during the session |
| `session plan` | Gets a recommended study plan based on subject priority |
| `status` | Shows what's been covered and what needs work |

### Example First Session

```
You: start

Coach: Before we study anything, I need to evaluate how you learn.
       I'm going to give you 10 conditions — sort them into groups
       however makes sense to you...

[diagnostic evaluation runs, profile is built]

Coach: Here's your learning profile. Your structure building is weak
       but your metacognitive awareness is strong. Here's your
       study timeline and what we should hit first...
```

### Example Returning Session

```
You: continue

Coach: Welcome back. Last session we built the retinal vascular
       disease framework — you got CRAO mechanism down but we
       didn't finish CRVO. Your weak areas are glaucoma
       categorization and pupillary pathways. I recommend we
       finish the retinal vascular framework, then do a card
       drill on what we covered last time. Ready?
```

### Example Study Session

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

Edit `CLAUDE.md` (CLI) or update the project's Custom Instructions (claude.ai) to change:
- Session length and round sizes
- Interleaving frequency
- How strict the coach is about retrieval-only
- Which subjects to prioritize
- Whether to include memory palace prompts

### Updating the Methodology

Edit `method/study-methodology.md` (CLI) or re-upload it to project knowledge (claude.ai) to add techniques, adjust protocols, or incorporate methods from courses you've taken.

## Research Foundation

This system is built on established cognitive science, not study tips. Key references:

- Ebbinghaus (1885) — the forgetting curve; memory decays ~70% within 24 hours without retrieval
- Miller (1956) — working memory holds 7 (±2) items; basis for chunking and round sizing
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
