"""look_scan.py: first-pass scan of HTML pages for tells that read as AI-generated or template-made.

Usage:
    python look_scan.py <file.html | folder> [--max-dashes 2]

Python 3, standard library only. Reads files, changes nothing.
It catches countable tells. It cannot see the page: always finish with screenshots and the fresh-eyes gate.
Exit code 1 if any GIVEAWAY is found.
"""
import argparse
import html
import os
import re
import sys
from html.parser import HTMLParser

PHRASES = [
    "unlock", "leverage", "seamless", "seamlessly", "robust", "elevate", "empower", "supercharge",
    "game-changer", "game changer", "cutting-edge", "cutting edge", "next-level", "next level",
    "transform your", "harness", "delve", "navigate the", "fast-paced world", "at scale",
    "all-in-one", "effortless", "effortlessly", "revolutionise", "revolutionize", "synergy",
    "holistic", "deep dive", "ready to get started", "the future of", "why choose us",
    "look no further", "to the next level", "in today's",
]
LABEL_HEADINGS = {"features", "benefits", "our process", "why choose us", "how it works", "about us",
                  "our services", "testimonials", "faq", "pricing", "overview", "introduction"}
CONTRAST = re.compile(r"\b(?:it is|it's|this is|this isn't|this is not|we are|we're)?\s*not (?:just )?(?:a |an |the )?[\w\s'-]{1,30}?[,;:—–-]\s*(?:but |it is |it's |it’s )?(?:a |an |the )?\w+", re.I)
X_NOT_Y = re.compile(r"\b\w+,\s+not\s+\w+[.!]", re.I)
TRIAD = re.compile(r"\b([A-Z]\w+)\.\s+([A-Z]\w+)\.\s+([A-Z]\w+)\.")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CSS_TELLS = [
    (re.compile(r"linear-gradient|radial-gradient", re.I), "gradient"),
    (re.compile(r"backdrop-filter", re.I), "glass or blur panel"),
    (re.compile(r"box-shadow\s*:\s*(?!none)", re.I), "drop shadow"),
    (re.compile(r"font-family[^;]*\b(Inter|Space Grotesk|Outfit|Poppins)\b", re.I), "default template typeface"),
]
HEAD = {"h1", "h2", "h3"}
TEXTY = {"p", "span", "div", "small", "strong", "em", "b", "label"}
BLOCK = {"section", "article", "header", "footer", "main", "div", "ul", "ol", "table", "figure",
         "p", "h1", "h2", "h3", "h4", "img", "blockquote", "form"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.skip = [], 0
        self.text = []            # visible text chunks
        self.headings = []        # (level, text)
        self.prev_text = None     # (tag, text) of the last closed short text element
        self.labels = []          # (label, heading)
        self.sections = []        # tag signature per <section>
        self.sec_depth, self.sec_sig = None, []
        self.cur = None
        self.css = []

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "noscript"):
            self.skip += 1
        if tag == "style":
            self.skip += 1
            self.in_style = True
        for k, v in attrs:
            if k == "style" and v:
                self.css.append(v)
        if tag in HEAD:
            # a label counts only if it is the element directly before the heading, at the same level or just inside it
            if not (self.prev_text and self.prev_text[2] >= len(self.stack) + 1 and not self.prev_text[3]):
                self.prev_text = None
        else:
            self.prev_text = None
        if self.cur is not None and tag in ("a", "button", "img", "svg"):
            self.cur[2] = True
        self.stack.append(tag)
        if tag == "section" and self.sec_depth is None:
            self.sec_depth, self.sec_sig = len(self.stack), []
        elif self.sec_depth is not None and len(self.stack) == self.sec_depth + 2 and tag in BLOCK:
            self.sec_sig.append(tag)
        if tag in HEAD or tag in TEXTY:
            self.cur = [tag, "", False]

    def handle_endtag(self, tag):
        if tag in ("script", "noscript", "style"):
            self.skip = max(0, self.skip - 1)
        if self.cur and self.cur[0] == tag:
            t = " ".join(self.cur[1].split())
            if tag in HEAD:
                self.headings.append((tag, t))
                lab = self.prev_text[1] if self.prev_text else ""
                if 0 < len(lab) <= 40 and len(lab.split()) <= 6 and not lab.endswith((".", "!", "?")):
                    self.labels.append((self.prev_text[1], t))
                self.prev_text = None
            elif t:
                self.prev_text = (tag, t, len(self.stack), self.cur[2])
            self.cur = None
        if self.stack:
            if self.sec_depth is not None and len(self.stack) == self.sec_depth and tag == "section":
                self.sections.append(tuple(self.sec_sig))
                self.sec_depth = None
            self.stack.pop()

    def handle_data(self, data):
        if self.skip:
            if self.stack and self.stack[-1] == "style":
                self.css.append(data)
            return
        if data.strip():
            self.text.append(data)
            if self.cur is not None:
                self.cur[1] += data
            else:
                self.prev_text = None


def scan(path, max_dashes):
    with open(path, encoding="utf-8", errors="replace") as f:
        raw = f.read()
    p = Page()
    p.feed(raw)
    body = html.unescape(" ".join(" ".join(p.text).split()))
    low = body.lower()
    found = []

    for label, head in p.labels:
        found.append(("GIVEAWAY", "Label above a heading", f'"{label}" above "{head[:50]}"'))
    for lvl, head in p.headings:
        if head.strip().lower().rstrip(".?") in LABEL_HEADINGS:
            found.append(("CONFUSING", "Label used as a heading", f'{lvl}: "{head}"'))
    if len(p.sections) >= 3:
        counts = {}
        for sig in p.sections:
            if sig:
                counts[sig] = counts.get(sig, 0) + 1
        for sig, n in counts.items():
            if n >= 3:
                found.append(("GIVEAWAY", "Same section shape repeated", f"{n} sections built as {' > '.join(sig)}"))
    for m in CONTRAST.finditer(body):
        s = m.group(0).strip()
        if re.search(r"[,;:—–-]\s*(but|it is|it's|it’s)\b", s, re.I):
            found.append(("CONFUSING", '"Not X, but Y" line (read it in context)', f'"{s[:70]}"'))
    for m in X_NOT_Y.finditer(body):
        found.append(("NIT", '"X, not Y" line', f'"{m.group(0)}"'))
    for m in TRIAD.finditer(body):
        found.append(("NIT", "Rule-of-3 fragments", f'"{m.group(0)}"'))
    hits = sorted({ph for ph in PHRASES if re.search(r"\b" + re.escape(ph) + r"\b", low)})
    if hits:
        found.append(("CONFUSING", "Stock AI phrases", ", ".join(hits)))
    dashes = body.count("—")
    if dashes > max_dashes:
        found.append(("NIT", "Em dash rhythm", f"{dashes} em dashes in the visible text"))
    em = EMOJI.findall(body)
    if len(em) >= 3:
        found.append(("CONFUSING", "Emoji as icons", f"{len(em)} emoji in the visible text"))
    css = " ".join(p.css)
    for rx, name in CSS_TELLS:
        n = len(rx.findall(css))
        if n:
            found.append(("NIT", f"Visual tell: {name}", f"{n} in inline or page CSS"))
    return found


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target")
    ap.add_argument("--max-dashes", type=int, default=2)
    a = ap.parse_args()
    files = []
    if os.path.isdir(a.target):
        for root, _, names in os.walk(a.target):
            files += [os.path.join(root, n) for n in names if n.lower().endswith((".html", ".htm"))]
    else:
        files = [a.target]
    order = {"GIVEAWAY": 0, "CONFUSING": 1, "NIT": 2}
    rows, visual = [], {}
    for fp in sorted(files):
        name = os.path.relpath(fp, a.target) if os.path.isdir(a.target) else os.path.basename(fp)
        for mark, tell, detail in scan(fp, a.max_dashes):
            if tell.startswith("Visual tell") and len(files) > 1:
                visual.setdefault(tell, []).append(name)  # shared CSS: 1 row per tell, not 1 per page
            else:
                rows.append((order[mark], mark, name, tell, detail))
    for tell, pages in visual.items():
        rows.append((2, "NIT", f"{len(pages)} pages", tell, "check by eye whether it is visible and deliberate"))
    rows.sort()
    print("| Mark | Page | Tell | Found |\n|---|---|---|---|")
    for _, mark, page, tell, detail in rows:
        print(f"| {mark} | {page} | {tell} | {detail.replace('|', '/')} |")
    tot = {k: sum(1 for r in rows if r[1] == k) for k in order}
    print(f"\n{len(files)} pages scanned · {tot['GIVEAWAY']} GIVEAWAY · {tot['CONFUSING']} CONFUSING · {tot['NIT']} NIT")
    print("This scan counts tells. It cannot see the page. Finish with screenshots and the fresh-eyes gate.")
    sys.exit(1 if tot["GIVEAWAY"] else 0)


if __name__ == "__main__":
    main()
