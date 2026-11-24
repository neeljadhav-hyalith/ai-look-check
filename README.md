# ai-look-check

A Claude skill that reviews any web page, landing page, deck screen or product UI for the tells that make it read as AI-generated or template-made, in the layout and in the copy. Each finding comes with why it reads as generated and what to do instead, marked GIVEAWAY, CONFUSING or NIT. It ends with a fresh-eyes gate: a reviewer with no context looks at screenshots at desktop and phone width and answers 1 question, "does anything here look AI-generated?". It changes nothing without your yes.

Built by Neel Jadhav, Hyalith AI. More free tools: https://hyalith.ai/resources

## Install

**Claude Code:** copy this folder into `~/.claude/skills/ai-look-check/` (or your project's `.claude/skills/`). Then ask Claude: "does this page look AI-made?" and give it the URL or the file.

**Claude.ai:** Settings > Capabilities > Skills > Upload skill, and upload a zip of this folder. Then share a screenshot or a link and ask the same question.

## How to use

1. Point Claude at the page: a live URL, a local HTML file, or screenshots at desktop and phone width.
2. Ask: **"does this look AI-made?"** Claude reviews the layout and the copy and returns 1 table, GIVEAWAYs first.
3. Say which fixes to make. Then run the fresh-eyes gate again until a round finds 0 GIVEAWAYs.

## Run the scan on its own

Needs Python 3, no other installs. It reads HTML files and changes nothing.

```
python scripts/look_scan.py path/to/page-or-site-folder
```

It counts the tells a script can count: labels above headings, label-style headings, the same section shape repeated, "not X, but Y" lines, rule-of-3 fragments, stock AI phrases, em dashes, emoji, gradients, shadows and blur. It cannot see the page, so it never replaces the screenshots and the gate.

## What is inside

- `SKILL.md`: the instructions Claude follows: the layout tells, the phone-width tells, the copy tells, the fresh-eyes gate, the guardrails and the report format.
- `scripts/look_scan.py`: the first-pass scan for HTML.

## Licence

MIT. Use it, change it, share it.
