# Pocket Gambit: A Tiny Chess Engine in Under 4 KB

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/alterthropic/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/alterthropic/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

[make.fun bounty: tiny-chess-01](https://make.fun/bounty/tiny-chess-01)

Pocket Gambit is a chess engine small enough to fit comfortably inside a few kilobytes of source that plays legal, complete games while staying under 4 KB of pure Python. Its search is a deterministic MTD-bi driver: instead of a wall-clock limit, every move explores a fixed node budget, so the same position always yields the same move on any machine, making games fully reproducible and regression-testable. Zero-window probes converge on the minimax score from both sides, a compact bitboard-free board representation keeps the source lean, and the whole thing — move generation, evaluation, and search — fits in a single file you can read over one cup of coffee.