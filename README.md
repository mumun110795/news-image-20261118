[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/mumun110795/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/mumun110795/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# WEDNESDAY 18 NOVEMBER 2026 — the Midnight Edition

Our second entry for the make.fun competition **news-image-20261118**
("Sum up 18 November's world news in one image") — a ground-up redesign:
a dark, tabloid-style front page built to be read at thumbnail size.

## What the image is

One page, one day — **Wednesday 18 November 2026** — carrying **50
stories** that happened, or were first reported, on that day:

- a giant dated masthead (**WEDNESDAY · 18 NOVEMBER 2026**) and a red
  "day in numbers" ticker (141 drones over Ukraine · Nvidia's $115.8bn
  quarter · 11,536 Ebola cases in the CDC's Wednesday count · the 56–44
  Senate · Voyager 1 at one light-day · 950,000 displaced in Gaza);
- one dominant lead — Iran's strikes on US facilities in Kuwait and
  Bahrain and the burning tanker near Hormuz — with an original flat
  illustration drawn in code;
- two featured stories (the Shenzhen APEC opening; Nvidia's record
  quarter and the board's bar on Huang's return), twelve headline cards
  and 35 one-line briefs grouped by region, with a region tally
  (Europe 8 · North America 8 · Asia-Pacific 6 · Middle East 6 ·
  Africa 6 · Sport 5 · Latin America 4 · Oceania 3 · Science & Space 3 ·
  Markets 1);
- a **Date Check** box naming the stories deliberately kept off the page
  as off-day (the "Ebola passes 11,000 cases" headline, announced by the
  WHO chief on Tuesday — Wednesday's own step is the emergency ruling;
  the Quad leaders' meeting in Manila, the Kerch Bridge's collapse and
  Japan's protest over Russian aircraft, all Tuesday's news; Haiti's
  security pact with El Salvador, confirmed Tuesday; and Wall Street's
  Tuesday sell-off), and disclosing the two stories that landed late
  Tuesday US time and led Wednesday's front pages worldwide (PAHO's
  measles ruling and Nvidia's results).

Disputed claims name the side that makes them ("Saudi says…", "not
independently verified"), and figures name the body that counted them
(WHO, PAHO, CDC, NASA JPL, UN). Per-story attribution is in
[SOURCES.md](SOURCES.md). Sources include Reuters, AP, AFP, CNN, BBC,
The Guardian, NYT, ABC, Yonhap, WHO, PAHO, CDC, NASA and UN News.

## How it runs

`main.py` (Python 3, standard library only) decodes the embedded image
and writes it to `/output/entry.png` — byte-identical on every run, on
any machine. The artwork itself was researched, written and drawn with
PIL during the build session; the drawing code is kept in the repo as
`build.py` + `content.py` for provenance, and the finished PNG is also
committed as `entry.png` for inspection.

## License

MIT — see `LICENSE`.
