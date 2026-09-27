# Deck Theme Brief — Tepper × Tepper Healthcare Club × Vertex

Written 2026-09-27. This brief sets the inputs for the team's theme decision. The team picks one direction; the agent then builds the master template (see the theme step in `prompts/agent-prompt-v4.md`).

## Brand inputs

| Brand | Color | Hex | Source / confidence |
|---|---|---|---|
| Vertex | Purple (Pantone 268 C) | `#52247F` | brandcolorcode.com, which cites the Pantone reference. Medium confidence; sample from the logo in the case PDF to confirm. |
| Vertex | Cool Gray 10 C (wordmark) | `#63666A` | Same source. |
| Case document | Heading purple used in the case PDF | *sample from PDF* | The sponsor's own document styling. The agent samples it from `materials/2026 VRTX AMKD Tepper Case Competition.pdf`. |
| CMU / Tepper | Carnegie Red | `#C41230` | [brand.cmu.edu/visual-identity/colors](https://brand.cmu.edu/visual-identity/colors), official. |
| CMU | Iron Gray | `#6D6E71` | Official. |
| CMU | Steel Gray | `#E0E0E0` | Official. |
| CMU campus palette | Weaver Blue (navy) | `#182C4B` | Official secondary color, "accents only." |
| Tepper Healthcare Club | Navy, red, and lavender (logo) | *sample from logo* | Eyeballed from the logo on the case cover. No published guide found. |
| CMU typefaces | **Open Sans** (sans) and **Source Serif Pro** (serif; current release is Source Serif 4) | — | Official CMU brand typefaces. Both are free Google Fonts. |

Tepper's own brand page did not publish colors or fonts. Tepper uses the CMU system (Carnegie Red, with the tagline "Data-Informed. Human-Driven.").

## Design constraints that apply to every option

- **Red is a problem color in financial charts.** Readers read red as "negative" or "loss." Keep Carnegie Red out of data encoding. Use it only for identity elements (title slide, a thin rule, slide numbers).
- **Purple and red side by side can clash.** Each option below lets one of them dominate and uses the other sparingly.
- **One accent marks "our recommendation"** consistently across every chart and table. Alternatives appear in gray.
- **Fonts: 2–3 maximum** (the workshop rule): a title font, a body font, and optionally a footnote size of the body font.
- **Font portability:** PDF export embeds fonts, so the submitted PDF is safe. However, all four teammates must install Open Sans and Source Serif 4 before editing the PPTX, or PowerPoint will substitute other fonts. The fallback pair is Georgia (titles) and Arial (body), which ship with every PC.
- **Logos:** Vertex, Tepper, and Healthcare Club logos go on the title slide only, unaltered, taken from official sources or the case PDF. Content slides stay clean.
- **Read deck:** the body text size must be readable in a PDF (about 12 pt minimum on a 16:9 slide) and footnotes about 8–9 pt.

## Options

### Option A — Sponsor-forward (recommended)
- **Dominant:** Vertex purple `#52247F` for titles, the recommendation accent, and the main numbers.
- **Neutrals:** Cool Gray `#63666A` for body text, Steel Gray `#E0E0E0` for rules and table fills.
- **CMU identity:** a Carnegie Red co-brand strip on the title slide and a thin red rule under the closing slide's heading only.
- **Fonts:** Source Serif 4 semibold for titles, Open Sans for body and footnotes.
- **Why:** the readers are Vertex executives, and the case document itself uses Vertex purple headings. A purple-led deck looks native to the audience. The serif titles and red strip still carry the CMU identity.
- **Risk:** it could read as "too Vertex." The title slide co-branding addresses that.

### Option B — Tepper-forward co-brand
- **Dominant:** Carnegie Red `#C41230` for the title bar, slide numbers, and section dividers.
- **Accent:** Vertex purple for the recommendation in charts.
- **Neutrals:** Iron Gray `#6D6E71` text, Steel Gray fills.
- **Fonts:** Open Sans only (bold titles, regular body).
- **Why:** it shows that the team comes from Tepper.
- **Risk:** red dominance fights with financial meaning, and red next to purple needs careful spacing.

### Option C — Healthcare Club navy, neutral
- **Dominant:** navy (Weaver Blue `#182C4B` or the club's navy) for titles and structure.
- **Accent:** Vertex purple for the recommendation; red limited to the title slide.
- **Fonts:** Open Sans only.
- **Why:** navy is the calmest executive palette and gives the deck a consulting-house look. It also borrows from the Healthcare Club logo.
- **Risk:** it is the least distinctive of the three.

## Decision needed from the team (Theme Checkpoint)
Before any content slides are built, the agent builds one suggestion deck containing all three options. Each option gets two slides: a co-branded title slide and a body slide with an action title, text, a sample chart, a footnote citation, and a slide number. The file is `work\theme\theme_suggestions.pdf`, and it arrives with the plan review (Gate A). Research does not wait for the pick. The team picks A, B, or C, or asks for a hybrid, and confirms the font pair, any time before Oct 1. The agent revises until the team approves, then saves the chosen look as `work\theme\master_template.pptx`. If no pick arrives by Oct 1, the agent uses Option A.
