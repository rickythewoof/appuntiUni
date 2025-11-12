a noi ha chiesto:
- cos'è la V-function
- ⁠cos'è la Q-function
- ⁠come sono legate le due equazioni
- ⁠cos'è un ambiente stocastico
- ⁠cosa cambia se applico una formula deterministica ad un ambiente non deterministico
- ⁠differenza principale tra Q-learning e DQN
## V-Function
La V-Function is one that maps a state, and the policy, to the cumulative reward $S \times \pi \rightarrow R$, where S is a given state to start with, $\pi$ is the policy, and $R$ is al of the collected reward to go from $s$ up until one of the ending states. This can be used in the case in which we know the reward function and we know that actions produce deterministic effects.

## Q-Function
The Q-Function is a 2-dimensional array $S \times A \rightarrow R$ which is useful when you don't know the reward function, and for this reason you need to keep track of what is the most high-yielding action for any given state. The Q-Function can be updated in various ways:
- $Q(s,a) = Q(s,a) - \alpha (r + \gamma * \max_a Q(s', a') - Q(s,a))$  \[Non-deterministic, our case since we don't know how the other ]
- $Q(s,a) = r(s,a) + \gamma \max_{a^\prime} Q(\delta(s, a), a^\prime)$ \[Deterministic]
Is used to represent the expected reward on executing an action given a state.
### How are these two things related?
the V-function can be used only if we already have a policy, and for that reason we already know all of the reward and the state-action, since $V^\star$ is known, and the optimal policy will be $\pi^\star = argmax_{a \in A} = r(s,a) + \gamma V^\star(\delta(s,a))$ .
If we don't know the rewards we can just "probe" for everything, and at that point $\pi^\star = argmax_{a \in A} Q(s,a)$
### What happens if I apply a deterministic formula into a nondeterministic case?
just theoretical questions, how to apply theory to practice. It doesn't work, because in nondeterministic scenarios we don't know what's the state that we get in if we apply an action over a state. This means that we will not converge.
### Q-Learning and DQL
The main differences in how they work is based on the fact that in Q-learning, to know the best strategy, we need to try every single state-action tuple, and in the case of non-deterministic also we need to try it multiple times. This, especially in big models, makes the learning exponentially more time-consuming. The idea on DQL is to apply deep learning technology to _learn_ the Q-table by observing its behaviour, and do some "bets" on it.