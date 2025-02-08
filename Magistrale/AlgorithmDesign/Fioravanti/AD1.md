# Exercise Week 1
## Ex 1
given set of stops $S=\{s_1, s_2, .., s_m\}$ and given amount of $n$ kms he needs to drive, give efficient algorithm to determine when he should stop
```
remaining = n
drove = 0
i = 0
stops = 0
while(!arrived(drove))
	if remaining-(drove-s[i]) > n
		remaining = remaining -(drove-s[i])
	else
		stops +=1
		remaining = n
	i=i+1
```
- (b) This algorithm yields an optimal solution. We can prove this by considering a possible OPT solution, which will be the same until a certain point, which will be better than our. Let's consider the iteration i, in which the number of stops is the same, and so its remaining driving time; if the optimum does one less stop than us then it mean it can reach a station, but if it could then our algorithm would've done so.
- (c) since we are still visiting all of the stations, and the number of iterations depends on i, our algorithm has a computational cost of $O(m)$, where $m$ is the number of stops
## Ex 2
- (a) The algorithm described in the lower part is optimal. We can demonstrate this by induction
	- *base case*: we know this is optimal because for change = 0 algorithm return 0
	- *inductive part*: We can create proof that, greedy solves optimally for value of change $x: c_{k-1} \le x < c_k$. We know that an optimal value must use less coins, and so not use $c_{k-1}$, but we know this is not possible for tables.
	- We can show that finding the problem for $x \longleftarrow x - c_k$ which we know optimal for tables. 
```
S = [0]^4 # Initialize array of 4 elements
change = N
i = 3
coins = [1,5,10,25]
while change > 0
	if change - coins[i] > 0
		change -= coins[i]
	else
		i-=1
```
- (b) This doesn't work for $x=14$ and coin denomination $coins = [1,7,10]$
- (c) We can create a dynamic programming algorithm that works with two variables.
	- $OPT(n, k)$ which is the optimal number of coin changes given $n$ and coin denominators $c_1, ..., c_k$.
	- if $n=0 \Rightarrow OPT(n,k)=0$
	- if $n < c_k \Rightarrow OPT(n,k) = OPT(n, k-1)$
	- else $OPT(n,k) = \max \{OPT(n-c_k, k), OPT(n, k-1)\}$
## Ex 3
- (a)This can be proven by contradiction. Suppose there are two MST's $T$ and $T\prime$, and since they are different they will have an edge $e=(u,v)$ that's different between one another. Let's assume that $e$ has the minimum weight of difference, and $e \in T$ and $e \notin T\prime$. Since MST are maximally acyclic, we can add $e$ in $T\prime$ and create a cycle. Since we added the smallest edge that has the difference, we'll then create a cycle in which there is also $f$ different, but also that $w_e < w_f$.
	Removing w_f would make it still a MST, since $T = T\prime\prime$, but also that now this shows that the weight of $T\prime$ was bigger than $T$, which concludes the proof.
- (b) We can create a subgraph where we have only edges in which weight is strictly less than $w_e$ and then run a connectivity check. If the subgraph is strongly connected, then $e$ isn't part of the MST, otherwise it is.
# Ex 4
- (a)(b) Given that this time we have $T$, if we add $e'=(u,w)$ we'll then create a cycle. Since we didn't add $e\prime$ to $T$ we'll use T to find the path in the MST from $u$ to $w$, which we know exists. If we see that $w_{e\prime}$ is larger than any edge in the path, than we know $e\prime$ doesn't belong in any MST. Otherwise it will, since now there will be a maximum edge $e \neq e\prime$ which will be removed from the cycle.  
