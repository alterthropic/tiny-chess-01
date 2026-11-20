# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/alterthropic/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/alterthropic/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 3,162 bytes of Python 3.13, standard library only, packed as an lzma payload with its unpacker. It decodes the FEN the env serves, generates moves, and plays alpha-beta with iterative deepening, a quiescence search on captures, piece-square evaluation, a history heuristic and an endgame term that drives a lone king to the edge, to a fixed node budget so it is deterministic and never reads a clock.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8917 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=snmxezy4&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
