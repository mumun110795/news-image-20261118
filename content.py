# -*- coding: utf-8 -*-
"""Story content for the re-grind: 'MIDNIGHT EDITION' — Wednesday 18 Nov 2026.
Briefs and decks are written terse on purpose: one line each at render size."""

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
