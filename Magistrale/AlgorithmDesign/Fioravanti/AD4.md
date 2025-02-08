# Exercise Week 4
## Ex 1
- (a) This is a typical case of edge-disjoint paths. We create a node s of source, and we connect it with infinite edges to every populated node $X$. We then create a sink node $t$ such that each safe node in $S$ connects to $t$ with an infinite-capacity edge. We'll then apply for every original edge $E$ a weight of 1. This will guarantee in a connection flow problem that no two escape paths share an edge.
- (b) we have a similar problem as before, but now we want to create the problem of node-disjoint paths. This can be done with a simple procedure:
	- for every node $u$ that is not in $X$ or in $S$ we will create two nodes $v$ and $v\prime$, that we will connect together with an edge with capacity 1.
	- For every edge such that $(w,u)$ we will create an edge $(w, v)$, and for every edge such that $(u, w)$ we will create an edge $(v\prime, w)$.
- (c) a simple case is one that has only one node that connects all nodes in $X$ to all nodes in $S$.
## Ex 2

## Ex 3

## Ex 4
This is a case of bipartite graph (2D-Matching) in which we have $L$ which is the set of injured people and $R$ which are the hospitals. We have an edge $e=(l,r)$ if person $l$ reaches hospital $r$, along with weight $w_e = n/k$  
## Ex 5
