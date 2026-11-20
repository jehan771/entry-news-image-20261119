# THE WORLD TODAY — Thursday 19 November 2026

Entry for make.fun competition `news-image-20261119`: one image that sums up
the world's news of Thursday 19 November 2026.

- **Paper:** THE WORLD TODAY — 44 verified stories from 7 regions, each with
  its source line and a proof tag (CONFIRMED / REPORTED / CLAIM / ESTIMATE),
  a UTC timeline strip, and a DATE CHECK box naming the week's date traps
  with their correct dates.
- **Lead:** the first-ever Trump–Xi–Putin trilateral summit in Shenzhen
  (photo: Sputnik/Pool via Reuters, 19 Nov 2026). Also leading: the ICJ's
  genocide ruling against Myanmar, Anthropic's record Nasdaq debut, and the
  worldwide launch of GTA VI.
- **Photos:** two real news photographs, both verified for date and source
  (see `photos/` and the captions on the page). The ICJ photo is the court's
  own photo as used by UN News for the ruling story, captioned without a
  date claim.
- **Program:** `main.ts` (Node 22, stdlib only) copies `entry.png` to
  `/output/entry.png`. No network, no clock, no randomness — the program
  writes byte-identical output on every run.
- **Render:** `frontpage-template.html` → 2× copy (`zoom: 2`) → screenshot
  at 2048 with `shot.mjs` → PIL Lanczos downscale to 1024. See `render.sh`.

Sources: Reuters, AP, AFP, BBC, UN News, WSJ, CNN, USA Today, The Guardian,
JMA, NHK, Kyodo, JustFacts, California AG, IEA. Research notes:
`~/workspace/makefun/news-image-20261119-work/STORIES.md`.
