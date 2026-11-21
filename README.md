# tiny-chess-01

A 4 KB Python chess engine built for the make.fun tiny-chess-01 bounty. It plays legal, reasonably strong chess within a tiny byte budget by leaning on the sunfish design: compact board representation, move generation folded into scoring, and an MTD-bi search bounded at 15000 nodes per move so games stay fast and fully reproducible.

## Engine

- Iterative-deepening MTD-bi search: repeated null-window probes around a score guess converge on the exact minimax value, with a transposition table carrying bounds and best moves between iterations.
- Aggressive cutoffs keep the tree small: futility pruning skips hopeless quiet moves near the leaves, late-move reductions search unpromising moves shallower, and null-move pruning lets the opponent move twice to prove a position is too good to bother with.
- Search is deterministic and capped at 15000 nodes per move, so the same position always yields the same move — games replay byte-identically.