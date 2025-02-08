# Exercise Week 7
## Ex 1
1. This is a 2-Approximation what works pretty similarly to the LoadBalancing problem we had, somehow. We'll consider an important upper bound on the solution, which is $w(E) = \sum_{e \in E} w(e) \ge OPT$. From there, we will consider the last iteration, in which we have just assigned the node $v_n$ to $S$ or $\bar{S}$. Without loss of generality, we say that we have assigned it to $S$, and this means that $w(S) \ge w(\bar{S})$. Since it's the last iteration, and we know that the two sets are disjoint, we can calculate that $w(S) \ge \frac{w(E)}2$ (considering the worst case in which they are both the same this makes sense). This means that: $GREEDY=w(S) \ge \frac{w(E)}2 \ge \frac{OPT}2$. This concludes our proof
2. Dunno, too tired to find this out, but I'm pretty sure proof works very similarly
## Ex 2
1. This algorithm is not optimal, and we can see this by simply doing an example
we have as a bound B = k

|       | $s_i$ | $v_i$ |
| ----- | ----- | ----- |
| $a_1$ | 1     | 1     |
| $a_2$ | 2k    | k     |
1. fractional knapsack problem is in P, as is the Linear Programming. We can prove its optimality with contradiction
	1. Considering that we are taking items in order of densities, we are maximizing per step unit the value we are adding and the weight capacity we are loosing.
	2. We are then getting until iteration $i$ and we are taking a fraction of $i+1$. Let's assume by contradiction that $v(S) < v(OPT)$. This means that the optimum has selected more items , but this is impossible since if it didn't get any of the fractional $i+1$ but more of the rest it couldn't get a high enough value to beat $S$ without also exceeding the weight limit. so $OPT$ chooses also the most fraction it can take of $i+1$.
## Ex 3
We can achieve a 2-approximation algorithm for it by randomly choosing an edge, considering it in the vertex cover, and removing all edges incident to the nodes connected to the edge chosen; this will be repeated until there aren't any more edges to select. (missing proof)

Another algorithm which gets a worse $\log n$ approximation is by selecting nodes at random and removing all incident edges. This can be proven to be $\log n$ since it's close to how a set cover works.