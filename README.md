# MCTS
Monte Carlo Tree Search on board game

### UCB1 in Multi-armed Bandit Problem:
construct statistical cobnfidence intervals for each machine
$$ \bar{x}_i \pm \sqrt{\frac{2\ln n}{n_i}}$$
where
* $\bar{x}_i$ : the mean payout for machine $i$
* $n_i$ : the number of plays of machine $i$
* $n$ : the total number of plays

**Strategy**: pick the machine with the highest upper bound each time. <br>
**Regret**: The regret grows only as $O(\ln n)$

### UCT (upper confidence tree):
Idea: Any given board position can be considered a multi-armed bandit problem, if statisitics are available for all of the positions that are only one move away.

* phase 1: **Selection**, for each move, choose by the UCB1 algorithm instead of randomly.
* phase 2: **Expansion**, for position with no record, randomly choose one child position.
* phase 3: **Simulation**, Monte Carlo simulation, pure random or with some simple heuristics, or using a heavy/light playout.
* phase 4: **Update**, or called *back-propagation* phase. This occurs whrn playout reaches the end of the game.

