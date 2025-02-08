# Exercise Week 9
## Ex 1
I can model this as an integer programming problem.

will consider $x_{i,j}$ as $1$ if agent $i$ chose strategy $j$, with $j \in \{1,2,3\}$, and we will put constraints over the fact that only one can be chosen (1) $x_{i,1}+x_{i,2}+x_{i,3} \ge 1$, and $x_{i,j} \in \{0,1\}$.
We'll now also model $L_e(\sigma)$ as $\sum_{i \in I: e\in E(i,1)} x_{i,1}w_i + \sum_{i \in I: e\in E(i,2)} x_{i,2}w_i + \sum_{i \in I: e\in E(i,3)} x_{i,3}w_i\ \ \forall e \in E$ and since we want to minimize the maximum, this will need to be $\ge z$.
now we can just minimize z and we should be done with the modelling.
Given that this is an integer programming, we'll resolve the much simple linear relaxation problem, remembering that $z_{LP} \le z_{OPT}$ .
Resolving the linear relaxation problem will give us an optimal value of z, and so an optimal value for all $x^*_{i,j} \in [0,1]$ that is not a valid solution for our integer programming problem.
We'll then adapt it by setting, for every  $x^*_{i,j}$, the relative $x_{i,j}$ of the $IP$ as 1 if and only if $x^*_{i,j} = \max \{x^*_{i,1},x^*_{i,2},x^*_{i,3}\}$. This will guarantee that the solution to the problem is a valid one, since for (1) there will be at least one $\ge 1/3$ that will be selected.
This means that $L^*_e(\sigma) \ge 1/3 L^S_e(\sigma)$ (with $S$ being the result derived from our greedy solution)
We can conclude then by saying $z_{GREEDY} \le 3 z^* \ge 3z_{OPT}$ 
## Ex 2
### i.
We can, for every vertex $v \in V$, randomly choose where to position it between the set $S$ and the set $V-S$. Given that we are considering directed cuts, we have that $Pr("e=(u,v)\ crosses\ the\ cut") = Pr(u \in S)Pr(v \in V-S) = \frac12 \frac12 = \frac14$  
### ii.
The best way to "prove" that this algorithm models the problem is by explaining it bit by bit. The first is that we are handling a maximization problem on $w_{ij}z_{ij}$. We hypothesize for now that $z_{ij}$ probably models the fact that it gets set to $1$ if and only if the edge $e=(i,j)$ crosses the cut.
We have now a tuple of constraints. $\forall (i,j) \in A$, $z_{ij} \le x_i$, which tells us that for the edge to be considered selected, the node $i$ _must_ be on the set $S$. The other one basically tells us the same thing, but for the node $j$ and for the fact that it _must not_ be on the set $S$. At that point we have integrality constraint on $x_i$ and value constraints on $z_{ij}$.
### iii.
Smartly proven, uses both probability and function analysis to check if a function is always positive.
$Pr(i \in S; j \in V_S) = (\frac14 + \frac{x_i^*}2)(\frac34 + \frac{x_i^*}2) \ge (\frac14 +\frac{x_i^*}2)^2$ 
and we want to prove that all of this is $\ge x_i^* / 2$ (which will directly take us to our solution $\frac{OPT}2$)

We'll need to study the function $(\frac14 +\frac{x_i^*}2)^2 -\frac{x_i^*}2$. Analyzing it shows us that the function is always non-negative, so we have proven that.
$E[\sum w_{ij}z_{ij}] = \sum w_{ij} E[z_{ij}] \ge \frac12 \sum w_{ij} \ge \frac{OPT}2$  