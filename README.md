# tiny-chess-01

A 4 KB Python chess engine: sunfish MTD-bi search, 15000-node cap, king-safety and endgame-aware evaluation. Built for make.fun's tiny-chess-01 bounty.

## Engine

- Iterative-deepening MTD-bi with null-window probes and a transposition table.
- Futility pruning, late-move reductions, null-move pruning, history repetition detection.
- Tapered king endgame table; deterministic node-capped search for byte-identical replay.