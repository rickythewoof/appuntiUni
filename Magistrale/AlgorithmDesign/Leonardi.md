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
We'll calculate lateness as $ l_j =  max {0, $f_j-d_j$}. And we'll schedule all jobs to minimize the maximum lateness $L = max_j l_j$.
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
## Sequence Alignment
The idea is to calculate how similar are two strings, considering as a cost the sum of mismatches and gaps.
Given two strings $x_1, x_2, ..., x_m$ and $y_1, y_2, ..., y_n$ find the min cost alignment, which is a set of ordered pairs $x_i, y_j$ such that each item occurs in at most one pair and there are no crossings.
this cost of alignment is
$$
cost(M) = \sum_{(x_i, y_j)\in M}{a_{x_i, y_j}} + \sum_{i:x_i\ unmatched}{\delta}+ \sum_{j:y_j\ unmatched}{\delta}
$$
We define our $OPT(i,j)$ as the min cost of aligning prefix strings $x_1, x_2, ..., x_i$ and $y_1, y_2, ..., y_j$, having three different cases
- Case 1: OPT matches $x_i, y_j$
	- pay mismatch cost + cost of aligning rest of string ($OPT(i-1, j-1)$)
- Case 2: OPT leaves $x_i$ unmatched
	- Pay gap price + min cost of rest ($OPT(i-1, j)$)
- Case 3: OPT leaves $y_j$ unmatched
	- Pay gap price + min cost of rest ($OPT(i, j-1)$)
### Hirschsberg's Algorithm for sequence alignment
Works by considering: let $f(i, j)$ be the shortest path from $(0,0)$ and $(i,j)$. We'll know that $f(i,j)=OPT(i,j)$. We have also $g(i,j)$, which is the shortest path from $(i,j)$ to $(m,n)$.
The shortest path that uses $(i,j)$ is $f(i,j)+g(i,j)$.
- **Divide**: We'll find an $q$ that minimizes  $f(q, n/2)+g(q,n/2)$; aligning $x_q$, and $y_{n/2}$. 
- **Conquer**: Recursively compute optimal alignment in each piece
Hirschberg's running time will be $O(mn\ logn)$.
## Bellman-Ford
It's the problem of finding the shortest path in a diagraph $G=(V,E)$, with arbitrary edge cost (also negative).
We cannot use Dijkstra, nor can we adapt the problem by reweighing. We have also the issue of negative cycles that can infinitely reduce the weight. So we'll need to find the shortest path that has also simple cycles. We'll model our algorithm by considering two possibilities:
- Cheapest $v-t$ path uses $\le i-1$ edges.
	- $OPT(i,v) = OPT(i-1, v)$
- Cheapest $v-t$ path uses exactly $i$ edges:
	- If $(v,w)$ is the first edge, then $OPT$ uses $(v,w)$ and then selects best $w-t$ paths using $\le i-1$ edges, so we'll try and find optimal path from all possible nodes $w$ to $t$.
	- $OPT(i,v) = \min_{(v,w)\in E}\{OPT(i-1,w)+c_{vw}\}$
We'll also need to find a way to check for negative paths, but it's simple since if after the $n-1$ iteration we shouldn't be able to find a better path. 
We can also do some optimization work:
- **Space Optimization**: We can maintain two 1-dimensional arrays, instead of a 2D one
	- $d(v)$: cost of cheapest $v-t$ path found so far
	- $successor(v)$: next node on a $v-t$ path
- **Performance Optimization**: We can say that if the $i-1$ iteration $d(w)$ wasn't updated, there is no reason to consider edges entering $w$ in the iteration $i$.
Especially in the space optimization it's like in Dijkstra, we have some information about distance in every node, but we calculate it bottom-up.
### Distance Vector protocols
This is the kinds of protocol used in the internet, in which we use information of the neighbor node to calculate the best path to a given destination. Even though all edges that connect routers are non-negative (since they represent delays) we still use Bellman-Ford for not needing to have the knowledge of the entire network to know a best path. It's a different routing algorithm in respect to *link state routing*, in which each router stores the entire path.
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
# Network Flow
We abstract graphs even more, by considering it as a way in which a material _flows_ through the edges. We have a digraph $G=(V,E)$, with a source $s \in V$ and a sink $t \in V$, and non-negative integer capacities $c(e)$ for each edge $e \in E$.
### Min cut problem
We then define _st cut_ as a partition $(A,B)$ of the vertices, in which $s \in A$ and $t \in B$. The capacity of the cut is the sum of the capacities of the edges from a to be
$$
cap(A,B) = \sum_{e\ out\ of\ A}{c(e)}
$$
We'll then define the problem of _min-cut_, which is finding a cut with minimum capacity
### Max flow problem
We'll define a _st-flow_ as a function $f$ that satisfies the following properties:
- for each $e \in E$: $0 \le f(e) \le c(e)$ \[Capacity]
- for each $v \in V \ {s,t}$: $\sum_{e\ into\ v}{f(e)} = \sum_{e\ out\ of\ v}{f(e)}$ \[Flow conservation]
With this we can define  the _value_ of a flow $f$ as
$$
val(f) = \sum_{e\ out\ of\ s}{f(e)}
$$
We'll then define the problem of _max-flow_, which is finding a flow of maximum value.
## Ford-Fulkerson Algorithm
The idea behind finding a max-flow is to find an $s-t$ path, augmenting the flow along this path P, and doing these two operations until we get stuck. This by itself doesn't give us the optimal solution, since we don't have any way to "backtrack", to find a better distribution of the flow along all incident edges of a node.
### Residual graph
We'll define for this reason a "residual edge"
- **Original edge**: $e=(u,v) \in E$
	- flow $f(e)$
	- capacity $c(e)$
- **Residual edge**: $e^R = (v,u)$ which represents the actual flow
	- We "undo" the flow sent
	- Residual capacity
$$ 
c_f(e) = c(e)-f(e)\ if\ e\in E
$$
$$
c_f(e) = f(e)\ if\ e^R\in E
$$
We remove the need of a flow by introducing the residual capacity
We'll have a residual graph $G_f = (V, E_f)$ in which:
- Residual edges have positive residual capacity
- $E_f = \{e:f(e)<c(e)\}\cup \{e^R:f(e) > 0\}$
- Key property is: $f\prime$ is a flow in $G_f$ if and only if $f+f\prime$ is a flow in $G$.
### Augmenting path
An _augmenting path_ is a simple $s-t$ path $P$ in the residual graph $G_f$, and the bottleneck capacity of an augmenting path $P$ is the minimum residual capacity of any edge in $P$.
We find an interesting augmenting property: let $f$ be a flow, and let $P$ be an augmenting path in $G_f$. Then $f\prime$ is a flow and $val(f\prime) = val(f)+bottleneck(G_f, P)$
```
Augment(f,c,P)
	b = bottleneck capacity for path P in G_f
	foreach edge e in P
		if e in E
			f(e) = f(e) + b # Augment the path in edge of the original G
		else
			f(e^R) = f(e^R) - b # The residual capacity gets lowered by b
```
### The algorithm
```
Ford-Fulkerson(G,s,t,c)
foreach edge e in E 
	f(e) = 0
	G_f is residual graph
	while there exist an augmenting path P in G_f
		f = augment(f,c,P)
		update G_f
return f
```
### max-flow min-cut theorem
We know that in general, let $f$ be any flow and let $(A,B)$ be any cut, then the flow across $(A,B)$ equals the value of $f$. This can be easily be proven by considering that $val(f) = \sum_{e\ out\ s}f(e)$, and by flow conservation the sum of the flow in and out of v are zero, except for s.
With this we build a weak duality, in which $val(f) \le cap(A,B)$. 
**Pf**:
$$
v(f)\le \sum_{e\ out\ A}{f(e)}\ -\sum_{e\ in\ A}{f(e)} \le \sum_{e\ out\ A}{f(e)} \le \sum_{e\ out\ A}{c(e)} \le cap(A,B)
$$
Now we have two different theorems:
- **Augmenting path theorem**: a flow $f$ is a max-flow if and only if there are no augmenting paths
- **max-flow min-cut theorem**: The value of the max-flow is equivalent to the capacity of the min-cut.

	**Pf**: It's directly connected to three conditions:
	1. There exist a cut $(A,B)$ such that $cap(A,B) = val(f)$
	2. $f$ is a max flow
	3. there is no augmenting path with respect to $f$
### Capacity-scaling
In general, with the Ford-Fulkerson's algorithm, we know that an augmentation will always increase the flow of 1. Since we'll calculate the value of the flow $f*$ in at most $nC$ iterations, we know that the running time of the algorithm is $O(nmC)$. It's pseudo-polynomial!
We need to find a way to find _good augmenting path_, which is by finding augmenting paths for all edges that have residual capacity $\ge \Delta$. We iterate over this limit, and then will do this operation for $\Delta = \Delta / 2$
This will have a computational cost of $O(m^2\ log\ C)$ time
### Shortest Augmenting Path
The algorithm selects smartly the path to which we augment by selecting the shortest $s-t$ path, with for example BFS (the least hops needed is equal to the level of t).
By doing this, the shortest augmenting path algorithm runs in $O(m^2\ n)$ time:
- $O(m+n)$ for BFS.
- $O(m)$ augmentations for paths of length $k$.
- if there is an augmenting path, then there is a simple one:
	- $1\le k< n$
	- $O(mn)$ augmentations
### Blocking Flow algorithm

The blocking flow algorithm focuses on finding a maximal flow by iteratively finding _blocking flows_, which are augmenting flows that cannot be increased further without violating the capacity constraints. A blocking flow is a set of edge-disjoint paths that together push the flow from the source to the sink. The key idea is to find these blocking flows in each phase and augment the flow accordingly. 
```
Initialize(G,s,t,f,c)
	L_g = level-graph of G-f
	P = empty set
	goto advance(s)

Advance(v)
	if v==t
		augment(P)
		remove saturated edges from L_G
		P = empty
		goto Advance(s)
	if exists edge (v,w) in L_G
		Add edge (v,w) to P
		goto Advance(w)
	else goto retreat(v)

Retreat(v)
	if v == s
		stop
	else
		delete v and all incident edges from L_G
		remove last edge (u,v) from P
		goto Advance(u)
```

## Unit-capacity simple networks
A network is a _unit capacity simple network if_:
- Every edge capacity is 1
- Every node apart from $s$ or $t$ has either at most 1 entering or exiting edge
This is the case, for example, in bipartite matching.
We can use the blocking flow algorithm to calculate maximum flow, taking $O(m\ n^{1/2})$ time:
- At each phase of normal augmentations takes $O(m)$ time
- After at most $n^{1/2}$ phases, $v(f*) \le v(f) + bottleneck*n{1/2}$ =>  $v(f) \ge v(f*) - n^{1/2}$
- After at most $n^{1/2} additional augmentations, flow is optimal
## Applications
### Bipartite Matching
We can formulate a problem of a bipartite matching with a network max-flow formulation.
Given a graph $G=(L\cup R, E)$, we create another graph $G\prime = (L\cup R\cup \{s,t\}, E\prime)$ in which:
	- we add nodes $\{s,t\}$
	- for every $e\in E$ -> Create an edge $e$ in $E\prime$ with $c_e = \infty$
	- for every $l \in L$, add $e =(s, l)$ with cost $c_e = 1$
	- for every $r \in R$, add $e =(r, t)$ with cost $c_e = 1$
We can say that Max Cardinality of a matching in $G$ equals to the value of max-flow in $G\prime$.
Given a graph, a subset of edges M in E is a perfect matching if each node appears in exactly one edge in $M$. given $S$ a subset of $L$, $N(S)$ is the set of nodes in $R$ connected with S. a graph has a perfect matching if $N(S) \ge S$ for every subset $S$ of $L$.

Possible applications can be done in
- Survey design
### Disjoint paths
Given a graph, and two nodes s, and t, we want to find the max number of edge-disjoint $s-t$ paths. Easily enough we can do it by considering the digraph $G$ and doing a network flow with all unit-capacity edges. The relative value of the flow is equal to the number of different edge-disjoint paths.
It's trivial to create the equivalent problem of _node-disjoint paths_ by transforming the graph $G$ to a relative $G\prime$ and doing a edge-disjoint path problem on that.
### Circulation (unknown)
Given a digraph $G=(V,E)$ with non-negative edge capacities $c(e)$ and node supply and demands $d(v)$, a *circulation* is a function that satisfies:
- for each $e \in E$: $0\le f(e) \le c(e)$ \[Capacity (as before)]
- for each $v \in V$: $\sum_{e in V}{f(e)}-\sum_{e out V}{f(e)} = d(v)$ \[Conservation]
In this case we won't have a source or a sink, but we'll be having supply nodes ($d(v) < 0$), demand nodes ($d(v) > 0$), and transshipment nodes.

We can formulate it as a max-flow problem, by adding source $s$ and sink $t$, and:
- for each $v$ with $d(v)<0$, we'll add an edge $(s,v)$ with capacity $c_{(s,v)} = -d(v)$
- for each $v$ with $d(v) > 0$, we add an edge $(v, t)$ with capacity $c_{(v,t)} = d(v)$
If we have lower bounds to be satisfied we may want to also add the decisional problem of _feasible circulation_, which can still be modeled to a max-flow problem by updating the demands in both endpoints. $f(e)$ is a circulation in $G$ iff $f\prime (e) = f(e)-l(e)$ is a circulation in $G\prime$.
![[Pasted image 20250201183858.png]]
### Project Selection
Prerequisites:
- Set of possible projects $P$: Project $v$ has associated revenue/cost $p_v$
- Set of prerequisites $E$: if $(v,w) \in E$, cannot do project $v$ unless we also do project $w$.
- A subset of projects $A$ in $P$ is feasible if the prerequisite for every project in $A$ also belongs in $A$.
We'll create a prerequisite graph in which all nodes are projects, and we'll add edge $(v,w)$ if we cannot do $v$ without doing $w$. We'll assign infinite capacity to all prerequisite edges.

At this point we'll do a very similar thing we did to circulation->max-flow (with demand nodes as cost, supply as revenue).
- we add edge $(s,v)$ with capacity $p_v >0$
- we add edge $(v,t)$ with capacity $-p_v$ if $p_v < 0$
