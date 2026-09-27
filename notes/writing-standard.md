# Writing Standard — Plain Language, No AI Accent

Written 2026-09-27. This standard applies to every piece of text in this project: the deck, the notes, the gate packages, subagent output, the Q&A bank, and every message to the team.

## The problem this standard fixes

Readers now recognize a default machine style of writing. It is often called the **"AI accent,"** and the low-quality, repetitive content it produces is called **"AI slop."** The uneasy feeling it gives readers is sometimes called the **linguistic uncanny valley**: the text is grammatical, but it does not sound like a person who knows the subject.

The accent has four common signs:
- adjectives and adverbs that carry no measurable meaning ("robust," "compelling," "significantly");
- a small set of overused verbs and nouns ("leverage," "unlock," "landscape");
- sentence patterns that sound like marketing ("Not just X, but Y");
- framing sentences that talk about the content instead of stating it.

Each of these adds reading effort and removes information. Judges who read many decks notice this style, and it costs trust.

**The goal:** write like a person with technical expertise explaining something to a colleague. Use simple words, few adjectives, and direct statements. Technical terms stay technical and are defined on first use.

## Rules, most important first

1. **State the fact. Do not write a sentence about the fact.**
   - Wrong: "It's worth noting that the payback period is an important consideration."
   - Right: "The investment pays back in [N] years."
2. **Replace descriptive words with the number or the specific thing.**
   - Wrong: "a large, underserved population"
   - Right: "about 150,000 patients, most of them undiagnosed"
   - Keep an adjective only if it changes the fact ("oral," "incremental," "unbranded," "two-variant").
3. **Use verbs, not nouns built from verbs.**
   - Wrong: "The implementation of the new program would enable the achievement of reach."
   - Right: "The program reaches [N] physicians in [M] months."
4. **Keep technical terms, and define each one on first use in plain words.** "NPV (net present value: future cash flows in today's dollars, minus the investment)." Do not replace a precise term with a vague one.
5. **One idea per sentence.** Aim for sentences of about 20 words or fewer. Split any sentence that does more than one job, and do not stack dashes or parenthetical asides.
6. **Say what a numbered item is.** Never refer to "Option 1b," "Gate B," or "slide 7" by label alone. Write "the contracted sales force (Option 1b)."
7. **No idioms or metaphors in place of an explanation.** If the idiom needs explaining, write the explanation instead.
8. **Make every sentence open with a subject and carry a specific active verb.** (This comes from Chris's global rules.)
9. **Rename the thing; never point back at it vaguely.** Write "the contracted-force NPV," not "that number" or "the figures above." (Chris's global rules.)
10. **Every comparison carries its numbers and the rule applied.** Wrong: "the two options are close." Right: "Option X's NPV is $[A]M and Option Y's is $[B]M, a $[A−B]M gap, which is inside the ±$[C]M range the sensitivity analysis produces." (Chris's global rules.)
11. **No counting for effect and no cinematic sequencing.** Never write "One drug, two paths, three decisions." Never write "step by step," "piece by piece," or "here's how it breaks down." (Chris's global rules.)

## Banned words and phrases

Delete the word, or replace it with the plain version. Quoting the case, Vertex, or a source verbatim inside quotation marks is allowed (for example, Vertex's own phrase "transform the disease").

| Category | Banned | Use instead |
|---|---|---|
| Hype adjectives | robust, compelling, powerful, seamless, cutting-edge, innovative, groundbreaking, game-changing, world-class, best-in-class, holistic, comprehensive, dynamic, unparalleled, unique (unless literally one of a kind) | The number, the specific property, or nothing |
| Importance words | critical, crucial, vital, essential, key (as an adjective), pivotal (outside "pivotal trial") | Say *why* it matters: "this sets the launch date" |
| AI-accent verbs | delve, leverage, unlock, harness, empower, foster, navigate, elevate, streamline, spearhead, bolster, underscore, showcase, embark, reimagine, supercharge, optimize (outside math), revolutionize | use, open, build, cut, show, start, raise, lower, plan |
| AI-accent nouns | landscape, ecosystem, tapestry, journey, realm, synergy, paradigm (shift), testament, arsenal, north star, deep dive, game plan, secret sauce, needle-mover, lever (as metaphor), cornerstone | competitors, market, set of tools, detailed review, plan |
| Intensifiers | genuinely, truly, really, actually, incredibly, extremely, highly, deeply, notably, importantly, clearly, simply, just, significantly (unless statistical) | Delete |
| Framing phrases | "it's worth noting," "importantly," "at the end of the day," "in today's fast-paced world," "let's dive in," "here's the thing," "the bottom line is," "moving forward," "at its core," "when it comes to," "in order to" | Delete; state the content |
| Sentence patterns | "Not just X, but Y"; "It's not X, it's Y"; "Not X. Y." fragments; rhetorical questions; colon reveals ("The result: ..."); lists of three adjectives | One plain declarative sentence |

**Allowed as technical terms** (not slop in this context): pivotal trial, key account manager (KAM), key opinion leader (KOL), key performance indicator (KPI), stage gate, statistically significant, optimize (for mathematical optimization), critical path (in a project schedule).

## Calibration rewrites

| AI accent | Plain |
|---|---|
| "Vertex is uniquely positioned to leverage its robust nephrology capabilities to unlock the primary care opportunity." | "Vertex already has nephrology reps. It has no primary care reps." |
| "A compelling, data-driven strategy to transform diagnosis." | "Option X costs $[N]M over three years and adds [M] treated patients by [year]." |
| "This critical insight underscores the importance of genetic testing." | "Genetic testing is the step where the most patients drop out: [N]% of at-risk patients are tested today." |
| "We delved into the competitive landscape." | "We reviewed the [N] companies developing APOL1 drugs." |
| "Not just a sales problem, but a trust problem." | "Patients must agree to a genetic test, so trust limits testing as much as physician awareness does." |
| "Significantly higher ROI" | "ROI of [A]× compared with [B]×" |

The brackets mark where real numbers go. None of these examples favors any option; the model decides the recommendation.

## Slide exemption

Slides are not prose, and consulting read decks use short text. On slides:
- **Titles** are full sentences that state the slide's conclusion, at most two lines.
- **Bullets, chart labels, table cells, and callouts** may be fragments of 12 words or fewer, but each must carry a number or a named thing (for example "Free Labcorp testing: ~2-week turnaround").
- **Bold lead-ins** are allowed on slides.
- The one-idea-per-sentence rule, the subject-and-verb rule, and the check against report formatting apply to titles and to any full sentence on a slide, not to fragments.
- The final-round spoken script may open with one question to engage the judges; the Tepper workshop recommends a hook.
- Words that appear in the case itself ("critical," "unique challenges," "key recommendations") may be used inside quotation marks when quoting the case.

## Self-check before sending any text

1. Can the reader act on each sentence without opening another file or asking what a phrase means?
2. Does each sentence state a fact, or does it talk about a fact?
3. Could any adjective be replaced by a number? If so, replace it.
4. Does any word from the banned table appear outside a direct quote?
5. Is the text formatted as a report when a plain paragraph would do? Headers and bold lead-ins create room for filler; use them only when the reader needs to navigate.

## Enforcement

The agent writes `work\qa\lint_language.py`, a script that scans every `.md` file in `work\` and the text extracted from each `.pptx`. It reports each banned word or pattern with its file and line. It skips text inside quotation marks, the allowed technical terms, and PPTX table cells and chart labels. Every gate package and the final deck must show zero hits, or give a written reason for each hit it keeps.
