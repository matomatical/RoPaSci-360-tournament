COMP30024 Tournament 2021
=========================

Welcome to the class tournament for Project Part B of COMP30024 Artificial
Intelligence, semester 1, 2021.

### Tournament rules

This is a single-elimination tournament: In each round, players are randomly
matched and the winner of each match proceeds to the next round (the other
player is eliminated from the tournament).

Each match involves at least three games. If a winner is clear from the first
three games of the match, the match ends. If not, for example due to draws,
the match continues 'sudden death': one game at a time until either player
wins a game, breaking the draw.

When a player runs out of time, crashes, or submits an invalid move, the
player forfeits the game. The match continues and the player may still win
the match if they win the other two games without further errors.

### This repository

This README documents the matchups and results of each round of the
tournament, and the folders in this repository contain the game logs.

The game logs are numbered with the match number and then `.0`, `.1`, and
`.2` (one for each game of the first three).

The games in sudden death were executed manually and only the result was
recorded, no logs were kept. Most other game logs are available, but some
are missing. If you are looking for a missing log, raise an issue or email
Matt, who can help tell you about the game or try to run some similar
sample games for new logs (without changing the result). The game logs don't
always record if the game ended due to a runtime error or timeout. If the
log ends abruptly, this is probably the cause.

#### Replay program

Experimental: A python script to replay a game log is included.
It is intended for displaying the tournament results in the lecture.
It only works if the log is formatted perfectly (e.g. some issues with
custom types cause log parsing errors; you can try to 'clean' the log or
improve the parsing to display more logs if it's a problem for you).
It and requires the third-party Python library `console`.

```
usage: python -m replay <path to logfile>`
```

### Round 1

128 teams qualified for the tournament (a small number of additional teams
unfortunately did not qualify due to some runtime and timing errors, however
if this is you don't worry, we will still be able to benchmark your players
for the assessment, we just didn't have time to fix the problem before the
tournament).

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
1.01  | `No_0`                      |  `Pepin`                    | Upper
1.02  | `UrBrother_in_Law`          |  `placeholder_text`         | Upper
1.03  | `hxd`                       |  `Heuristic`                | Upper
1.04  | `dwayne_johnson`            |  `CedSam`                   | Upper
1.05  | `HomemadeIntelligent`       |  `LUCKY_LALAS`              | Lower
1.06  | `the_pink_coder`            |  `Future_Yoda`              | Lower
1.07  | `group_of_AIs`              |  `gloaming`                 | Upper
1.08  | `AlgorithmsAreFun`          |  `ass_to_grass`             | Lower
1.09  | `nitromelon`                |  `Billy_Louise`             | Upper
1.10  | `H1_GO`                     |  `PeppaPig`                 | Lower
1.11  | `m`                         |  `a_potato`                 | Upper
1.12  | `SEGMENTATION_FAULT_11`     |  `Stockfish9`               | Lower
1.13  | `XAEA_Xii`                  |  `Robots_2005`              | Upper
1.14  | `SneakPeek`                 |  `ApexPredator`             | Lower
1.15  | `eye_robot`                 |  `ROPASCI_KILLERS`          | Upper
1.16  | `SS_AI`                     |  `access_pending`           | Lower
1.17  | `ABCDE`                     |  `artificial_noob`          | Lower
1.18  | `elongated_muskrat`         |  `AlphaRPS`                 | Lower
1.19  | `Uuuuh`                     |  `fire_punch`               | Upper
1.20  | `ACCESS_GRANTED`            |  `liauw`                    | Upper
1.21  | `PotatoSalad`               |  `lulululululu`             | Upper
1.22  | `Pain_Peko`                 |  `daydayup`                 | Lower
1.23  | `__name__`                  |  `Noidea`                   | Upper
1.24  | `ElectricSheep`             |  `Horizon_Dawn`             | Upper
1.25  | `bender`                    |  `kill_bot_v4`              | Lower
1.26  | `Navi`                      |  `admin`                    | Lower
1.27  | `LMAO`                      |  `Beans`                    | Lower
1.28  | `grandMasters`              |  `revolverUpstairs`         | Lower
1.29  | `monke`                     |  `Just_a_couple_of_T800s`   | Lower
1.30  | `arizona`                   |  `GlobalElite`              | Upper
1.31  | `sfAUS`                     |  `cheesers`                 | Lower
1.32  | `cooked_pancakes`           |  `icu996`                   | Lower
1.33  | `WALL_E`                    |  `RTX3090`                  | Lower
1.34  | `invictus_gaming`           |  `Hornet`                   | Lower
1.35  | `Ti_Ming`                   |  `LoiGu`                    | Upper
1.36  | `chill_mates`               |  `updog`                    | Lower
1.37  | `luv`                       |  `neverland`                | Lower
1.38  | `googleme`                  |  `plastic_love`             | Upper
1.39  | `cornChips`                 |  `pez_pilot`                | Upper
1.40  | `Macrohard`                 |  `ACCESS_DENIED`            | Lower
1.41  | `artificially_unintelligent`|  `real_human_team`          | Upper
1.42  | `fingers_crossed`           |  `FiveYang`                 | Lower
1.43  | `massive_biscuit`           |  `on_my_block`              | Upper
1.44  | `Team_A_A`                  |  `Genius`                   | Lower
1.45  | `ROCK_PAPER_SCISSORS`       |  `aaabaaajss`               | Upper
1.46  | `Wombat`                    |  `wheatley`                 | Lower
1.47  | `T_30024`                   |  `DOMINATORS`               | Upper
1.48  | `WandaVision`               |  `RoPaSci_2077`             | Upper
1.49  | `teamMS`                    |  `cybermancer`              | Upper
1.50  | `CouchNCouchess`            |  `Noobs`                    | Lower
1.51  | `A_Team`                    |  `ninecommas`               | Upper
1.52  | `Double_sky`                |  `_pythonbois`              | Upper
1.53  | `DiscoJanet`                |  `Amateurs`                 | Lower
1.54  | `ChumBucket`                |  `Botted`                   | Upper
1.55  | `Anonymous`                 |  `California`               | Upper
1.56  | `Group233`                  |  `DOMINATORS`               | Upper
1.57  | `goToHornyJailDoNotPassGoDoNotCollect200`  |  `Dido`      | Upper
1.58  | `RussiAnBot137_`            |  `HAL_9000`                 | Lower
1.59  | `ADDITIONAL_PYLON`          |  `QuanyingLyu`              | Lower
1.60  | `Spartans`                  |  `TBD`                      | Lower
1.61  | `x3u6tt`                    |  `Tronity`                  | Lower
1.62  | `Druids`                    |  `StockFish_Players`        | Lower
1.63  | `NeverMindSomeLosers`       |  `rock_paper_scissors`      | Upper
1.64  | `alienware`                 |  `wambusters`               | Upper

### Round 2

64 first-round winners proceeded to the second round.

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
2.01  | `No_0`                      | `UrBrother_in_Law`          | Lower
2.02  | `hxd`                       | `dwayne_johnson`            | Lower
2.03  | `LUCKY_LALAS`               | `Future_Yoda`               | Lower
2.04  | `group_of_AIs`              | `ass_to_grass`              | Lower
2.05  | `nitromelon`                | `PeppaPig`                  | Upper
2.06  | `m`                         | `Stockfish9`                | Upper
2.07  | `XAEA_Xii`                  | `ApexPredator`              | Lower
2.08  | `eye_robot`                 | `access_pending`            | Upper
2.09  | `artificial_noob`           | `AlphaRPS`                  | Lower
2.10  | `Uuuuh`                     | `ACCESS_GRANTED`            | Upper
2.11  | `PotatoSalad`               | `daydayup`                  | Upper
2.12  | `__name__`                  | `ElectricSheep`             | Lower
2.13  | `kill_bot_v4`               | `admin`                     | Lower
2.14  | `Beans`                     | `revolverUpstairs`          | Upper
2.15  | `Just_a_couple_of_T800s`    | `arizona`                   | Upper
2.16  | `cheesers`                  | `icu996`                    | Lower
2.17  | `RTX3090`                   | `Hornet`                    | Lower
2.18  | `Ti_Ming`                   | `updog`                     | Upper
2.19  | `neverland`                 | `googleme`                  | Lower
2.20  | `cornChips`                 | `ACCESS_DENIED`             | Upper
2.21  | `artificially_unintelligent`| `FiveYang`                  | Lower
2.22  | `massive_biscuit`           | `Genius`                    | Lower
2.23  | `ROCK_PAPER_SCISSORS`       | `wheatley`                  | Lower
2.24  | `T_30024`                   | `WandaVision`               | Lower
2.25  | `teamMS`                    | `Noobs`                     | Lower
2.26  | `A_Team`                    | `_pythonbois`               | Upper
2.27  | `Amateurs`                  | `ChumBucket`                | Lower
2.28  | `Anonymous`                 | `Group233`                  | Lower
2.29  | `goToHornyJailDoNotPassGoDoNotCollect200` | `HAL_9000`    | Lower
2.30  | `QuanyingLyu`               | `TBD`                       | Lower
2.31  | `Tronity`                   | `StockFish_Players`         | Lower
2.32  | `NeverMindSomeLosers`       | `alienware`                 | Upper

### Round 3

32 second-round winners advanced to the third round.
The tournament is heating up!

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
3.01  | `No_0`                      | `dwayne_johnson`            | Upper
3.02  | `Future_Yoda`               | `ass_to_grass`              | Upper
3.03  | `nitromelon`                | `m`                         | Upper
3.04  | `ApexPredator`              | `eye_robot`                 | Lower
3.05  | `AlphaRPS`                  | `Uuuuh`                     | Upper
3.06  | `PotatoSalad`               | `ElectricSheep`             | Lower
3.07  | `admin`                     | `Beans`                     | Lower
3.08  | `Just_a_couple_of_T800s`    | `icu996`                    | Lower
3.09  | `Hornet`                    | `Ti_Ming`                   | Lower
3.10  | `googleme`                  | `cornChips`                 | Upper
3.11  | `FiveYang`                  | `Genius`                    | Upper
3.12  | `wheatley`                  | `WandaVision`               | Upper
3.13  | `Noobs`                     | `A_Team`                    | Lower
3.14  | `ChumBucket`                | `Group233`                  | Upper
3.15  | `HAL_9000`                  | `TBD`                       | Upper
3.16  | `StockFish_Players`         | `NeverMindSomeLosers`       | Lower


### Round 4

16 third-round winners advanced to the fourth round.

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
4.01  | `No_0`                      | `Future_Yoda`               | Lower
4.02  | `nitromelon`                | `eye_robot`                 | Lower
4.03  | `AlphaRPS`                  | `ElectricSheep`             | Upper
4.04  | `Beans`                     | `icu996`                    | Upper
4.05  | `Ti_Ming`                   | `googleme`                  | Lower
4.06  | `FiveYang`                  | `wheatley`                  | Upper
4.07  | `A_Team`                    | `ChumBucket`                | Upper
4.08  | `HAL_9000`                  | `NeverMindSomeLosers`       | Upper


### Round 5: Quarter-final

Eight winners from the fourth round advanced to the quarter final.

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
5.01  | `Future_Yoda`               | `eye_robot`                 | Lower
5.02  | `AlphaRPS`                  | `Beans`                     | Upper
5.03  | `googleme`                  | `FiveYang`                  | Lower
5.04  | `A_Team`                    | `HAL_9000`                  | Upper


### Round 6: Semi-final

The winners from the quarter-final advance to the semi-final. Only four
teams remain. Which two will advance to the final round?
The results of the semi-final round will be revealed on Thursday morning.

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
6.01  | `eye_robot`                 | `AlphaRPS`                  | Lower
6.02  | `FiveYang`                  | `A_Team`                    | Upper

### Round 7: Final match

Cogratulations `AlphaRPS` and `FiveYang` for making it to the final round.

Match | Upper team                  | Lower team                  | Winner
------|-----------------------------|-----------------------------|-------
7.01  | `AlphaRPS`                  | `FiveYang`                  | Lower

After three decisive victories in the final match, `FiveYang` defeated
`AlphaRPS` and was crowned the *RoPaSci 360* ***champion***!

Congratulations `FiveYang`!

