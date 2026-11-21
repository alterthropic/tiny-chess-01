# Thimble: A Chess Engine That Fits in a Postcard

Thimble is a deterministic chess engine built around MTD-bi, squeezed into fewer than four kilobytes of Python. Instead of trusting a wall clock, every search spends a fixed budget of visited nodes, so the same position always yields the same move on any machine, at any speed. The driver repeatedly probes the tree with zero-width alpha-beta windows, nudging its guess up or down until the bounds meet on the exact minimax score. A compact transposition table remembers previously judged positions, iterative deepening feeds each pass a better starting guess, and the whole thing stays small enough to read in one sitting while still playing a genuinely stubborn game.

## How the Search Earns Its Nodes

- **Null-window bisection:** every probe asks a yes/no question — is the score above this bound? — with alpha and beta one unit apart, so each search fails fast and the driver halves the remaining interval until a single value survives.
- **Transposition tables:** reached positions are hashed and cached with their depth and bound type, letting move-order swaps and repeated lines reuse earlier verdicts instead of paying for them twice.
- **Pruning heuristics:** captures and killer moves are tried first to trigger early cutoffs, while shallow extensions and futility-style skips trim branches unlikely to change the bound, stretching the fixed node budget further down the tree.