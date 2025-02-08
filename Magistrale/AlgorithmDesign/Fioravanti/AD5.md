# Exercise Week 5
## Ex 1
To show that clique is an NP-Complete problem we will use the fact that:
1. It is in NP, since it's polynomial-time to check for a complete graph
2. we can do a reduction $3-SAT<_PClique$.
	Given an instance of 3-sat we will create a cluster of 3 nodes, each representing one variable of the Clause. We'll then connect every node with other mutually-compatible nodes of clusters related to other clauses. We can then say that there exist a satisfiable assignation of variables if there is a subset of vertices $S$, with at least one for every clause, such that we can create a complete subgraph.
## Ex 2
We can prove that Max2SAT is NP-Complete if we can prove that:
1. It's in NP
2. We can create a reduction $Clique <_P Max2SAT$
	For every node we create 2 different clauses
	$(x_i\lor z)$
	$(x_i \lor \hat{z})$
	if there are two nodes $x_i, x_j$ such that $\nexists (x_i, x_j) \in E$, then create another clause
	$(\hat{x_i} \lor \hat{x_j})$  
## Ex 3
We can prove NP-Completeness of this problem by proving that:
1. It's in NP, since it's easy to check that all the accepted bids are proper and that the sum of bids it's at least the bound $B$
2. We'll do this by a reduction $Indipendent-Set <_P WinnerDetermination$.
	We have a graph $G=(V,E)$, and a parameter B. We'll create an instance of _WinnerDetermination_ as follows:
	- Every edge $e \in E$ represents an item
	- Every node $v \in V$ represents a bid.
	- A bid $S_v$ contains all edges - items that are incident to $v$
	- Every bid has a price of $1$.
## Ex 4
Class scheduling. We'll prove NP-Hardness by doing reduction
$Vertex-Cover <_P ClassScheduling$, as follows.
Given graph $G=(V,E)$, and an integer $k$, we create instance of classScheduling as follows. Classes are represented by nodes. If an edge connects two classes, then their timeslots are compatible. For every node we'll save a variable to assign a room. If we are able to create a vertex cover of size $\le k$ we will be able to assign a room to every compatbile class.