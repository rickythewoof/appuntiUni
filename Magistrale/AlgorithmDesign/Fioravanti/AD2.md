# Exercise Week 2
## Ex 1
- (a) We can create a dynamic programming algorithm that works with two variables.
	- $OPT(n, k)$ which is the optimal number of coin changes given $n$ and coin denominators $c_1, ..., c_k$.
	- if $n=0 \Rightarrow OPT(n,k)=0$
	- if $n < c_k \Rightarrow OPT(n,k) = OPT(n, k-1)$
	- else $OPT(n,k) = \min \{1 + OPT(n-c_k, k), OPT(n, k-1)\}$
To efficiently implement this we'll store the values of OPT into a 2D-array
```
M[n][k] # array of opt values
M[0][k] = 0 # for every denomination
M[n][0] = undef
for i=1, ..., n
	for j = 1, ..., k
		if n < c_j
			M[i][j] = M[i][j-1]
		else
			m[i][j] = min{1+M[n-c_j][j], M[i,j-1]}
```

After calculating this we'll just search for the table in position $M[n][k]$ which will return the minimal number of coin changes needed
## Ex 2
- (a) We may need to create a max independent set of this, and for this reason we'll create a possible Greedy strategy
```
sort_by_weight(V)
sol = {}
for every v in V
	if v compatible sol
		add v
return sol
```
- this doesn't work in the simple case of $ [v_1 = 100] - [v_2 = 101] - [v_3 = 2], as Greedy takes solution {$v_2$}, but it's incorrect since $OPT = \{v_1, v_3\}$
- (b) 
- (c) we can create a dynamic programming algorithm that works in two major steps
```
M[n] # solutions
M[0] = 0
M[1] = v_1
i = 2
while i <= n
	M[i] = max{v_i + M[i-2], M[i-1]}
```
then we'll create our actual solution
```
S = emptyset
i = n
while i > 0
	if M[i] > M[i-1]
		S.append(v_i)
		i=i-2
	else 
		i = i-1
```
Given we are linearly iterating on $M$, and $|M| = n$, the asymptotic time and space is $O(n)$.
## Ex 3
- This rod cutting problem is similar to the knapsack problem, in which we have as weight the length $l$ remaining, and the values the value of the cut.
- Creating such problem becomes easily a problem of $OPT(i, w) = \max\{v_i+OPT(i, w-w_i), OPT(i-1, w\}$, or just $OPT(i,w) = OPT(i-1, w)$ if $w<w_i$
- (b) here bottom-up implementation
```
compute_OPT(M, i, j)
	if M not empty
		return M[i][j]
	else
		if i = 0
			return 0
		else if j < w_i
			M[i][j] = Compute_OPT(M, i-1, j)
		else
			M[i][j] = max(v_i + Compute_OPT(M, i, j-w_i), Compute_OPT(M, i-1, j))
```

We can easily build our solution back Top-Down by
```
M = Compute_OPT(m, L, L)
remaining = L 
i = L
cut = {}
while remaining > 0
	if M[i][remaining] == v_i + M[i, remaining-w_i]
		cut = cut union {i}
		remaining = remaining-w_i
	else
		i = i - 1
return cut
```