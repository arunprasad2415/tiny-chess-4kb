# tiny-chess-4kb

A 3.8 KB Python chess engine for the make.fun tiny-chess-01 bounty.

It talks to the trial env over HTTP: POST /game, POST /move, and stops when the
env answers status "done". Deterministic: no clock and no randomness anywhere
in the search, so the same position always gets the same move.

Search: negamax with alpha-beta to two plies from the root, then a
capture-only quiescence search one ply deeper, moves ordered by victim value.
Evaluation: material (pawn 100, knight 320, bishop 330, rook 500, queen 900)
plus a centrality term weighted per piece, negative for the king.

Two habits keep it out of the env's 4xx refusals: every move it sends is
checked against the env's own legal_moves, and a promotion that the env lists
only with its piece letter is sent as ...q.
