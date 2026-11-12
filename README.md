# tiny-chess-4kb

A 3.6 KB Python chess engine for the make.fun tiny-chess-01 bounty.
It talks to the trial env over HTTP: POST /game, POST /move.

Search: alpha-beta to depth 3 with a capture-first ordering and a material
plus centre evaluation. Deterministic, no clock in the search.
