---
name: ai-look-check
description: Review any web page, landing page, deck screen or product UI for the tells that make it read as AI-generated or template-made, in the layout and in the copy, and report each with the fix. Use before a page goes live or is shown to anyone, and when someone asks "does this look AI-made", "does this look like a template", "why does my site feel generic" or asks for a design or copy review of a screen. Ends with a fresh-eyes gate: a reviewer with no context looks at screenshots at desktop and phone width. Findings are marked GIVEAWAY, CONFUSING or NIT, and nothing is changed without the owner's yes.
---

# AI look check

Visitors decide in a few seconds whether a page was made by someone who cared. A page that reads as generated loses that test before anyone reads a word. The tells are specific and learnable: a small label above every heading, the same section stamped 4 times, a grid of identical cards, 3 tidy benefits with 3 tidy icons, a line that says what something is not before it says what it is.

Each tell comes from the same root. A generator, or a template, makes the safe average choice at every step. 1 average choice is invisible. 10 of them in a row are a fingerprint. The fix is always the same in spirit: make a decision the average would not make, for a reason that belongs to this page.

## The order. Never change it

**Look, report, wait for the owner's yes, fix, look again.** Never fix while reviewing. Never change a word the owner wrote without showing them first.

## Step 1. Get the real page

Review what a visitor sees, never the code alone. A page can pass every code check and still read as generated.

1. Open the page in a real browser. Take full-page screenshots at 1440 pixels wide and at 390 pixels wide.
2. Scroll the whole page at both widths and look at the screenshots. Describe only what is on screen.
3. If the page is a deck, look at every screen in order. If it is a product, look at the 3 to 5 screens people use most.
4. Optional, for HTML: run `python scripts/look_scan.py <file-or-folder>`. It flags copy phrases, labels above headings, repeated section shapes and common visual tells. It is a first pass. It catches the countable tells and misses the ones you can only see.

## Step 2. Layout tells

For each tell, ask the question. If the answer is yes, it is a finding.

| Tell | Why it reads as generated | What to do instead |
|---|---|---|
| A small label, eyebrow or kicker above a heading ("Features", "How it works", "Step 2 · Build") | It is the single most common template move. It says the same thing as the heading in smaller type, so it adds nothing a person would choose to add. | Open the section on its heading. Move any step or issue number into a quiet meta line under the content. |
| A thin rule or a number with a trailing line before a label ("01 ____") | Decoration standing in for structure. | Delete it. Let spacing and the heading carry the section break. |
| The same section shape repeated: label, big heading, grey sub-line, grid | Every section built from 1 template. The visitor feels the pattern by the 3rd section. | Give each section the shape its content needs: a table for a comparison, a single large quote for proof, a list for steps, a full-width image for a demo. |
| A grid of identical cards, same size, same icon slot, same 2 lines | No element is more important than another, so nothing is. | Pick 1 dominant item per view. Make it clearly largest. Vary the rest by weight: 1 raised, some plain, some as a list. |
| Everything centred | Centring is the default when nobody decided. It also gives every block a different left edge. | Left-align body text and most headings. Hold each view to at most 2 left edges. Centre only a short, single statement. |
| Gradients, glow, glass or blur panels, soft drop shadows, very rounded cards | The default finish of most UI kits and image generators. | Pick 1 finish and hold it: flat with hairlines, or 1 clear depth. Use it everywhere. |
| An emoji or generic icon before every point | Icons that could sit on any site carry no meaning. | Remove them, or use a real image of the product, the work or the person. |
| A coloured pill or badge on every number | When every metric is highlighted, none is. | Colour only the 1 number that matters in that view. |
| 5 colours doing different jobs | Reads as a library palette. Nobody can tell what is clickable. | 1 colour for everything clickable. 1 for highlights. Greys for the rest. Status colours only on a real status. |
| Arrows between blocks, step diagrams for 2 steps | Process theatre. | Number the steps in the text. Draw a diagram only when the flow branches. |
| Callouts that narrate the page ("Here is the best part") | The page talking about itself. | Delete the callout. If the point matters, make it the heading. |
| An empty slot in a grid, a card with no visible action, placeholder text | Unfinished template residue. A person notices the hole before the content. | Fill the grid, change its column count or make it a list. Give every card a visible link or remove the card's card look. |
| Stock or generated hero imagery with no link to the product | Says "a website" and nothing about this business. | Show the real product, the real output or the real person. |
| Default chart styling, legend in a box, 5 series in 5 hues | The chart tool's choice, untouched. | Flat chart, light grid, 1 or 2 coloured series, the rest grey, 1 highlight on the point the sentence is about. |
| A third or fourth typeface, a trendy default face, an italic accent word in a headline | The fingerprint of a template or a generator prompt. | 1 face for headings, 1 for everything else, or 1 for both. No accent word. |

### Phone width, the tells that only show at 390 pixels

- Tables that wrap 1 letter per line in a narrow column. Fix: stack each row as a block, or let the table scroll sideways inside its own box.
- The same field label repeated above every value when a table collapses into cards. Fix: show the label once, or keep the table and let it scroll.
- Horizontal page scroll, a menu that cannot be opened, buttons under 44 pixels tall.

## Step 3. Copy tells

Generated copy has a rhythm people now recognise. Read every heading, button and first sentence aloud.

| Tell | Example | What to do instead |
|---|---|---|
| The contrast line | "It is not a tool, it is a partner." "Fast, not rushed." | Say what it is. "It drafts the first version of every proposal." |
| The rule-of-3 list, everywhere | "Faster. Smarter. Simpler." 3 benefits, 3 cards, 3 adjectives, in every section | Use the real number of things. 2 is fine. 5 is fine. Vary list lengths across the page. |
| Stock AI phrases | unlock, leverage, seamless, robust, elevate, empower, supercharge, game-changer, cutting-edge, next-level, transform your, harness, delve, navigate the landscape, in today's fast-paced world, at scale, all-in-one, effortless | Name the specific thing the product does, with a number if there is one. |
| The question-answer heading | "Tired of slow reports? Meet X." | State the outcome. "Reports in 10 minutes." |
| Labels as headings | "Features", "Benefits", "Our Process", "Why Choose Us" | Phrase the heading as the reader's question or a plain statement of what the section shows. |
| Vague proof | "Trusted by thousands", "Loved by teams", stars with no source | A real number with its source, a named customer with permission, or nothing. |
| Em dash rhythm | 3 or more em dashes on a page, often in pairs around an aside | Use a full stop or a comma. |
| The self-aware closer | "Ready to get started?", "The future of X is here" | 1 plain action: what happens when they click. |
| Same headings on every page of a set | Every case study or guide uses "The problem", "The solution", "The result" in the same order | Write each page's headings from its own content. |

## Step 4. The fresh-eyes gate

You have seen the page too many times to see it. So hand it to a reviewer who has not.

1. Start a fresh reviewer with no context: a new subagent, a new chat, or a person who has never seen the page. Give it only the screenshots at 1440 and 390 pixels, and the tell lists from Steps 2 and 3.
2. Ask 1 question: **"Does anything here look AI-generated?"** Ask for every instance, with where it is on the page.
3. The reviewer marks each finding:
   - **GIVEAWAY:** a visitor would suspect the page is generated or templated. Blocks launch.
   - **CONFUSING:** a visitor would not be sure what something is or what to do. Fix before launch.
   - **NIT:** small polish. Fix when convenient.
4. Fix, take new screenshots, and run the gate again with a new reviewer. A reviewer that saw the last round is no longer fresh.
5. The gate passes when a round returns 0 GIVEAWAYs. Expect 2 or 3 rounds. Each round finds smaller things, because the big tells hide the small ones.

Passing the code scan is never enough. Only the gate counts.

## Guardrails

1. **Never rewrite the owner's copy silently.** Propose the new line next to the old one. The owner picks.
2. **Never delete content.** Removing a section or a card goes in the report and waits for a yes.
3. **Fix the source.** If the page comes from a template, a builder or a script, fix it there, or the next build brings the tell back.
4. **1 fix can create a new tell.** Rebuilding 4 sections into 4 shapes can leave 1 grid with an empty slot. Look again after every fix.
5. **Keep the brand's own rules.** If the owner has a design system, a tell fix uses its colours, type and spacing. This skill decides what to change. The brand values stay as they are.

## Report format

1 table, GIVEAWAYs first, then CONFUSING, then NITs:

| Mark | Where | What a visitor sees | Why it reads as generated | Fix |
|---|---|---|---|---|

Then 1 line of totals, the round number, and whether the gate passed. No prose about what passed.

**Know when to stop.** 0 GIVEAWAYs and a short list of NITs you understand is done. Say so.
