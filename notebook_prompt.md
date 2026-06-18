# CS50 Lecture Notes — Authoring Specification

This document defines how the `lecture-N.ipynb` study notebooks are written. It is the
single source of truth for tone, voice, content, structure, and process. Follow it when
creating a new lecture notebook or expanding an existing one with supplementary material.

These notes are **personal study notes** distilled from CS50 lecture transcripts and the
accompanying "shorts" (transcripts + slide PDFs). They are not a transcript, not a
summary for an audience, and not a blog post.

---

## 1 Tone & Voice (most important)

- **Write as if translating the transcript into a reference book**, not as if recounting
  a lecture that happened.
- **Impersonal, third-person, textbook voice.** Use **passive voice where it reads
  naturally** ("A compiler translates one language into another", "The condition is
  checked before each iteration").
- **Present tense** for how things work ("`strlen` returns the length", not "Malan showed
  that `strlen` returned…").
- **Dense and precise.** No filler, no hedging, no conversational throat-clearing.
- It is for personal use — clarity and faithfulness beat polish or persuasion.

> Mental model the user gave: *"Write it as if you're translating the transcription into a
> book. But make it passive sentences, since it's for personal use."* and *"Imagine you're
> in the audience taking the note."*

---

## 2 What to INCLUDE

- **Every concept and technical point** in the source. Comprehensiveness is required — for
  a full lecture transcript, *every line must be accounted for* (see §9).
- **The concrete examples that illustrate each point** — this is non-negotiable. A barebones
  notebook of abstract bullet points is a failure. Keep:
  - real code (reconstructed faithfully from the narration),
  - exact numbers used (e.g., `72`, `73`, `33`; ASCII `65`/`97`; `32764` garbage value),
  - file/program names (`buggy.c`, `scores.c`, `greet.c`, `cowsay`),
  - pseudocode when the lecture gives it.
- **Real-world consequence examples** (e.g., Boeing 787 integer overflow, Pac-Man level 256,
  Y2K, Year 2038).
- **Cautions, gotchas, and common-bug notes** (e.g., `=` vs `==`, integer truncation,
  comparing strings needs `strcmp`, out-of-bounds → segfault).
- **Cross-references** to related sections elsewhere in the notebook.

---

## 3 What to EXCLUDE (the "fluff")

Strip all lecture theater and narration. Specifically remove:

- **Speaker/professor narration** — never write "Prof. Malan opened VS Code", "David showed",
  "Doug Lloyd", "Carter", "my name is…", "I'm Doug Lloyd, this is CS50".
- **The people.** Volunteer names, their dorms/majors, "a round of applause", audience
  banter. Keep the *example*, drop the humans.
  > User: *"I don't fucking care about the people, I just want the example."*
- **Meta / classroom logistics** — "any questions?", Q&A back-and-forth, "pause the video",
  "take a minute", snack/break announcements (Cheez-Its, muffins, "10-minute break"),
  cake at the end, the clock striking 4:15, "see you next time".
- **Verbatim retelling of demonstrations.** Extract the *key points* of each demo, not a
  blow-by-blow transcript of what was typed and clicked.
  > User: *"remove all those stupid demonstrations, just keep the main points, include
  > examples, and instead of taking the demonstration verbatim, take key points from each
  > example."*
- **First-person lecturer voice and filler.**

Course-relative time references **are allowed** ("in Week 0", "revisited in a later week",
"Week 4 reveals what a string really is") — these are useful and should be kept.

---

## 4 How Examples Are Handled

- Present each example as an **illustration of a concept**, not as an event ("Three bytes
  `72, 73, 33` decode as `HI!`" — not "the volunteers spelled out…").
- **Reconstruct code faithfully** from the narration/slides. Show buggy *and* fixed
  versions where the lecture walks through a fix.
- When the lecture leaves something open, **say so** ("left as an exercise") rather than
  inventing an answer.
- Show **output** where it matters (`x is 1, y is 2`; `10 22`; `59.333…`).

---

## 5 Structure & Organization

- **One major topic per markdown cell**, led by a `##` heading. Subsections use `###`,
  sub-subsections `####`.
- **Main-lecture cells follow the transcript chronologically.** Do not reorder topics.
  > User: *"make sure the note follows chronologically as the transcript."*
  - When a topic is previewed early and developed later (e.g., cryptography, debugging),
    mirror that: a short "(Preview)" / "Motivation" cell early, the full treatment where
    the lecture actually develops it — no duplication.
- **Supplementary "shorts"** (Doug Lloyd topic videos, section walkthroughs, their slide
  PDFs) are folded in as **dedicated cells placed at the most logically relevant point**,
  next to the related main-lecture material. They must **deepen, not duplicate**:
  - open with a one-line cross-reference to the existing cell that covers the basics,
  - focus the body on what is genuinely new,
  - explicitly **reconcile differing terminology** when sources disagree (e.g., note that
    "declaration" and "prototype" are the same thing),
  - **flag genuinely new concepts** that the main lecture didn't cover (e.g., `strcmp`,
    pass-by-reference for arrays, `argv` values are strings).
- After any insertion, **verify the final cell order**.

---

## 6 Heading Numbering

Hierarchical section numbers, prefixed by the lecture number `N`:

| Level | Markdown | Number format | Example |
|-------|----------|---------------|---------|
| Title | `#`      | *unnumbered* (it *is* section N) | `# CS50 Lecture 2 Key Notes` |
| Section | `##`   | `N.x`         | `## 2.5 Debugging in Practice` |
| Subsection | `###` | `N.x.y`     | `### 2.5.3 debug50 — Step-Through Debugging` |
| Sub-subsection | `####` | `N.x.y.z` | `#### 2.5.3.4 The Control Icons` |

Rules:
- `###` counters reset within each `##`; `####` counters reset within each `###`.
- **Do not number text inside code fences** (e.g., the Mario `###` grid, `#include`,
  `#define` are not headings).
- Remove any redundant manual numbering in a title once the scheme is applied
  (e.g., "1. Declaration" → "Declaration" so it doesn't read "2.12.4.1 1. Declaration").

---

## 7 Formatting Conventions

- **GitHub-flavored Markdown.**
- **Fenced code blocks with a language tag**: ` ```c `, ` ```cpp `, ` ```python `,
  ` ```sql `, ` ```r `, ` ```bash `, ` ```text `.
- **Tables** for reference data and comparisons: type sizes, truth tables, format
  specifiers, side-by-side analogies, and summary tables.
- **Bold** key terms on first definition.
- **Blockquotes (`>`)** for cautions, key takeaways, and "why" asides.
- **ASCII diagrams** where they aid understanding (black-box function, memory grid,
  efficiency curves, the input → [algorithm] → output model).
- Inline `code` for identifiers, keywords, filenames, and operators.

---

## 8 Special Pattern — Algorithm Examples

When a section teaches algorithms (as in Lecture 0):

- **Define "algorithm" as language-independent logic**, and sharply distinguish it from
  **implementation/optimization**. The recurring learner confusion to pre-empt:
  switching libraries/tools (e.g., `dplyr` → `data.table`, `lapply` → `furrr::future_map`,
  base R → parallel) is an **implementation** change, *not* a new algorithm; changing the
  decision procedure (linear → binary search, kNN → gradient boosting) *is*.
  > Useful test to state: *"if the pseudocode looks different, the algorithm is different."*
- **Use a representative, commonly-used language per example**, drawn from what a CS course
  teaches (C, C++, Java, JavaScript, Python, SQL, R) — keep the manual/conceptual ones in
  plain pseudocode. The *real-world problem* may be advanced; only the *language choice* is
  constrained.
- **Draw on the user's domains** where natural (R data-wrangling, MLB Statcast / xBA).
- **End each algorithm example with a summary table** distinguishing algorithms from
  improvements. For the implementation-heavy example (R), the table's first column is the
  algorithm and subsequent columns are *Improvement #1, #2, …* (rows may have empty cells
  when an algorithm has fewer improvements).

---

## 9 Process & Workflow

1. **Read the entire source first** — the full transcript (use offset/limit for large
   files) and any PDFs — *before* writing anything.
2. **Account for every line.** For a long transcript, partition it into contiguous,
   non-overlapping line ranges and cover each. Subagents may be used for this, each given
   an exact line range and the relevant slice of this spec; assemble their output into
   cells afterward. No gaps.
3. **PDFs:** slide decks usually duplicate the transcript. Extract only what is *new* —
   truth tables, range diagrams, side-by-side tables, and rules stated only on slides
   (e.g., "`else` binds to the nearest `if`", "Scratch `repeat until` is the reverse of C's
   `while`", "`#include` ≈ copy/paste, `#define` ≈ find/replace"). (Reading PDFs requires
   `poppler` / `pdftoppm` installed.)
4. **Faithfulness over invention.** Reconstruct code from narration; never fabricate
   details the source doesn't support; mark open items as exercises.
5. **Verify** cell order and headings after edits.

---

## 10 File Conventions

- Notebook per lecture: `lecture-N.ipynb`, stored in the matching `week-N/` folder.
- Source transcripts: `lectureN-720p-en.txt`; shorts: `<topic>.txt` + `<topic>.pdf`.
- This spec lives at the repo base: `notebook_prompt.md`.

---

## 11 Editing Mechanics (appendix)

- When rewriting cells programmatically, **preserve Unicode** — write JSON with
  `ensure_ascii=False`, read/write UTF-8. Em dashes (`—`, U+2014), arrows (`→`), check
  marks (`✓`), etc. must survive.
- Track ` ``` ` code-fence state so code content is never mistaken for headings or prose to
  transform.
- Prefer `NotebookEdit` for cell-level changes; a Python script over the `.ipynb` JSON is
  acceptable for bulk, consistent transforms (e.g., heading numbering) — verify output
  afterward.
- For large or ambiguous rewrites, it is welcome to **propose the changes first**, then
  apply on confirmation.
