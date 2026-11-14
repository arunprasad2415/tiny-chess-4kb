# tiny-chess-4kb

A 3.4 KB Python chess engine for the make.fun tiny-chess-01 bounty.

main.py is a bootstrap: it holds the engine source as an lzma payload and execs it,
the same packing the house baseline entry uses, so the readable engine is about 12 KB
but only its compressed bytes count against the 4,096-byte cap.

The engine talks to the trial env over HTTP (POST /game, POST /move) and stops when
the env answers status "done". Deterministic: no clock and no randomness in the
search, so the same position always gets the same move.

Search: iterative deepening negamax with alpha-beta, a transposition table keyed by
Zobrist, killer moves and MVV-LVA ordering, and a capture-and-promotion quiescence
search. Evaluation: material (pawn 100, knight 320, bishop 330, rook 500, queen 900)
plus standard piece-square tables mirrored for black.

Every move it sends is checked against the env's own legal_moves, and a promotion the
env lists only with its piece letter is sent as ...q.
