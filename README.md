# tiny-chess-4kb

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/arunprasad2415/tiny-chess-4kb/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/arunprasad2415/tiny-chess-4kb/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A deterministic chess engine for make.fun's tiny-chess-01 bounty, packed into the
4,096-byte entrypoint. It plays a full negamax search with alpha-beta, iterative
deepening, a Zobrist transposition table, killer moves, MVV-LVA capture ordering,
quiescence search and piece-square evaluation, and talks to the trial env over HTTP.

## Run it

```sh
MAKEFUN_ENV_URL=<the trial env url> python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=6erpjdnf&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
