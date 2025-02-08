# Exercise Week 3
## Ex 1
What the fuck is it asking???? I swear to fucking god
## Ex 2
- (a) We'll first give the OPT formulation of the algorithm.
	- if $i = 0\ or\ j= 0: OPT(i,j) = 0$ 
	- else if $A[i] == B[j]: OPT(i, j) = 1+OPT(i-1,j-1)$
	- else $OPT(i, j) = \max\{OPT(i-1, j), OPT(i, j-1)\}$
- (b) The algorithm chooses between three possible choices:
	- it matches two letters together, and decreases the iterator by one on both strings
	- it doesn't match two letters, and continues the search by iterating search on X-1 and Y and on X, Y-1
	since the algorithm assigns a point only if it matches two character together, it will not match them again and it's construction is correct.
- (c) To prove optimality we can put ourselves in a specific iteration on our algorithm, in which $M[i][j] = OPT[i][j]$, for a given $\le i,j$. Let's assume that it diverges in this iteration in a better way. This means that it has two letter matched. If this is the case, our algorithm would've done so too, since it calculates the max between matching and not.
	- Other proof consists on analyzing the problem on its inductive steps. If we assume OPT(k,l) is true, we calculate that for $i = k+1$, and $j = l+1$. If $a[i] = b[j]$ then we'll increase by one + OPT(k,l) which is optimal, otherwise we'll find the one that excludes $a[i]$ or $b[j]$
## Ex 3
We'll calculate the optimal value by defining $OPT(i)$ the value of the longest common sub-sequence on the string $x_0, x_1, ..., x_i$. Once we did that we can create the iterative steps
- if $i = 0 : OPT(i) = 0$
- else $OPT(i) = 1 + \max_{0<j<i}\{if(x_j < x_i):OPT(j)\}$
## Ex 4
Will need to try and better understand Bellman-Ford.
