# Class of Problems
We'll be dealing with two classes of problems, even tho there are many more:
- **P** = {Problems solvable in polynomial time by a deterministic Turing machine}
- **NP** = {Decisional problems solvable in non-deterministic polynomial time, or also that there exists _an efficient certifier_ for them}
**def**: An efficient certifier $B(s,t)$ is an algorithm that
- Runs in polynomial time on |s|, |t|
- There exist a polynomial function $p$ s.t. for we have $s \in X$ if and only if there exists a string $t$ (certificate) such that. $|t| \le p(|s|)$ \[t should be polynomial on the input problem] and $B(s,t) = "Yes"$.
- $s$ is the *instance* of our problem X and $t$ is a solution.

$P \subseteq NP$, since there exist a polytime algorithm A that answers the problem. Problem is to know that $P=NP$.
### NP-Completeness
a NP-complete problem is one that "it's as hard" as all the problems in NP.
X is NP-complete if:
- $X \in NP$ (Problem X is NP)
- $\forall Y \in NP, Y\le_P X$ (Problem X is NP-Hard)
This can be used to know relationship $P-NP$. If $X$ is NP-Complete, and $X \in P$, then $P=NP$.
## Reductions
We can say that A is polynomially reducible to B if there exist a polytime algorithm that converts any instance of problem A into one of the problem B.
A is "as hard" as B, and we'll indicate it as $B \le_P A$ 
### Circuit SAT
This is the first problem that we kind of prove to be NP-complete. It's a string consisting of a series of variables and logic gates _AND_, _OR_, _NOT_. We'll study the _satisfiability_ of a problem, trying to see if there exists an assignation of variables with T/F that can make a string true.
The idea behind the proof is considering that given an algorithm $X \in NP$, there exists a verifier algorithm, which is just a sequence of logic gates.
### 3-SAT
There are $n$ binary variables: $x_1, x_2, ..., x_n$, $x_i \in \{0,1\}$, and we have $k$ clauses $C_1, C_2, ..., C_k$. A clause contains three variables, connected with OR, $t_i$ where $t_i = x_i$, or $t_i = \hat{x_i}$. Clauses are connected with AND logic gates.
Problem is finding an assignation for every $x_i$ such that all clauses return $TRUE$.

We'll apply the reduction $Circuit-SAT \le_P 3-SAT$:
- We create a variable for every node.
- We insert clauses that force the variable to implement the following operations:
	- **NOT**: $(x_i \lor x_j) \land (\hat{x_i} \lor \hat{x_j})$
	- **AND**: $(\hat{x_i} \lor x_j) \land (\hat{x_i} \lor x_k) \land(x_i \lor \hat{x_j} \lor \hat{x_k})$
	- **OR**: $(x_i \lor x_j) \land (\hat{x_i} \lor x_k) \land (\hat{x_j} \lor \hat{x_k} \lor x_i)$
For every two-variable clauses there will be added a variable.
### Independent Set
Given a graph $G=(V,E)$ and an integer $k$, does $G$ contain an independent set, which is a set of nodes that are not neighbors, of size $\ge k$?

We have $3-SAT \le_P Independent\ Set$.
For every clause we create a gadget that contains 3 nodes, each corresponding to one variable or it's negation. We then connect the gadgets as follows. If there is a variable $x_i$ in one clause and $\hat{x_i}$ in another, we'll connect the relative nodes with an edge. We'll say then that the original 3-sat problem is "yes" if and only we can create an independent set of size $\ge k$, with $k$ being the number of variables.
### Vertex Cover
Given a graph $G=(V,E)$ and an integer $k$, does $G$ contain a subset $S$ of nodes of size $|S| \le K$ such that for every $e=(u,v) \in E$ we have $u \in S$ or $v \in S$. We say that $e$ is covered.

We have proven that Independent Set and Vertex Cover are one the opposite of the other.
### Set Cover
Given universe of elements $U = \{e_1, e_2, ..., e_n\}$ and some sets $S_1, S_2, ..., S_m$ over $U$, such that $\cup_{i}S_i = U$, and given integer $k$. Find a subset $S$ of sets among $S_i$ whose union is $U$, and $|S| \le k$.

It can be easily proven that $Vertex\ Cover \le_P Set\ Cover$. Given an instance of vertex cover $G=(V,E)$ we will create a universe of elements $U=E$. We will also create the subset $S_i$ containing all edges incident with node $v_i$. There exist a vertex cover of size $\le k$ if and only if we can create on this instance a set cover of size $\le k$
### 3D-Matching
Given disjoint set $X, Y, Z$ of elements, each of size n, and given triples $T \subseteq X \times Y \times Z$, the goal is to choose subsets $S \subseteq T$ such that $\forall e \in X \times Y \times Z\ \exists! e \in s\ s.t.\ s \in S$.

We can prove that $3-SAT\le_P 3D-Matching$. Given an instance $x \in 3-SAT$ with n variables and k clauses we'll add $2nk$ elements.
- We'll encode all of the variables in _variable gadgets_: For every $x_i$, if $x_i = 1$ if the even tips are free, $x_i = 0$ elsewhere. Like this, each core element will be covered once.
- We'll have a tip for every clause, creating _clause gadgets_: for every variable $x_j$ in our clause $C_i$ we'll create two elements $p_i, p_i\prime$ and we'll connect them to every tip $b_{j, 2i}$ according if $x_j$ or $\hat{x_j}$.
- We'll create _cleanup gadgets_, that will cover all of the tips that aren't covered by clauses

![[Pasted image 20250202112303.png]]

If we manage to be able to do it for everything we will be able to create a unique 3D-match.
### Subset Sum
Given n integers $A = {a_1, a_2, ..., a_n}$, and given target $T$, is there a subset $S \subseteq A$ such that $\sum_{s\in S}s = T$.

we'll reduce $3D-Matching \le_P Subset\ Sum$, by mapping 3D-matches with a unique value. 
In the present situation, we handle this problem by a simple trick. We have only m numbers in all, and each has digits equal to 0 or 1; so if we assume that our numbers are written in base $d = m + 1$, then there will be no carries at all.
We construct the instance of subset sum, with for each triple $t=(x_i,y_j, z_k)$ we construct a number $w_t$ in base $m+1$. We define W to be the number in base $m+1$ with $3n$ digits, each of which is equal to 1, that is $W = \sum_{i=0}^{3n-1}(m+1)^i$.
A set $T$ of triples contains a perfect three-dimensional matching if and only if there is a subset of numbers $\{w_t\} that adds up to $W$.
### Hamiltonian Cycles
Given a directed graph, does it have a simple cycle that visits all nodes?

We can do $3-SAT \le_P Hamiltonian\ Cycles$:
We'll create a directed $s-t$ strongly connected graph with $n$ levels, one for each variables, and $2nk$ nodes for each level. At this point we'll create _clause gadgets_: if $x_i = 1$ we'll add node $u$ and two edges: $(v_{i, 2j}, u), (u, v_{i, 2j+1})$. It'll be specular if $x_i=0$.
There'll exist a Hamiltonian cycle if and only if $\forall C_j$ at least one of the edges that pass $u_j$ are passed.
![[Pasted image 20250202115528.png]]
### Traveling Salesman Problem
We have a graph $G=(V,E)$., with every edge connecting two nodes having a non-negative distance $d(v_i, v_j)$. Given an instance, and a budget $D$ is there a tour that starts and finishes in the same node, and visits all nodes with a total distance $\le D$?

We can easily prove $Hamiltonian\ Cycles \le_P TSP$.
### Scheduling with Release Time and Deadlining
As an input we have $n$ jobs that must be scheduled in a single machine. Each job $j$ has:
- Release time $r_j$, where the job is available after $r_j$
- Duration $t_j$ in which it requires $t_j$ contiguous time steps
- Deadline $d_j$, where the job must finishes before $d_j$. So we need to assign $t_j$ steps during \[$r_j, t_j$]
Does there exist a schedule that allows to process all $n$ jobs?

We can demonstrate that $Subset\ Sum \le_P SRTD$
We have an instance of subset sub $w_1, w_2, ..., w_n$ and W. We create the instance of SRTD with $n+1$ jobs. The first $n$ we'll create as $r_j = 0$, $t_j = w_j$, $d_j = 1+ \sum_{i=1}^{n}w_i$.
The last job will be $r_{n+1} = W$, $t_{n+1} = 1$, $d_{n+1}=W+1$.
We'll be able to schedule the job iff there exist a subset $S$ that we can assign before the job $n+1$ and that has $\sum_{i \in S}{w_i} = W$.
## CO-NP Class
Regarding the NP-Class we can do an observation; to say that a problem $X$ is in NP we present a certificate, verifying that it's solvable in polytime.
String $s$ is a "yes" if and only if there exist a short $t$ such that $B(s,t)$ = "yes". Negating it is not easy, s is "no" if and only if for ALL short t we have $B(s,t)$ = "no".
CO-NP class is the _complementary_ class to NP.

We can also say that if $X \in P$, $\hat{X} \in P$  since once calculated X with $A$ we can produce $\hat{A}$ that flips the result over. This cannot be said about NP problems, since for all $s \in \hat{X}$ if and only if for all t of of at most |p|, $B(s,t)$ = no. We cannot just invert, since definition changed from "exists t" to "for all t".

is $Co-NP = NP$? Not easy, as this would answer problem $P=NP$. This kinds of problems, that belong both in NP and Co-NP are called of _good-characterization_.
# Approximation Algorithms
Idea behind them is, for the NP-Hard problems which would take a long time to optimally resolve, to create an algorithm that goes "close" to a solution by a given margin.
$$
\frac{GREEDY}{OPTIMUM} \le apprx\_value\ \ \ \  [For\ minimization\ problems]
$$
In this case our solution doesn't get more distant than $apprx\_value$ from the optimal solution 
$$
\frac{GREEDY}{OPTIMUM} \ge apprx\_value\ \ \ \  [For\ maximization\ problems]
$$
In this other case our greedy solution is with value at least OPT/$apprx\_value$
## Load Balancing
The problem of Load balancing implies to have $m$ machines, and $n$ jobs with each taking $t_i$ units. We want to assign the jobs to the machines to minimize the system's _makespan_, which is the maximum time units needed for any machine to finish the assigned jobs.

This problem is NP-Complete, but we'll propose an approximation algorithm that's polynomial.
```
Greedy_balance:
	start with no jobs assigned
	set T_i = 0 and A_i = empyset for all machines M_i
	for j= 1, ..., n
		let M_i be a machine that has minimum time T_i
		assign job j to machine M_i
		set A_i = A_i + {j}
		set T_i = T_i + t_j
	return assignment, max(T_i)
```
The greedy_balance algorithm returns a 2-approximation algorithm, which means that $T_{greedy} \le 2\times T_{OPT}$.
**Pf**: 
We know that T* $\ge_1 \frac{1}{m} \sum_{j=1}^{n}t_j$, and also that T* $\ge_2 \max_j t_j$ 
We'll also consider that just before inserting $t_j$ in the machine $M_i$, that before that had load $T_i - t_j$, which means that for every machine $M_k$ I have $T_k \ge T_i - t_j$. Summing both terms $m$ times we'll have.
$$
\sum_{l=1}^m {(T_i - t_j)} \le \sum_{l=1}^m T_l \rightarrow T_i-t_j \le \frac{1}{m}\sum_{l=1}^mT_i \rightarrow_1 T_i -t_j \le T^* \rightarrow_2 T \le T^* + t_j \le 2T^*
$$

We can achieve an even better $\frac32$-approximation if we order the set before running the algorithm. At the last step now we can say more, because we know that $T^* \ge 2t_n$
$$
T_i -t_j \le T^* \rightarrow T \le T^* +t_j \rightarrow_3 T \le T^* +\frac12T^*\rightarrow T \le \frac32T^*
$$

## Center Selection
We have another set of problems where we have a set $S$ = $\{S_1, ..., S_n\}$ of $n$ sites, and an integer $k$. We have also a function $dist : S \times S \rightarrow R$ which follows triangular disequation. 
We'll open $k$ centers $C = \{c_1, c_2, ..., c_k\}$. We'll also define $dist(s, C) = \min_{c \in C} dist(s, c)$.
Find $k$ centers such that we minimize $r= \max_{s \in S} dist(s, C)$.

Since we are dealing with an optimization problem, Center Selection is NP-hard.
Assuming that we know the radius $r$, we still need to find the location of the centers.
```
S' will represent the sites that still need to be covered
S' = S
let C = emptyset
while S' is not empty
	Select any site s in S' and add s to C
	Delete all sites from S' that are distant at most 2r from s
if |C| <= k then
	return C as the selected set of sites
else
	claim that there is no set of k centers with at most 2r of covering radius
```
we claim that this is a 2-approximation algorithm , since we are assigning the centers at $2r$ distance, and our optimal solution cannot be less than $r$. We need to prove that if we have more than k points then there is no way to cover all points with radius $r$, and so optimal solution has radius $>r$, which can be easily done by showing that for every center $c_i \in C$ there exist a $c^* \in C^*\ s.t.\ dist(c_i, c^*) \le r$. Each center $c^*$ cannot be mapped to two more centers $c \in C$, since they would be deleted by the algorithm being $\le 2r$.

This is a valid reason that can take us close to our solution, but it's slow. We need to find a $r$ big enough to cover all sites, but small enough to be a good precision indication.
A
```
Assume k <= |S| (otherwise we can put centers in each site)
select any site s and let C = {s}
while |C| < k
	select a site s in S that maximizes dist(s,C)
	add site s to C
return C
```
## Weighted Set Cover
We have a universe of elements $U = \{e_1, ..., e_n\}$ and some sets over U as previously defined. For every set $S_I$ we have an associated cost $w(S_i)$. Now we want to select a subset $C \subseteq S$, such that we cover all elements and we minimize overall cost.
```
Greedy-Set-Cover
Start with R=U and no sets selected
while R is not empty
	select set S_i that minimizes w_i/|S_i intersection R|
	delete S_i from R
return selected sets
```
this is a $O(log\ n)$ approximation algorithm. Given that the greedy solution C has weight $w(C) = \sum_{s \in C} w(s) = \sum_{s \in U} c_s$. We'll lower bound our optimal solution, by saying that for every set $S_k$ we have $w(S_k) \ge \frac1{H(|S_k|)}*\sum_{s \in S_k}c_s$. Without loss of generality, we rename the elements $s_j \in S_k$ by ordering them by the "covering order". 

When the greedy covered element $s_j$ using some set $S_i$ there were at least $|S_k \cap R| \ge d-j+1$ uncovered elements. We know that at the time $S_i$ was selected
$$
c_{s_j} = \frac{w(S_i)}{|S_i \cap R|} \le \frac{w(S_k)}{|S_k \cap R|} \le \frac{w(S_k)}{d-j+1}
$$
using the property we had before, we can continue our proof by saying
$$
\sum_{s_j \in S_k} c_{s_j} \le \sum_{s_j \in S_k}\frac{w(S_k)}{d-j+1}=w(S_k)\sum_{j=1}^d\frac1{d-j+1} = w(S_k)\sum_{j=1}^d\frac1j = w(S_k)*H(d)
$$
Now, let $d^* = max |S_k|$ and $C^*$ be our optimal solution.
$$
w(C*) = \sum_{S_k \in C}w(S_k) \ge \sum_{S_k \in C}\frac1{H(|S_k|)}\sum_{s_j \in S_k} c_s \ge \frac1{H(d^*)}\sum_{S_k \in C}\sum_{s_j \in S_k}c_s \ge_1 \frac1{H(d^*)}*\sum_{s \in U}c_s = \frac{w(C)}{H(d^*)}
$$
(1) = every element gets covered by 1 ore more sets
this proves that $w(C) \le O(\log n)\ w(C^*)$
## Weighted Vertex Cover
This is a special case of weighted set cover, and _although we cannot use approximations algorithms for other reducible problems_, we could use the Weighted set cover problem to resolve it and have a $O(\log n)$ approximation. 

We can use another method based on "_paying a price_" method to minimize the cost. As the set cover, we defined $c_s$ as the cost payed to cover the element s with a set, and we tried to pay less. In here we have a similar idea, considering each edge as an "agent" willing to "pay" something to the node that covers.
We'll talk about fairness if the cost payed by selecting the vertex $i$ is less than the sum of all the agents: $\sum_{e=(i,j)}p_e \le w_i$.
This idea of prices gives us a lower bound on the cost of any solution, $\sum_{e\in E}p_e \le w(S^*)$, which can be easily proven by summing to the disequation presented before all vertexes selected, and considering that being a vertex cover, each edge has at least one vertex that covers it.
```
Vertex-Cover-Approx(G,w):
	set p_e = o for all e in E
	while there is an edge e=(i,j) such that neither i nor j is tight
		select such edge
		increase p_e without violating fairness
	let S be set of tight nodes
	return S
```
This will return a valid vertex cover, since we guarantee that there is no edge that isn't covered by at least one tight node, and we know that at every iteration we'll have one or more tight nodes. This means that some edge may need to "pay" its two nodes twice!
This means that $w(S) \le 2\sum_{e \in E} p_e$.
**Pf**:
$$
w(S) = \sum_{i \in S} w_i = \sum_{i \in S} \sum_{e = (i,j)} p_e \le 2 \sum_{e \in E} p_e \le 2w(S^*)
$$
This also demonstrates that this has a $2$-approximation ratio.
## Integer Programming
It's a very strong method of proving the approximation bound of a lot of problems. In this case we have a set of variables $x^T = [x_1, x_2, ..., x_n]$, a matrix of constraints $A \in R^{m \times n}$, a cost vector $c^T = [c_1, c_2, ..., c_n]$, and a constraint vector $b^T = [b_1, ..., b_m]$.
we create this system:
$$
\min c^Tx
$$
$$
s.t.\ Ax \ge b\ \ \ \ \ x \in \{0,1\}
$$
#### For vertex cover
Given that this is a NP-Hard problem we can also model a lot of problems using this approach, for example Vertex Cover, by modelling integer variables, setting $x_i$ to $1$ iff the node $v_i$ got selected, and $0$ elsewhere, modelling the node weight as $w^T=[w_1, w_2, ..., w_n]$, and the constraints as $\forall (i,j) \in E\ \ x_i+x_j \ge 1$, with $x_i \in\{0,1\}$.

By computing the relaxation $w_{LP}$ we already have a good approximation value, since $w(S^*) \ge w_{LP}$. We'll call $\frac{w(S^*)}{w_{LP}}$ the _integrality gap_. Solving linear programming in polytime is possible, thanks to Simplex method, such that we get values for $x_1, x_2, ..., x_n$, all $x_i \in [0,1]$. We need now to set $x_i$ such that each variable respects the integer property, so we'll let our solution (1) $S = \{i \in [n]\: x_i \ge \frac12 \}$. We can see that $w(S) \le 2w_{LP}$, since:
$$
w_{LP} = \sum_{i=1}^nw_ix_i \ge \sum_{i \in S}w_ix_i\ge_1 \sum_{i \in S}w_i\frac12 = \frac12 \sum_{i \in S}w_i = \frac12w(S)
$$
with this we can reach our final 2-approximation, which tells us that $w(S) \le 2w_{LP}\le 2w(S^*)$.

This is a very solid way to prove a constant approximation ratio, that's dependent mostly on the set of constraint A.
#### For set cover
we can create an Integer Programming problem by considering $x_i = 1$ if we select set $S_i$, and so then creating the problem of $\min \sum w_ix_i$, considering that $\forall j \in [n]$ we'll need to satisfy $\sum_{i:e_j \in S_i} x_i \ge 1$, which means for every element $e_j$, make it such that the sum of all selected sets covering the element $e_j$ is at least $1$.
# Randomized Algorithms
The idea behind this approach is that by following probability we may have a better outcome, given that it'll give us a good approximation with good probability. We'll expand more on this concept later, for now we'll be talking about set cover randomization.
## Randomized rounding for (weighted) set cover
Let $w_{LP} be the optimal solution of (SC.LP) and let $C^*$ be the optimal solution for (SC.IP), then we know that $w_{LP} \le w(C^*) = \sum_{S_j \in C^*}w_j$.
```
let x = [x_1, x_2, ..., x_m] optimal solution for SC.LP
Randomized-Rounding
	for l = 1,..., c*ln n times
		C_l = {}
			for j=1,..., m
				insert S_j into C_l with probability x_j
		C =  C u nion C_l
	return C
```
#### Claim 1:
$$E[w(C)] \le (c\log n) w(C^*)$$
**Pf**:
We define the random variable indicator $x_j^l$ and we make it $1$ iff $S_j \in C_l$, $0$ else.
$Pr(x_j^l = 1) = x_j$ => $E[x_j^l] = 1 * Pr(x_j^l =1) + 0*Pr(x_j^l =0) = x_j$ 
We continue our proof:
$$
E[w(C_l)] = E[\sum_{j=1}^m w_jx_j^l] = \sum_{j=1}^m w_jE[x_j^l] = \sum_{j=1}^m w_jx_j^l = w_{LP}
$$
Given this, and knowing that probabilities are independent and the set $C$ is union of all $C_l$
$$
w(C) \le \sum_{l=1}^{c\log n} C_l \Rightarrow E[w(C)] \le \sum_{l=1}^{c\log n} E[C_l] \Rightarrow E[w(C)] \le c\log nw_{LP} \le c\log \ w(C^*)
$$
#### Claim 2:
Every element is covered with probability of at least $\ge 1-\frac1n$
**Pf**:
We consider some element $e_i$. Given the difficulty of finding probability that element gets cover in _at least_ one set $C_l$, we'll calculate the inverse probability
$$
Pr(e_i \notin C) = Pr(\forall l\in[c\log n]:e_i \notin C_l) =_1 \prod_{l=1}^{c\log n}Pr(e_i \notin C_l)
$$
considering that $Pr(e_i \in C_l)$ represents the probability that element $e_i$ got added in $C_l$ because there was a set $S_j$ that contained $e_i$
$$
Pr(e_i \notin C_l) = Pr(\forall j:e_i \in S_j:x_j^l = 0) =_1  \prod_{j:e_i \in S_j}Pr(x_j^l = 0) \le_2 \prod_{j:e_i \in S_j}e^{-x_j} = e^{-\sum_{j:e_i \in S_j}x_j} \le_3 e^{-1}
$$
$(1)$ The choices for different rounds are independent
$(2)$ For any $x$ there exist inequality $1+x \le e^x$
$(3)$ $x_j$ satisfies the constraint of SC.LP 
So, to continue the first part
$$
Pr(e_i \notin C) \le \prod_{l=1}^{c\log n} e^{-1}= (e^{-1})^{c\log n}=(e^{\log n})^{-c} = \frac{1}{n^c}
$$
So the probability that _some element didn't get covered_ becomes
$$
Pr("some\ element\ not\ covered") \le_4 \sum_{i=1}^nPr(e_i \notin C) \le \frac1{n^{c-1}}
$$
With $c=2$ the probability of covering all elements becomes
$$
Pr("All\ elements\ covered") = 1-Pr("some\ element\ not\ covered") \ge 1-\frac1n
$$

so, $c$ becomes a double-edged sword, the bigger it is the more the probability of getting a valid result, but the approximation ratio gets bigger.
## Randomized Global min cut
This algorithm uses the concept of multi-graphs $G=(V,E)$ in which a node can contain multiple other nodes that have been contracted into it.
```
S(v) = set of nodes that have been contracted into v
S(v) = {v} for each node
Contract
	if |V| = 2
		return S(v_1), S(v_2)
	else
		choose edge e randomly
		let G' be graph resulting from contraction of e
		create node z_uv replacing u, v
		s(z_uv) = S(u) union S(v)
		Contract
```
Let's pick a minimum cut, and we'll assume that the size of cut is k.
If I never contract one of those k edges then the algorithm is optimal. What's the probability of this happening?
Let $E_i$ be the event "I don't contract an edge of the min-the cut in the $i$'th round", $\forall i \in [n-2]$
Probability of success is
$(1): Pr(E_1)\cdot Pr(E_2|E_1)\cdot Pr(E_3|E_2E_1)\cdot ...\cdot Pr(E_{n-2}| E_{n-3}...E_2E_1)$
$Pr(E_1) = 1-\frac km \ge_2 1 - \frac2n \Rightarrow Pr(E_{j+1}|E_1,...,E_j) \ge 1-\frac2{n-j}$   
$(2)$ Considering that $m \ge \frac{nk}{2}$ (every node has degree $\ge k$ and t)

Continuing the $(1)$ we see that the probability of reporting the correct and optimal answer is:
$$
(1) \ge (1-\frac2n)(1-\frac2{n-1})(1-\frac2{n-2})...(1-\frac24)(1-\frac23)= \frac2{n(n-1)}= \binom{n}{2}^{-1}
$$
It's very small! So we'll boost our probability by repeating the algorithm $T$ times so that we reach "satisfying probabilities":
$$
(1-\frac2{n(n-1)})^T \le e^{\frac{-2T}{n(n-1)}}
$$
We'll choose a value for T such that $e^{\frac{-2T}{n(n-1)}} = n^{-1}$, which will give a value of $T= \frac{n(n-1)\log n}2$
## Max 3-SAT
When we studied NP-Completeness, the biggest problem was the decisional 3-SAT. We'll modify the problem a bit, by asking to make _all clauses_ true to finding a truth assignment that satisfies _as many clauses as possible_. It's an NP-Hard optimization problem, since 3-SAT is a decisional problem on $k\ge m$.
A possible implementation is pretty simple, and works by independently setting each $x_i$ variable to 0, or 1, with a $\frac12$ probability.
We'll then create variable $Z_i$ to indicate whenever the clause $C_i$ is satisfied. Thus, it becomes a problem of finding $\max\sum_i{Z_i}$ .
$E[Z_i]$ equals to the probability of the clause $C_i$ to be satisfied. Since a clause is satisfied if there is at least one variable satisfied, we'll find this probability by calculating 
$$
Pr(Z_i = 1) = 1-Pr(Z_i = 0) = 1-Pr(t_1 = 0)Pr(t_2 = 0)Pr(t_3 = 0) = 1 -\frac18 = \frac78
$$ Given that $OPT \le m$, we will have that $GREEDY = E[Z] = \sum_iE[Z_i] = \frac78 m \Rightarrow GREEDY = \frac78m \ge \frac78 OPT$   