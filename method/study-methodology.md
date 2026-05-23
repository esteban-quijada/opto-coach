# Evidence-Based Study Methodology

A study system for medical and optometric board exams, grounded in cognitive science research on how memory works and how to study effectively.

## Foundation: The Learning Circuit

All learning follows three sequential stages:

1. **Encoding** — entering information into memory
2. **Storage** — retention over time (consolidation, reorganization, stabilization)
3. **Retrieval** — accessing material from memory

Most students fail at encoding and retrieval because they rely on passive review (rereading, highlighting, recopying), which creates a **familiarity trap** — recognizing material without being able to produce it.

## Phase 0: Diagnostic Evaluation

Before any studying begins, evaluate the student's **learning process** — not their knowledge. This diagnostic shapes how all subsequent sessions are structured.

### What to Assess

| Area | How to Test |
|---|---|
| **Structure building** | Give 10 conditions, ask them to sort into groups. Do they organize by surface features (anatomy/location) or by mechanism/pathway? |
| **Retrieval vs. recognition** | List 5-6 core concepts. Ask: do you *know* it (produce cold), *recognize* it (get it right if you saw the answer), or *don't know* it? |
| **Encoding ability** | Teach a small framework, test retrieval 10 minutes later. Does the framework stick when provided? |
| **Study habits** | Ask directly: re-reading? Anki grinding? Blocked practice? Passive review? Identify which traps they're currently falling into. |
| **Metacognitive awareness** | Can they accurately distinguish between what they know and what they merely recognize? |

### Why This Matters

Students arrive with different learning profiles. A student who naturally builds structure needs less frameworking scaffolding. A student deep in the familiarity trap needs aggressive retrieval protocols. A student with strong metacognitive awareness can self-monitor; one without it needs external checkpoints. The diagnostic determines where to invest session time.

### Output

The diagnostic produces a **learning profile** (stored in `profile/learning-profile.md`) that persists across sessions and is updated as the student's abilities develop. This profile tracks:
- Structure building ability (weak/moderate/strong)
- Retrieval vs. recognition baseline
- Encoding style (needs skeleton provided vs. self-generates)
- Study habit history and traps to watch for
- Metacognitive awareness level

## Session Types: Separated Learning

Study sessions are divided into two distinct types. Do NOT blend them.

### Type 1: Framework Sessions (No Cards)

Discussion-based sessions focused on building and deepening conceptual frameworks. The coach teaches through elaborative interrogation — asking "why" and "what would happen if" questions — not by presenting facts. Cards are not used.

**Purpose:** Build the organizational skeleton so details have somewhere to attach. Convert recognition into understanding of mechanisms, pathways, and relationships.

**Structure:**
1. Identify the topic and its place in the larger framework
2. Build the skeleton through guided discussion (major categories, mechanisms, relationships)
3. Use elaborative interrogation — the student must predict and reason, not just listen
4. When a gap is found, zoom out to the framework level before filling it in
5. End by having the student reproduce the framework from memory

**When a student misses a concept:** Don't just correct and move on. Zoom out — where does this fact sit in the framework? What category, what mechanism, what's it connected to? Anchor the fact to the skeleton before proceeding.

### Type 2: Card Drilling Sessions

Pure retrieval practice using the cards in `cards/`. The student has already built the framework in a Type 1 session. Now they stress-test whether specific details stuck.

**Purpose:** Convert framework understanding into retrievable factual knowledge. Identify specific gaps.

**Timing:** Do card drilling within 24 hours of the framework session on the same topic to catch the forgetting curve at its steepest.

**Structure:** Follow the retrieval practice protocol below (rounds of 5-8 cards, interleaved, spaced repetition of misses).

## Core Techniques

### 1. Conceptual Frameworking

Before studying any details, extract the **organizational schema** of the material.

**Why it matters:** Many learners cannot encode isolated facts effectively. They need the big picture first. Without a framework, details have nowhere to attach and fall away. This is supported by research on structure building (Gernsbacher, 1997) — high structure builders naturally organize information, while low structure builders need to be taught to do it explicitly. Frameworking also works with working memory constraints — Miller (1956) showed we can hold roughly 7 (plus or minus 2) items in short-term memory. A framework lets you chunk related details under fewer top-level categories, effectively compressing what you need to hold in mind at any one time.

**How to apply:**
- Before touching any cards in a subject/unit, build a structural outline: What are the major categories? How do they relate? What's the hierarchy?
- Think of it as the skeleton that details hang on
- The framework should answer: "If someone asked me what this unit is ABOUT, what would I say in 30 seconds?"
- Revisit and refine the framework as you encounter new details

**For NBEO cards:** Before drilling any unit, generate the framework first. For example, Ocular Anatomy Unit 1 (Eyelids/Lacrimal) — the framework might be: Layers of the lid (skin -> orbicularis -> tarsal plate -> conjunctiva) -> Glands (Meibomian, Zeis, Moll, Wolfring, Krause) -> Lacrimal system (gland -> puncta -> canaliculi -> sac -> nasolacrimal duct).

### 2. Multi-Pass Learning

Do NOT go front-to-back through material once. Instead, make **multiple passes at different depths**:

- **Pass 1 (Skeleton):** Framework only. Major categories, relationships, big-picture organization. No details yet.
- **Pass 2 (Muscle):** Key facts, high-yield associations, the "meat" of each concept.
- **Pass 3 (Deep):** Edge cases, exceptions, fine distinctions, connections across subjects.

This aligns with the levels-of-processing framework (Craik & Lockhart, 1972) — deeper, more elaborative processing produces stronger memory traces.

### 3. Retrieval Practice

The single most evidence-backed study technique. Over 100 years of research on the testing effect.

**Why timing matters — the Forgetting Curve:** Ebbinghaus (1885) demonstrated that memory decays exponentially after initial learning — roughly 70% is lost within 24 hours without intervention. Each successful retrieval attempt resets and flattens the curve, making the memory progressively more durable. This is why the protocol below emphasizes multiple retrievals within the first 48 hours: you're catching the memory before it falls off the cliff and reinforcing it at the steepest point of decay.

**The Protocol:**
1. **Choose material** — start small (one concept cluster, ~5-10 cards). This aligns with working memory limits — Miller (1956) showed short-term memory holds roughly 7 (plus or minus 2) items. Keeping chunks small prevents cognitive overload during initial encoding.
2. **Attempt blind recall** — close everything, write/say what you remember. Allow failure.
3. **Self-check** — compare your recall to the source. Note gaps.
4. **Repeat 4x in 48 hours** — with spacing between attempts. Each retrieval flattens the forgetting curve further.

**Critical rules:**
- Retrieval is not review. Looking at a card and thinking "I know that" is recognition, not retrieval.
- The discomfort of struggling to recall IS the learning. It's supposed to feel hard.
- Start with small chunks. Scale up only after the protocol feels natural.
- Always self-check. Unverified recall can cement errors.

**The circuit:** Attempt -> Fail/Succeed -> Self-check -> Correct -> Space -> Attempt again

### 4. Memory Palaces (Method of Loci)

For high-density factual content that resists narrative organization. This technique dates back to ancient Greek and Roman rhetoric and is supported by modern research (Legge et al., 2012).

**Memory Palace:** A familiar physical space (your house, a route you walk) where you place information at specific locations.

**Linking strategies:** Connect each fact to a location using the simplest association that works:
- **Sound-Based Links:** The word sounds like something visual (e.g., "Moll" -> mall -> picture a shopping mall at location 1)
- **Association-Based Links:** The concept naturally associates with something (e.g., "tears" -> crying person)
- **Prescribed Links:** Arbitrary but vivid visual assigned to a concept

**Rule:** Use the minimum link needed. Don't over-elaborate. Crude, vivid, simple beats elegant and complex.

### 5. Concept Mapping

Mind maps and concept maps for organizing relationships between concepts. Useful for:
- Differential diagnosis trees
- Drug classification hierarchies
- Anatomical relationships
- Physiological pathways

Research supports that generating concept maps produces stronger learning than passively studying pre-made ones (Nesbit & Adesope, 2006).

### 6. Active Reading

Active reading with intentional marking/annotation. Not highlighting everything — marking strategically to identify:
- Framework elements (headers, transitions, organizational cues)
- High-yield facts
- Connections to other topics
- Gaps in understanding

## Scheduling Principles

### Spaced Practice (vs. Massed Practice)
- **DO:** Many short sessions spread over time
- **DON'T:** Marathon sessions cramming one topic

Spacing is one of the most robust findings in learning science. Distributed practice consistently outperforms massed practice across domains (Cepeda et al., 2006).

### Interleaved Practice (vs. Blocked Practice)
- **DO:** Mix subjects within a session (e.g., 15 min Anatomy -> 15 min Pharm -> 15 min Optics)
- **DON'T:** Study one subject exclusively until "done"

Interleaving forces discrimination between concepts and improves transfer (Rohrer & Taylor, 2007).

### Time Management
- Know the master plan, where to start today, when you're done, and when to move on
- Make prioritization, time management, and organization **external and explicit** (written schedules, not mental estimates)
- Be accountable for outcomes, not just hours logged

## Test-Taking Strategy

For boards-style questions (clinical vignettes):
1. Read the question stem systematically — don't skip to the answer choices
2. Identify key clues before looking at options
3. Beware the "narrow to two, pick wrong" trap
4. Use partial knowledge + critical thinking to reason through unfamiliar questions
5. Periodically assess your state during the exam (rushing? anxious? skipping clues?)

## Traps to Avoid

| Trap | What It Looks Like | Why It's Dangerous |
|---|---|---|
| **Familiarity Trap** | "I recognize this, so I know it" | Recognition does not equal retrieval. You'll fail when you need to produce the answer cold. |
| **Illusion of Productivity** | Rewriting notes, making pretty flashcards, rewatching lectures | Feels like work, produces no retrievable knowledge. |
| **Massed Practice** | 6-hour anatomy marathon | Diminishing returns after ~45-60 min on one subject. |
| **Blocked Practice** | "I'll finish all of pharm before touching anything else" | Prevents interleaving, weakens long-term retention. |
| **Passive Review** | Reading cards and flipping to see the answer | Not retrieval. Must attempt recall BEFORE seeing the answer. |

## Research Foundation

- **Testing Effect:** Roediger & Karpicke (2006) — retrieval practice produces more learning than restudying
- **Desirable Difficulties:** Bjork & Bjork (2011) — conditions that make learning harder in the short term (spacing, interleaving, retrieval) improve long-term retention
- **Forgetting Curve:** Ebbinghaus (1885) — memory decays exponentially after learning; ~70% lost within 24 hours without retrieval
- **Working Memory Capacity:** Miller (1956) — short-term memory holds roughly 7 (plus or minus 2) items, necessitating chunking and frameworking
- **Spacing Effect:** Ebbinghaus (1885), Cepeda et al. (2006) — distributed practice beats massed practice
- **Interleaving:** Rohrer & Taylor (2007) — mixing problem types improves discrimination and transfer
- **Structure Building:** Gernsbacher (1997) — individual differences in ability to build coherent mental structures from information
- **Levels of Processing:** Craik & Lockhart (1972) — deeper processing produces stronger memory traces
- **Method of Loci:** Legge et al. (2012) — spatial mnemonics improve recall of ordered information
- **Concept Mapping:** Nesbit & Adesope (2006) — visual organization of knowledge improves learning
- **Elaborative Interrogation:** Asking "why" and "how" during encoding strengthens memory traces
- **Make It Stick:** Brown, Roediger, & McDaniel (2014) — comprehensive synthesis of learning science for practitioners
