# tiny-chess-01

A 4 KB Python chess engine built on sunfish's MTD-bi search with a hard cap of 15000 nodes per move, written for the make.fun tiny-chess-01 bounty. Because the search is deterministic and node-capped rather than time-capped, the same position always explores the same tree, so recorded games replay byte-identically on any machine.

## Engine

- MTD-bi drives a sequence of null-window alpha-beta probes, converging on the true score from above and below while a transposition table caches each probe's bounds so repeated positions cost nothing.
- Move ordering feeds futility pruning to skip hopeless quiet moves near the leaves, late-move reductions to search unpromising moves shallower, and null-move pruning to cut whole branches when passing the turn still beats beta.
- Piece-square tables shift between middlegame and endgame phases, so the king stops hiding in the corner and starts marching toward the center to support passed pawns once material thins out.
