# -*- coding: utf-8 -*-
"""MIDNIGHT EDITION — Wednesday 18 November 2026 in one image.

Entry for make.fun news-image-20261118. A single self-contained
program: the story content — 50 stories, all from Wednesday
18 November 2026 — is inlined below, and the drawing code renders the
front page with PIL. Dark tabloid layout: a giant WEDNESDAY masthead,
one dominant Iran/Hormuz lead with original code-drawn artwork, a
numbers ticker, colour-coded region cards, briefs grouped by region,
and an on-page Date Check box naming the Tuesday stories kept off.

Running `python3 main.py` writes the finished page to ./entry.png
(or to the path given as argv[1]). The render is deterministic:
same fonts, same code, same bytes on every run. Python 3 + Pillow;
no embedded image data, no local imports.
"""
import os, sys, math
from PIL import Image, ImageDraw, ImageFont

# =====================================================================
# CONTENT — every story happened, or was first reported, on
# Wednesday 18 November 2026. Briefs and decks are written terse on
# purpose: one line each at render size.
# =====================================================================

HERO = {
    "kicker": "MIDDLE EAST · CONFLICT · STRAIT OF HORMUZ",
    "headline": "IRAN FIRES ON US BASES AS HORMUZ BURNS",
    "deck": ("Tehran's missiles fall on Kuwait and Bahrain before dawn, answering a US strike on "
             "Qeshm Island. A tanker burns near Hormuz — one sailor missing, 11 hurt."),
    "src": "REUTERS · AP · WEDNESDAY",
}

DUO = [
    {
        "kicker": "ASIA-PACIFIC · DIPLOMACY · SHENZHEN",
        "headline": "THREE PRESIDENTS, ONE ROOM IN SHENZHEN",
        "deck": ("Xi greets Trump on the tarmac as APEC opens; a first trilateral "
                 "with Putin follows on Thursday."),
        "art": "apec",
    },
    {
        "kicker": "NORTH AMERICA · TECH · SANTA CLARA",
        "headline": "NVIDIA'S RECORD $115.8bn QUARTER — AND NO WAY BACK FOR HUANG",
        "deck": ("Revenue beats forecasts and guidance hits $130bn, yet the board "
                 "bars Huang's return as CEO."),
        "art": "chip",
    },
]

# (region_color_key, kicker, headline, deck) — decks <= 45 chars = one line
CARDS = [
    ("NA", "NORTH AMERICA · HEALTH", "AMERICA LOSES MEASLES-FREE STATUS AFTER 26 YEARS",
     "PAHO ends a 26-year era; 5,412 cases (CDC)."),
    ("NA", "NORTH AMERICA · POLITICS", "PELTOLA WINS ALASKA — THE SENATE GOES 56–44",
     "Peltola beats Sullivan; Dems take Senate."),
    ("EU", "EUROPE · WAR · UKRAINE", "141 DRONES IN A SINGLE NIGHT OVER UKRAINE",
     "126 downed by 08:00; six hurt in Dnipro."),
    ("EU", "EUROPE · DIPLOMACY · LONDON", "\u201cTRUSTED PARTNERSHIP\u201d VANISHES FROM THE EU DRAFT",
     "Cut days before Friday's Brussels summit."),
    ("EU", "EUROPE · WAR & MONEY", "EU OFFERS KYIV A \u20ac45 BILLION LOAN FOR 2027",
     "Brussels funds Kyiv's 2027 war budget."),
    ("AF", "AFRICA · HEALTH · DR CONGO", "EBOLA STAYS A GLOBAL EMERGENCY, WHO RULES",
     "CDC's Wednesday count: 11,536 cases."),
    ("ME", "MIDDLE EAST · WAR · GAZA", "ISRAELI TROOPS ENTER HAMAS-HELD GAZA AGAIN",
     "First since the 2025 ceasefire — Israel."),
    ("ME", "MIDDLE EAST · DIPLOMACY · GAZA", "BOARD OF PEACE FAULTS BOTH SIDES OVER THE TRUCE",
     "Israel and Hamas both faulted on truce."),
    ("LA", "LATIN AMERICA · DIPLOMACY · CARACAS", "WASHINGTON SIGNS A MILITARY DEAL IN CARACAS",
     "Hegseth: a \u201ccompliant security partner\u201d."),
    ("OC", "OCEANIA · DIPLOMACY · CANBERRA", "AUSTRALIA SANCTIONS WEST BANK SETTLERS",
     "Wong targets settler-violence groups."),
    ("MK", "MARKETS · NEW YORK", "GOLD BREAKS BELOW $3,800 FOR THE FIRST TIME IN A YEAR",
     "Sensex, Nifty records; Fed minutes loom."),
    ("SC", "SCIENCE & SPACE · DEEP SPACE", "VOYAGER 1 IS NOW A FULL LIGHT-DAY FROM HOME",
     "Its signals take a day to reach home."),
]

TICKER = ("THE DAY IN NUMBERS — 141 DRONES OVER UKRAINE · $115.8bn NVIDIA QUARTER · 11,536 EBOLA CASES · "
          "SENATE 56–44 · VOYAGER AT 1 LIGHT-DAY · 950,000 DISPLACED IN GAZA (WHO)")

# (header, [(lead_in, text), ...]) — lead_in + text <= ~60 chars = one line
BRIEF_COLS = [
    [
        ("EUROPE", [
            ("Bratislava —", "Slovaks protest PM Fico's government."),
            ("Brussels —", "EU acts on Temu over illegal product sales."),
            ("Prague —", "Two locomotives collide; many wounded."),
            ("Bucharest —", "A 5.3-magnitude quake strikes Romania."),
            ("Rwanda plan —", "Five EU states plan Rwanda return hubs."),
        ]),
        ("MIDDLE EAST", [
            ("Riyadh —", "Saudi says it intercepted a Houthi missile."),
            ("Baghdad —", "Iraq orders Kata'ib Hezbollah out of Jurf al-Sakhar."),
            ("Beirut —", "Lebanon hails improving ties with Syria."),
        ]),
        ("LATIN AMERICA", [
            ("Miami —", "Pastor Sanon convicted over Mo\u00efse killing."),
            ("The Amazon —", "Brazil reports contact with isolated group."),
            ("La Paz —", "Bolivia among nine to get Ukrainian wheat."),
        ]),
    ],
    [
        ("ASIA-PACIFIC", [
            ("Seoul —", "Lee and Xi discuss peace, stability (Yonhap)."),
            ("Taipei —", "Taiwan logs 10 PLA sorties, 11 navy vessels."),
            ("Bangkok —", "Arsenic in Thai rivers traced to Myanmar."),
            ("Odisha —", "Cyclone Akvan: evacuations, schools shut."),
            ("Shenzhen —", "Canada's Carney meets Trump at APEC."),
        ]),
        ("NORTH AMERICA", [
            ("Washington —", "Jeffries wins Democrats' Speaker nomination."),
            ("Washington —", "DHS chief Mullin faces a House hearing."),
            ("Washington —", "Venezuela TPS case reaches Supreme Court."),
            ("Nationwide —", "Waymo pauses driverless freeway rides."),
            ("Albany —", "Hochul clashes over ICE detention sites."),
        ]),
        ("SCIENCE & TECH", [
            ("Washington · Seoul —", "Agencies warn urgently over Java flaws."),
            ("United Nations —", "Chemical exposure begins before birth."),
        ]),
    ],
    [
        ("AFRICA", [
            ("W. Kordofan —", "Army claims gains vs RSF; unverified."),
            ("Sudan —", "UN: 2,230 civilian deaths in 10 months."),
            ("Abuja —", "Nigeria approves state police by law."),
            ("Johannesburg —", "Water restrictions begin this weekend."),
            ("Tunis —", "Voluntary migrant returns continue."),
        ]),
        ("OCEANIA", [
            ("Sydney —", "Australia's gender pay gap: a record low."),
            ("Wellington —", "NZ lifts tsunami warning after sea activity."),
        ]),
        ("SPORT", [
            ("Turin —", "Alcaraz d. Medvedev 6-2 6-4; Zverev d. Shelton — both into the semis."),
            ("Turin —", "Tiafoe d. Cobolli 7-6(6) 6-0, first Finals win."),
            ("London —", "Buurman's 87th-minute goal: Chelsea 1-0 PSG."),
            ("Nations League —", "England 3-2 Spain ends 43-match run; Germany 5-0 Netherlands."),
            ("Hobart —", "Duckett's 133 seals England's ODI series win."),
        ]),
    ],
]

TALLY = "EUROPE 8 · NORTH AMERICA 8 · ASIA-PACIFIC 6 · MIDDLE EAST 6 · AFRICA 6 · SPORT 5 · LATIN AMERICA 4 · OCEANIA 3 · SCIENCE & SPACE 3 · MARKETS 1"

DATECHECK = (
    "Every story here happened, or was first reported, on Wednesday 18 November 2026 — somewhere on Earth. "
    "KEPT OFF as Tuesday's news: the \u201cEbola passes 11,000 cases\u201d headline (Wednesday's own step is the emergency ruling), "
    "the Quad meeting in Manila, the Kerch Bridge collapse, Japan's airspace protest, Haiti's El Salvador pact and Wall Street's "
    "Tuesday sell-off. Two stories landed late Tuesday US time and led Wednesday's pages — PAHO's measles ruling and Nvidia's "
    "results; both are carried here and flagged in this box. Disputed claims name their maker; figures name who counted them."
)

# =====================================================================
# DRAWING PROGRAM — renders the page top to bottom with PIL.
# Deterministic: same fonts, same code.
# =====================================================================

W, H = 1024, 1024
M = 26
CW = W - 2 * M

INK    = (13, 13, 16)
PANEL  = (22, 22, 29)
PANEL2 = (27, 27, 36)
PAPER  = (246, 242, 233)
DIM    = (178, 176, 168)
FAINT  = (120, 118, 112)
RED    = (230, 46, 32)
GOLD   = (242, 160, 7)
TEAL   = (46, 196, 182)
SKY    = (64, 132, 214)
GREEN  = (74, 190, 110)
PINK   = (232, 110, 168)
WHITE  = (255, 255, 255)

# Fonts are vendored in fonts/ next to this script (Noto Sans Display and
# Liberation Sans, both SIL Open Font License 1.1) and resolved relative to
# this file, so the program renders identically on any machine.
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")
F = os.path.join(BASE, "noto") + os.sep
def font(name, size): return ImageFont.truetype(F + name, size)
BLACK, CBLACK, XBOLD, BOLD, SEMI, MED, REG = ("NotoSansDisplay-Black.ttf",
    "NotoSansDisplay-CondensedBlack.ttf", "NotoSansDisplay-ExtraBold.ttf",
    "NotoSansDisplay-Bold.ttf", "NotoSansDisplay-SemiBold.ttf",
    "NotoSansDisplay-Medium.ttf", "NotoSansDisplay-Regular.ttf")
LIB  = os.path.join(BASE, "liberation", "LiberationSans-Regular.ttf")
LIBB = os.path.join(BASE, "liberation", "LiberationSans-Bold.ttf")
def lib(s):  return ImageFont.truetype(LIB, s)
def libb(s): return ImageFont.truetype(LIBB, s)

img = Image.new("RGB", (W, H), INK)
d = ImageDraw.Draw(img)

def tw(t, f): return d.textlength(t, font=f)
def wrap(text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if tw(t, fnt) <= width or not cur: cur = t
        else: lines.append(cur); cur = w_
    if cur: lines.append(cur)
    return lines
def fit_wrap(text, name, sizes, width, max_lines):
    for s in sizes:
        f = font(name, s)
        ls = wrap(text, f, width)
        if len(ls) <= max_lines: return f, ls
    f = font(name, sizes[-1])
    return f, wrap(text, f, width)[:max_lines]
def block(x, y, text, fnt, fill, width, lh, max_lines=None):
    ls = wrap(text, fnt, width)
    if max_lines: ls = ls[:max_lines]
    for ln in ls:
        d.text((x, y), ln, font=fnt, fill=fill); y += lh
    return y

# ---------------------------------------------------------------- masthead
y = 12
d.text((M, y), "THE WORLD IN ONE PAGE", font=font(XBOLD, 14.5), fill=RED)
r = "50 STORIES · 10 REGIONS · ONE DAY ONLY"
d.text((W - M - tw(r, font(XBOLD, 14.5)), y), r, font=font(XBOLD, 14.5), fill=DIM)
y += 22
d.text((M - 2, y), "WEDNESDAY", font=font(BLACK, 76), fill=PAPER)
bx, by, bw_, bh_ = W - M - 188, y + 1, 188, 76
d.rectangle([bx, by, bx + bw_, by + bh_], fill=RED)
d.text((bx + 14, by - 2), "18", font=font(BLACK, 50), fill=WHITE)
d.text((bx + 94, by + 7), "NOV", font=font(CBLACK, 24), fill=WHITE)
d.text((bx + 94, by + 34), "2026", font=font(CBLACK, 24), fill=WHITE)
d.text((bx + 14, by + 56), "ONE DAY ONLY", font=font(XBOLD, 11), fill=WHITE)
y += 84
d.text((M, y), "18 NOVEMBER 2026", font=font(CBLACK, 26), fill=GOLD)
sub = "·  THE DAY THE WORLD TALKED ABOUT — ALL OF IT, ON ONE PAGE"
d.text((M + tw("18 NOVEMBER 2026", font(CBLACK, 26)) + 8, y + 5), sub, font=font(SEMI, 13.5), fill=DIM)
y += 28
d.rectangle([M, y, W - M, y + 4], fill=RED)
y += 8
tf, _ = fit_wrap(TICKER, XBOLD, [13, 12.5, 12, 11.5, 11], CW, 1)
d.text((M, y), TICKER, font=tf, fill=RED)
y += 19

# ---------------------------------------------------------------- hero art
def hero_art(x, yy, w_, h_):
    d.rectangle([x, yy, x + w_, yy + h_], fill=(38, 16, 20))
    for i, c in enumerate([(54, 22, 24), (84, 28, 24), (120, 38, 26), (150, 52, 30)]):
        d.rectangle([x, yy + i * 13, x + w_, yy + (i + 1) * 13], fill=c)
    cx, cy, r_ = x + int(w_ * 0.68), yy + int(h_ * 0.50), 28
    d.ellipse([cx - r_, cy - r_, cx + r_, cy + r_], fill=(255, 122, 40))
    d.ellipse([cx - r_ + 5, cy - r_ + 5, cx + r_ - 5, cy + r_ - 5], fill=(255, 160, 60))
    sea_y = yy + int(h_ * 0.60)
    d.rectangle([x, sea_y, x + w_, yy + h_], fill=(16, 34, 54))
    for i in range(5):
        ly = sea_y + 8 + i * 7
        d.line([x + 8 + (i % 3) * 22, ly, x + w_ - 30 - (i % 2) * 40, ly], fill=(44, 84, 118), width=2)
    tx, ty = x + 22, sea_y + 11
    d.polygon([(tx, ty + 15), (tx + 132, ty + 15), (tx + 122, ty + 25), (tx + 10, ty + 25)], fill=(6, 8, 12))
    d.rectangle([tx + 14, ty + 8, tx + 113, ty + 15], fill=(6, 8, 12))
    d.rectangle([tx + 92, ty - 2, tx + 107, ty + 8], fill=(6, 8, 12))
    d.rectangle([tx + 26, ty + 3, tx + 38, ty + 8], fill=(200, 60, 40))
    d.rectangle([tx + 46, ty + 3, tx + 58, ty + 8], fill=(220, 120, 50))
    fx, fy = tx + 117, ty + 4
    d.polygon([(fx, fy + 7), (fx + 6, fy - 8), (fx + 12, fy + 7)], fill=(255, 110, 30))
    d.polygon([(fx + 3, fy + 7), (fx + 6, fy - 1), (fx + 9, fy + 7)], fill=(255, 190, 60))
    d.ellipse([fx + 2, fy - 22, fx + 16, fy - 10], fill=(70, 66, 70))
    d.ellipse([fx + 7, fy - 30, fx + 24, fy - 16], fill=(56, 52, 58))
    for (sx, ex, peak) in [(x + 16, x + 188, 48), (x + 46, x + 232, 62), (x + 78, x + 262, 52)]:
        pts = []
        for t_ in range(0, 21):
            u = t_ / 20.0
            pts.append((sx + (ex - sx) * u, (yy + 6) + (sea_y - yy - 6) * u - math.sin(u * math.pi) * peak * 0.38 - u * u * 5))
        d.line(pts, fill=(255, 214, 150), width=2)
        exx, eyy = pts[-1]
        d.ellipse([exx - 3, eyy - 3, exx + 3, eyy + 3], fill=(255, 230, 170))
    d.polygon([(x + w_ - 106, yy + h_), (x + w_ - 52, sea_y + 18), (x + w_, sea_y + 25), (x + w_, yy + h_)], fill=(8, 10, 14))

# ---------------------------------------------------------------- hero
hero_h = 164
d.rectangle([M, y, W - M, y + hero_h], fill=PANEL)
d.rectangle([M, y, W - M, y + 4], fill=RED)
hero_art(W - M - 324, y + 4, 324, hero_h - 4)
tx = M + 18
d.text((tx, y + 11), HERO["kicker"], font=font(XBOLD, 12.5), fill=RED)
hy = y + 30
hf, hls = fit_wrap(HERO["headline"], CBLACK, [48, 46, 44], 590, 2)
for ln in hls:
    d.text((tx, hy), ln, font=hf, fill=PAPER); hy += int(hf.size * 1.05)
hy += 3
block(tx, hy, HERO["deck"], font(REG, 13.5), DIM, 590, 16.5, max_lines=2)
y += hero_h + 7

# ---------------------------------------------------------------- duo art
def apec_art(x, yy, w_, h_):
    d.rectangle([x, yy, x + w_, yy + h_], fill=(24, 30, 52))
    cx0 = x + w_ // 2
    for i, c in enumerate([(230, 46, 32), (242, 160, 7), (64, 132, 214)]):
        cx = cx0 + (i - 1) * 26
        d.ellipse([cx - 28, yy + 10, cx + 28, yy + 66], outline=c, width=5)
    base = yy + h_ - 19
    bx = x + 9
    for b in [8, 14, 11, 19, 13, 16, 10]:
        d.rectangle([bx, base - b, bx + 8, base], fill=(90, 110, 150)); bx += 13
    d.line([x + 6, base + 4, x + w_ - 6, base + 4], fill=(140, 160, 190), width=2)

def chip_art(x, yy, w_, h_):
    d.rectangle([x, yy, x + w_, yy + h_], fill=(10, 34, 26))
    s = 50
    cx, cy = x + (w_ - s) // 2, yy + (h_ - s) // 2
    for i in range(5):
        px = cx - 14 + i * 20
        d.line([px, cy - 11, px, cy], fill=GOLD, width=3)
        d.line([px, cy + s, px, cy + s + 11], fill=GOLD, width=3)
        py = cy - 14 + i * 20
        d.line([cx - 11, py, cx, py], fill=GOLD, width=3)
        d.line([cx + s, py, cx + s + 11, py], fill=GOLD, width=3)
    d.rectangle([cx, cy, cx + s, cy + s], fill=(16, 90, 60), outline=(74, 220, 140), width=3)
    d.rectangle([cx + 11, cy + 11, cx + s - 11, cy + s - 11], outline=(120, 240, 180), width=2)

# ---------------------------------------------------------------- duo row
duo_h = 99
dw = (CW - 10) // 2
for i, item in enumerate(DUO):
    x = M + i * (dw + 10)
    accent = GOLD if i == 0 else GREEN
    d.rectangle([x, y, x + dw, y + duo_h], fill=PANEL)
    d.rectangle([x, y, x + dw, y + 3], fill=accent)
    aw = 106
    (apec_art if item["art"] == "apec" else chip_art)(x + dw - aw, y + 3, aw, duo_h - 3)
    tx = x + 13
    d.text((tx, y + 8), item["kicker"], font=font(XBOLD, 9.5), fill=accent)
    hy = y + 22
    hf, hls = fit_wrap(item["headline"], CBLACK, [23, 22, 21, 20], dw - aw - 24, 2)
    for ln in hls:
        d.text((tx, hy), ln, font=hf, fill=PAPER); hy += int(hf.size * 1.05)
    block(tx, hy + 2, item["deck"], font(REG, 11), DIM, dw - aw - 24, 14, max_lines=2)
y += duo_h + 7

# ---------------------------------------------------------------- lead cards
RCOLORS = {"EU": SKY, "NA": RED, "ME": GOLD, "AF": GREEN, "AP": TEAL, "LA": PINK, "OC": (150, 130, 255), "SC": (120, 200, 255), "MK": (255, 200, 90)}
cols, rows, gap, card_h = 4, 3, 8, 66
card_w = (CW - gap * (cols - 1)) // cols
for idx, (rk, kicker, head, deck) in enumerate(CARDS):
    cx = M + (idx % cols) * (card_w + gap)
    cy = y + (idx // cols) * (card_h + gap)
    d.rectangle([cx, cy, cx + card_w, cy + card_h], fill=PANEL2)
    d.rectangle([cx, cy, cx + card_w, cy + 3], fill=RCOLORS[rk])
    d.text((cx + 9, cy + 6), kicker, font=font(XBOLD, 7.5), fill=RCOLORS[rk])
    hy = cy + 16
    hf, hls = fit_wrap(head, CBLACK, [16.5, 15.5, 14.5], card_w - 18, 2)
    for ln in hls:
        d.text((cx + 9, hy), ln, font=hf, fill=PAPER); hy += int(hf.size * 1.07)
    df, dls = fit_wrap(deck, None, [0], card_w - 18, 1) if False else (lib(9.6), wrap(deck, lib(9.6), card_w - 18))
    assert len(dls) == 1, f"deck wraps: {deck}"
    d.text((cx + 9, hy + 1), deck, font=df, fill=DIM)
y += rows * card_h + (rows - 1) * gap + 7

# ---------------------------------------------------------------- briefs (auto-fit line height)
d.text((M, y), "THE REST OF WEDNESDAY", font=font(BLACK, 19), fill=PAPER)
tr = "35 MORE STORIES, BY REGION"
d.text((W - M - tw(tr, font(XBOLD, 11)), y + 5), tr, font=font(XBOLD, 11), fill=RED)
y += 23
brief_top = y
col_w = (CW - 2 * 16) // 3
BF, BBF = lib(10), libb(10)
def col_height(col, lh):
    hgt = 0.0
    for header, items in col:
        hgt += 13
        for lead_in, txt in items:
            hgt += len(wrap(lead_in + " " + txt, BF, col_w)) * lh + 1.5
        hgt += 3.5
    return hgt
dc_lines = len(wrap(DATECHECK, lib(10.3), CW - int(tw("DATE CHECK  ", font(BLACK, 14))) - 4))
reserve = 15 + 9 + dc_lines * 12 + 4 + 12 + 4   # tally + rule + datecheck + gap + footer + slack
BLH = 10.4
for cand in (11.9, 11.6, 11.2, 10.8, 10.4):
    if brief_top + max(col_height(c, cand) for c in BRIEF_COLS) + reserve <= H - 4:
        BLH = cand; break
brief_h = max(col_height(c, BLH) for c in BRIEF_COLS)
for ci, col in enumerate(BRIEF_COLS):
    x = M + ci * (col_w + 16)
    cy = brief_top
    for header, items in col:
        d.text((x, cy), header, font=font(XBOLD, 10.5), fill=GOLD); cy += 13
        for lead_in, txt in items:
            lines = wrap(lead_in + " " + txt, BF, col_w)
            for li, ln in enumerate(lines):
                if li == 0 and ln.startswith(lead_in):
                    d.text((x, cy), lead_in, font=BBF, fill=PAPER)
                    d.text((x + tw(lead_in + " ", BBF), cy), ln[len(lead_in):].lstrip(), font=BF, fill=DIM)
                else:
                    d.text((x, cy), ln, font=BF, fill=DIM)
                cy += BLH
            cy += 1.5
        cy += 3.5
y = brief_top + brief_h + 2
d.text((M, y), TALLY, font=font(SEMI, 10.5), fill=FAINT)
y += 14

# ---------------------------------------------------------------- date check + footer
d.rectangle([M, y, W - M, y + 2], fill=RED)
y += 7
d.text((M, y), "DATE CHECK", font=font(BLACK, 14), fill=RED)
dc_x = M + tw("DATE CHECK  ", font(BLACK, 14))
yf = block(dc_x, y + 1, DATECHECK, lib(10.3), DIM, W - M - dc_x, 12)
y = max(y + 16, yf) + 3
foot = "Sources: Reuters · AP · AFP · CNN · BBC · The Guardian · NYT · ABC · Yonhap · NASA JPL · WHO · PAHO · CDC · UN — full attribution in SOURCES.md (repository). Original artwork, drawn in code."
block(M, y, foot, font(SEMI, 9.5), FAINT, CW, 11.5, max_lines=1)
print("BLH:", BLH, "| brief_h:", round(brief_h, 1), "| final y:", round(y + 12, 1))
out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
img.save(out)
print("saved", out)
