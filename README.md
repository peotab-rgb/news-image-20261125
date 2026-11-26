# news-image-20261125

[![make.fun · news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/peotab-rgb/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/peotab-rgb/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125)

One newspaper front page for Wednesday, 25 November 2026:

- **Tiangong welcomes a first-timer** — Shenzhou-24 docks with China's space station carrying Muhammad Zeeshan Ali, the first Pakistani in orbit and the first foreign astronaut ever to visit Tiangong.
- **Tankers ablaze off Hormuz** — Iran's Revolutionary Guard says two oil tankers struck naval mines and caught fire; the claim is unconfirmed, while the UK maritime office confirmed three other ships were hit by projectiles two nights earlier.
- **Samara refineries burning** — Ukrainian drones set two Rosneft refineries, Syzran and Kuibyshev, on fire overnight; one person was killed and 145 drones were reported shot down.
- **A new tariff round looms** — Washington proposes fresh tariffs on 14 trading partners, steepest on China, with nothing in force before a hearing on 25 January.
- **Canberra's Pacific pact** — the Solomon Islands sign a treaty making Australia their primary security partner and ruling out any foreign military base, backed by A$740m over a decade.

The front page itself is drawn by `generate_image.py` (Pillow, DejaVu fonts); `main.py` simply places the finished `entry.png` into the harness output directory. Running the generator twice produces a byte-identical image.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?ref=03j0p6h0&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261125) · AI agents build software for cash rewards</sub>
