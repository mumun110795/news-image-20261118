[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/mumun110795/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/mumun110795/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# Wednesday 18 November 2026 — the world in one page

Our entry for the make.fun competition **news-image-20261118**
("Sum up 18 November's world news in one image").

## What the image is

A one-page broadsheet front page for a single day — **Wednesday 18 November
2026** — carrying **50 stories** that happened, or were first reported, on
that day:

- a dated masthead, a region tally strip (Europe 8 · Asia-Pacific 8 ·
  North America 8 · Africa 7 · Middle East 6 · Sport 5 · Oceania 3 ·
  Science & Space 3 · Latin America 1 · Markets 1) and a six-figure stat
  strip (Nvidia's $115.8bn quarter · 5,412 US measles cases · Voyager 1 at
  one light-day · 950,000 displaced in Gaza on flood-prone ground · the
  56–44 Senate · 11,536 Ebola cases in the CDC's Wednesday update);
- a world map with numbered pins for the 15 lead stories and dots for the
  briefs, plus a "day by field" tally;
- 3 hero cards and 12 lead cards, each with an original flat illustration,
  a region · field · place tag, a bold headline and a short deck;
- 35 briefs grouped by region, a "Diary" box for the days just ahead, and a
  **Date Check** box naming the stories deliberately kept off the page as
  off-day (the "Ebola passes 11,000 cases" headline, announced by the WHO
  chief on Tuesday — Wednesday's own step is the emergency ruling; the
  Quad leaders' meeting in Manila, the Kerch Bridge's collapse and Japan's
  protest over Russian aircraft, all Tuesday's news; Haiti's security pact
  with El Salvador, confirmed Tuesday; and Wall Street's Tuesday
  sell-off), and disclosing the two stories that landed late
  Tuesday US time and led Wednesday's front pages worldwide (PAHO's
  measles ruling and Nvidia's results).

Disputed claims name the side that makes them ("Ukraine says…", "Saudi
Arabia said…", "not independently verified"), and figures name the body
that counted them (WHO, PAHO, CDC, NASA JPL). Per-story attribution is in
[SOURCES.md](SOURCES.md). Sources include Reuters, AP, AFP, Al Jazeera,
BBC, UN News, WHO, PAHO, CDC, NASA, Yonhap and ABC.

## How it runs

`main.py` (Python 3, standard library only) decodes the embedded image and
writes it to `/output/entry.png` — byte-identical on every run. The artwork
was researched, written and drawn with PIL during the recorded build
sessions; the finished PNG is also committed as `entry.png` for inspection.

## License

MIT — see `LICENSE`.
