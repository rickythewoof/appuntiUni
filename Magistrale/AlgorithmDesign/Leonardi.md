# Graphs
## Definition
A graph has the following notation: $G  = (V,E)$, where:
- V = set of Nodes, or Vertices
- E =  Set of Edges, or Arcs, between pairs of nodes
- we has as size $m = |E|$, $n=|V|$
### Path
A Path in an undirected graph $G=(V,E)$ is a sequence of nodes $v_1, v_2, ..., v_k$ with the property that each consecutive pair $v_{i-1}, v_i$ is joined by an edge $e\in E$.
A path is _simple_ if all nodes are distinct. An undirected graph is _connected_ if for every pair of nodes $u$ and $v$ there is a path between them
### Cycle
A cycle is a path $v_1, ..., v_k$ in which $v_1 = v_k$, $k> 2$ and the first $k-1$ nodes are distinct.
### Trees
An undirected graph is a tree if it is connected and doesn't contain a cycle.
**Th**: let G be an undirected graph on $n$ nodes. Any two statements imply the third:
- G is connected
- G doesn't contain a cycle
- G has $n-1$ edges
## Graph connectivity 
- $s-t$ connectivity problem: Given two nodes $s, t \in V$ is there a path between them?
- $s-t$ shortest path problem: Given two nodes $s,t\in V$ what is the length of the minimum path between them?
### BFS and DFS
They are both different methods to create a tree from a starting node $s$. They work in different ways:
- **Breadth-First Search**: before exploring the nodes in a lower level we explore all nodes in the level we're in.
- **Depth-First Search**: We try to explore the deepest level for a given node before searching to another node.
They both work in $O(n+m)$ time, but they are useful for different things. For example, BFS is useful to understand the concept of levels, which is the minimum number of "steps" to get from a node to another.
### Bipartite graphs
An undirected graph $G=(V,E)$ is bipartite if the nodes can be colored blue or white such that every edge has one white and one blue end. We can see some interesting properties with this:
- If a graph is bipartite, then it cannot contain an odd-length cycle, since it wouldn't be possible to 2-color it
- Let $G$ be the connected graph, and let $L_0, ..., L_k$ be the layers produced by BFS starting from node $s$, then only one holds:
	i.  No edge of G joins two nodes of the same layer, and $G$ is bipartite. (Every level can be colored with the same 2-color, and bipartite property holds).
	ii. An edge of $G$ joins two nodes in the same layer, and $G$ contains an odd-length cycle.
### Strong Connectivity
In the case of directed graph this has more sense. A graph is _strongly connected_ if any two pair of nodes is mutually reachable. Let $s\in V$ be any node, then $G$ is strongly connected iff every node is reachable from $s$, and $s$ is reachable from every node.
#### Algorithm:
- pick any node $s$
- run BFS in $G$
- run BFS in $G^{reverse}$
- return true iff all nodes reached in both BFS executions.
We can still group subsets of $G$ into strongly connected components.
### Directed Acyclic Graphs
A _DAG_ is a directed graph that contains no directed cycles.
A _topological order_ of a directed graph $G = (V,E)$ is an ordering of its nodes $v_1, v_2, ..., v_n$ such that for every edge $e=(v_i, v_j)$ we have $i,j$.
**Th**: given $G=(V,E)$, topological order <=> DAG.
# Greedy Algorithms
it's a family of algorithms in which we "go only in one direction", without looking back at our results. Once a path has been crossed it won't ever go back (useful definition for later with Dynamic Programming)
## Some algorithms
### Coin Changing problem
Goal: given the current currency denomination: 1, 5, 10, 25, 100, devise a method to pay amount to customer using fewest number of coins.
#### Cashier's algorithm
At each iteration add coin of the largest value that doesn't take us past the amount to be paid.
```
sort n coin denomination such that c_1 < c_2 < ... < c_n
S = set of coins selected
while x > 0
	k = largest coin denomination such that c_k <= x
	if no such k return "no solution"
	else
		x = x - c_k
		S = S = {k}
return S
```
This algorithm is **optimal** for this set of coin
**Pf** \[by induction on x]:
- Consider we have optimal way to change $c_k \le x < c_{k+1}$ greedy takes coin $k$.
- Any optimal solution must also take coin k
	-  If not, it needs enough coins of type $c_1, ..., c_k$ to add up to $x$
	- We can calculate all optimal solutions for tuple $k, c_k$
- Problem reduces to coin change $x - c_k$ cents, which by induction is optimally solved by cashier's algorithm.
This algorithm doesn't effectively work with every denomination!
ex: C = {1, 2, 5, 7}, x = 10
- OPT = 2, since 5+5
- GREEDY = 3, since 7+2+1
### Interval Scheduling
we are given a set J of jobs, $J = \{j_1, j_2,...,j_n\}$. Job $j_i$ starts at $s_i$ and finises at $f_i$. Two jobs are compatible if they don't overlap. Goal: Find the maximum subset of mutually-compatible jobs.
We may try lots of possible greedy templates, for example:
- Earliest start time
- Earliest finish time (*actually best*)
- Shortest interval
- Fewest conflicts
All of them are based on ordering the set of jobs using a pre-established method and then selecting compatible jobs until we finish the list. We can prove that the others aren't the optimal possibilities by finding a counter example. 
![[Pasted image 20250131120743.png]]
```
sort J set of jobs by finish time
A = set of selected jobs
for j = 1, ..., n
	if compatible(j, A)
		A = A + {j}
return A
```
Earliest-Finish-time-first is optimal.
**Pf** \[By contradiction]:
- Assume greediness is not optimal, but that algorithm is optimal for job 1, ..., r.
- We see that at step $r +1$ OPT is better. This means that at that we had a job that finished later than our choice, but  got us a better result. We can see that we have selected that, for earliest-finish-time-first.
### Interval Partitioning
We have a set of lectures. Lecture $j$ starts at $s_j$ and ends at $f_j$. 
Goal is to find minimum number of classroom such that all lectures are scheduled and no lecture collide for the same rooms.
At this way it could be more optimal to use earliest start time, which is the actual optimal solution.
![[Pasted image 20250131122342.png]]
```
Sort lectures by start time.
d = 0, number of classrooms allocated
for j = 1, ..., n
if lecture j is compatible with some classroom
	schedule lecture j in any such classroom
else
	allocate new classroom d + 1
	schedule j for that classroom
return schedule
```
Earliest start time is optimal, we "normalize" the depth of a set of open intervals, and we will consider that OPT(# of needed classroom) $\ge$ $depth$, giving ourselves a lower bound on the optimal value. 
- Let d be the number of classrooms that the algorithm allocates. Classroom d is opened because we scheduled a lecture $j$ incompatible with all other $d-1$ classrooms
- each of the $d$ lectures end after $s_j$, and since we sorted by start time all incompatibilities are caused by lectures that start no later than $s_j$.
- Thus we have $d$ lectures overlapping at time $s_j + \epsilon$. By lower bound, then GREEDY = $depth$ $\le$ OPT => GREEDY = OPT
### Lateness minimization
We have a single resource processing one job at a time. Job j requires $t_j$ units of processing time and its due at time $d_j$. if j starts at time $s_j$, it'll finish at time $f_j = s_j + t_j$. 
We'll calculate lateness as $ l_j =  max {0, $f_j-d_j}. And we'll schedule al jobs to minimize the maximum lateness $L = max_j l_j$.
Here too we have multiple possible ways: _shortest processing time_, _earliest due time_, _smallest slack_. We can see with counterexamples 
![[Pasted image 20250131125812.png]]
``` 
Sort jobs by earliest deadline
t = 0
for j = 1, ..., n
	Assing job j to interval [t, t+j]
	s_j = t, f_j = t + t_j
	t = t + t_j
return intervals [s_1, f_1], ..., [s_n, f_n]
```
We can arrive to the optimality of our solution by considering that an optimal solution doesn't have idle time, and our algorithm won't ever have idle time. We'll base our proof with _inversions_:
Given a schedule $S$, an inversion is a pair of jobs i, j such that i < j (with our ordering earliest deadline), but j scheduled before i. We claim that swapping two adjacent and inverted jobs reduces the number of inversions by one and doesn't increase lateness.
**Pf** \[By contradiction]:
- We'll define S* as our optimal schedule that has fewest number of inversion. We can assume it doesn't have idle time. If S* has no inversions, then S = S*
- if S* has an inversion, let $i-j$ be an adjacent inversion
- Swapping i and j:
	- Doesn't increase max lateness
	- Strictly decreases number of inversions
- This directly contradicts definition of S*.
## Greedy Algorithm Strategies
Given the proofs that we have seen here, we have 3 major strategies when it comes to proving optimality of greedy algorithms:
- **Greedy algorithm _stays ahead_**: We can show that after each step of the greedy alg. its solution is at least as good as the optimal solution.
- **Structural**: We may discover a "structural" bound that tells us that our solution must have at least/at most a certain value, and we show that our algorithm achieves exactly that value.
- **Exchange Argument**: Gradually transform any solution to the one found by the greedy algorithm without hurting its quality.
## For graphs 
### Shortest Path problems
Given a graph $G = (V,E)$, with edge lengths $l_e \ge 0$, source $s\in V$, destination $t \in V$, find the shortest s-t path.
#### Dijkstra's Algorithm
It's a greedy approach, that works if all edges have non-negative length. It consists of a kind-of mix between BFS and DFS:
- Initialize $S = \{s\}$, $d(s) = 0$
- Repeatedly choose unexplored node $v$ which minimizes:
$$
\pi (v) = min_{e = (u,v):u \in S} d(u) + l(e)
$$
- add $v$ to $s$, and set $d(v)$ = $\pi (v)$
We can apply some optimizations, for example by remembering $\pi (v)$ instead of always recomputing it, or applying a priority queue to directly sort the nods by shortest length.
This greedy algorithm offers the optimal solution
**Pf**: \[By induction]
- _Base case:_
	- we have $|v| = 1$, so $d(s) = 0$
- _Inductive step, assume true for $|S| = k \ge 1$_
	- let $v$ be next node added to $S$, and let $(u,v)$ be the final edge
	- The shortest s->u path plus $(u,v)$ is an s->v path of length $\pi (v)$.
	- Considering any s->v path P, we can see that it's no shorter than $\pi (v)$
	- let $(x,y)$ be the first edge in $P$ that leaves $S$, and let $P\prime$ the sub-path to $x$
	- $P$ is already too long as soon as it reaches $y$.
$$
l(P) \ge l(P\prime) + l(x,y) \ge d(x) + l(x,y) \ge \pi(y) \ge \pi(v)
$$
The idea of this proof is that given an S, if the algorithm chose an edge $(u,v)$, then there isn't any other path that can get to $v$ faster than the selected. In the case of only one direct hop through $(w, v)$ if the s.p. to $v$ got through $w$ then the algorithm would've selected it.
### Minimum Spanning Tree
**Def**: A _path_ is a sequence of edges which connect a sequence of nodes. A _cycle_ is a path with no repeated nodes or edges other than the starting and ending nodes. A _cut_ is a partition of the nodes into two non-empty subsets into $S$ and $V-S$. The _cutset_ of a cut $S$ is the set of edges with exactly one endpoint in $S$.
A cycle and a cutset always intersect in an even number of edges, given that a cycle is a closed loop the number of edges "entering" $S$ is the same of the edges "exiting".

**Proposition**: Let $T=(V,F)$ be a sub graph of $G=(V,E)$. The following are equivalent:
- T is a spanning tree of G
- T is acyclic and connected
- T is connected and has $n-1$ edges
- T is acyclic and has $n-1$ edges
- T is minimally connected
- T is maximally acyclic
- T has a unique simple path between pairs of nodes.
T is a minimum spanning tree if T is a spanning tree in which the sums of all the edge costs is minimized.
MST is NOT a shortest path, given just the fact that MST doesn't have a _starting node s_.

*Fundamental Cycle observation*: Adding any non-tree edge $e$ to a spanning tree T forms a unique cycle $C$, and deleting any edge $f \in C$ from $T \cup \{e\}$ results in another spanning tree. Now, if $c_f$ < $c_e$, then the original $T$ wasn't an MST.
_Fundamental Cutset observation_: Deleting any tree edge $f$ from a spanning tree $T$ partitions the nodes into two connected components. Let D be a cutset of one of the connected components. Adding any edge $e \in D$ to $T - {f}$ results in a new spanning tree. If $c_e < c_f$, then original T wasn't an MST.
#### Greedy Rule 
A working greedy rule to get a MST works by applying two rules:
- **Red Rule**:
	- Let $C$ be a cycle with no red edges
	- Select uncolored edge of $C$ of max weight and color it red
- **Blue Rule**:
	- Let $D$ be a cutset with no blue edges.
	- Select uncolored edge in $D$ of min weight and color it blue.
This can be optimal, but at this stage there is no deterministic algorithm to apply one rule over the other.
#### Prim's Algorithm
```
initialize S = any node s
for each v!=s d(v) = inf
for each v insert v with key d(v) into priority queue
while priority is non-empty:
	u = delete-min from priority queue
	for each edge (u,v) in E incident to u
	if d(v) > c(u,v)
		decrease-key of v to c(u,v) in priority queue
		d(v) = c(u,v)
```
This is a special case of red-blue rule, in which we apply only the blue rule, and the proof is _very similar_ to Dijkstra's algorithm.
#### Kruskal's Algorithm
This uses a particular data-structure called _union-find_, which consists of adding ascending-order edges unless it creates a cycle.
```
sort m edges by ascending weight
S = empty set
for each v in V: makeset(v)
for i = 1, ..., m
	(u,v) = e_i
	if find_set(u) != find_set(v)   # They don't belong in the same set,
		S = S + {e_i}               # so we don't create a cycle by adding
		union(u,v)                  # e_i to our solution.
return S
```
it's an MST, because it's still a special case of our greedy algorithm:
- Case 1: Removing edge $e$ doesn't disconnect graph (fundamental cycle)
	- We'll apply red rule to cycle $C$ formed by adding $e$ to existing path between two endpoints
- Case 2: Removing edge $e$ does disconnect graphs (Fundamental cutset)
	- Apply blue rule to cutset $D$ induced by either components
#### Boruvka's Algorithm
We apply the blue rule to cutset corresponding to each blue tree, applying this until we have no new tree. We choose the min edge as in Prim's algorithm, but while having multiple sub-trees. We can apply this algorithm if and only if all costs are distinct (i.e. it exists a single MST).
# Dynamic Programming
Dynamic programming breaks up a problem into a series of overlapping sub problems, and, differently from what a greedy algorithm would do, builds up a solution to larger and larger sub problems while "going back".
## Weighted Interval Scheduling
It's close to the greedy algorithm, but in this case every job has an associated weight $v_j$, our job is to find a subset of mutually compatible jobs with maximum possible weight. Now, our greedy algorithm wouldn't be useful, and also considering biggest-weight-first wouldn't either.
The "solution" consists on "trying out all possible solutions by applying or not applying" job j to our solution. We have two cases:
- OPT selects job j
	- We collect profit $v_j$ and we "discard" incompatible jobs {p(j) +1, p(j)+2, ...j-1}.
	- Must include optimal solution to problem consisting of remaining compatible  jobs 1, 2, ..., p(j)
- OPT doesn't select job j
	- We include the optimal solution to problem consisting of remaining compatible jobs 1, 2, ..., j-1
OPT(j) = {0 if j = 0}, { max{$v_j$ + OPT($p(j)$), OPT(j-1)} }
where p(j) is the next compatible job selecting j.

This is basically "trying out all possibilities", but it's inefficient since we calculate already calculated values n times!
the idea is to first calculate and store the "value" of our optimal solution, and with this "get back" to the actual optimal solution.
## Segmented Least Squares
Even tho we can, given n points in plane $(x_1, y_1), (x_2, y_2), ... , (x_n, y_n)$ , find a line $y=ax+b$ that minimizes the sum of squared errors.
$$
SSE = \sum_{i=1}^n({y_i-ax_i-b})^2
$$
we can calculate in time $O(1)$ using calculus.
We have in this case that we want to find a function $f(x)$ of sequence of lines such that we can balance Accuracy (goodness of fit) and Parsimony (Number of lines), and so minimize $f(x) = E + cL$, with E being sum of sums of squared errors in each segment, and L being the number of lines.
We compute OPT(j) by considering:
- Last segment uses points $p_i, p_{i+1}, ..., p_j$ for some i
- Cost = e(i,j) + c + OPT(i-1)

if j = 0 -> $OPT(0) = 0$
else -> $OPT(j) = min_{1\le i \le j}\{e(i, j) + c + OPT(i-1)\}$
## Knapsack problem
We have a typical problem of the integer programming family.
Given $n$ objects, with every item $i$ having a weight $w_i > 0$ and a value $v_i > 0$, and a "knapsack" that has a maximum capacity of $W$, our goal is to fill the knapsack so as to maximize total value without overflowing the weight limit.
There are no greedy algorithms that can optimally resolve this!
#### A False start
We'll define our $OPT(i)$ as the max profit given subsets of items $1, ..., i$.
- Case 1. Opt doesn't select item i
	- We'll select best between subset $1, ..., i-1$
- Case 2. OPT selects item i
	- This doesn't immediately imply that we need to reject other items, we need more information about items selected before!
#### Adding new variable
We'll redefine our $OPT(i, w)$ , which is the max profit subset of items $1, ..., i$ and weight limit $w$.
- Case 1. Opt doesn't select item i
	- We'll select best between subset $1, ..., i-1$ and unchanged weight limit $w$
- Case 2. OPT selects item i
	- We'll select best between subsets $1, ..., i-1$ with updated weight $w - w_i$

if i = 0 -> $OPT(i, w) = 0$
if $w_i > w$ -> $OPT(i, w) = OPT(i-1, w)$
else -> $OPT(i, w) = max\{OPT(i-1, w), v_i + OPT(i-1, w-w_i)\}$

We'll implement M in a bottom-up approach, and we'll scan the optimal solution in top-down. This algorithm is pseudo-polynomial in time, since it depends on the max weight limit $W$. In fact, this algorithm takes$O(nW)$ in time and space!
## Dynamic Programming summary
 In general, we have this kind of outline:
- Polynomial number of sub-problem
- solution to problem can be computed from sub-problems.
### Techniques
- **Binary choice**: Weighted interval scheduling
- **Multi-way choice**: segmented least squares
- **Adding new variable**: Knapsack problem
- **Dynamic programming over intervals**: RNA secondary structure.

Both Bottom-up and Top-down approaches are valid!