# Propositional Logic
### Knowledge Base
For the Wumpus world (Omitting gold for simplicity):
- $p_{x,y}$ pit in x,y
- $w_{x,y}$ Wumpus in x,y
- $b_{x,y}$ Breeze in x,y
- $s_{x,y}$ Stench in x,y
- $I_{x,y}$ Agent in x,y
for $x,y \in \{1,2,3,4\}$ 
 We'll have the following constraints:
 1. Wumpus in exactly one square
	 - $\bigvee w_{x,y} \in \{1,2,3,4\}$ (Wumpus in at least one square)
	 - $\neg(w_{x,y} \wedge w_{x\prime, y\prime}) \ \forall (x,y) \neq (x\prime, y\prime)$ (Wumpus in at most one square)
2. Square $(x,y)$ has stench iff Wumpus in adjacent square
	- $s_{x,y} \leftrightarrow w_{x+1, y} \vee w_{x-1, y} \vee w_{x, y+1} \vee w_{x, y-1}$ 
3. Square $(x,y)$ has breeze if pit in adjacent square, and there is no pit in the first block
	-  $b_{x,y} \leftrightarrow p_{x+1, y} \vee p_{x-1, y} \vee p_{x, y+1} \vee p_{x, y-1}$ 
	- $\neg p_{1,1}$
An interpretation may not satisfy all constraints.

While not knowing the map, we can construct a model considering the constraint of the things observed, concatenated in an _and_ statement. Any interpretation may be valid as long as they satisfy the observations.
It's a satisfiability problem (SAT). Done countless times already.
### Propositional Satisfiability
A propositional formula $\varphi$ is said to be _satisfiable_ if there exists an interpretation I such that $I \models \varphi$
For example:
- $\neg(a \vee b) \rightarrow c$ is satisfiable (For example: $I = \{c\}$).
- $a \wedge (a \rightarrow b) \wedge (b \rightarrow \neg a)$ is not satisfiable.
### Propositional Validity
A propositional formula $\varphi$ is said to be valid if $I \models \varphi$ for all interpretations I
for example:
- $(a \rightarrow b) \wedge (b \rightarrow \neg a)$ is valid.
- $(a\rightarrow b)$ is satisfiable but is not valid.
A valid formula is also called a *tautology*.
### Logical Implication
We might want to know if the subset of all possible interpretations given a propositional formula imply something. For example, given the path we've discovered, we may want to know if a Wumpus is for sure in a given box.
Formula $\varphi$ logically implies $\gamma$ ($\varphi \models \gamma$), if for every $I$ s.t. $I \models \varphi$, it is the case that $I \models \varphi$.
### Logical Equivalence
We might be interested in checking whetever two formulas have the same meaning. $\varphi, \gamma$ are logically equivalent if every interpretation $I$ is such that $I \models \varphi$ if and only if $I \models \gamma$.
## Expansion Rules
$\alpha$-rules -  Deterministic Rules, in conjunction, we don't need to choose any path
- When we use $\alpha$-rule to expand, we may want to expand one of the two at first, but we will need to expand the other too, at one point.

$\beta$-rules - Splitting Rules, done in the disjunctions, we need to non-deterministically choose a path

Logical rules, once again. Too lazy to write them here, please write them in last notes.
The goal of expansion rules is to create a situation in which are symbols are cancelled and/or simplified, so that the formula creates a raw literal.
When we expand a rule we'll need to expand it on the leaves underneath it.
# Tableaux
>A tableaux is a tree-like structure, where root is the original formula $\varphi$.
>we want to check for satisfiability, and internal nodes contain formulas over propositions of $\varphi$. All levels are labelled with X or O.

Once construction is complete, we'll say that _$\varphi$ is satisfiable if and only if there exist some leaf labelled with O_

![[Pasted image 20250604093115.png]]
_in the image above we first expanded $(P \vee Q)$ using the $\beta$ rule, and we got down to literals. When we expanded $\neg(P \wedge Q) = (\neg P \vee \neg Q$) using again the $\beta$ rule on the bottom of the two nodes. _


Tableaux is constructed proceeding top-down with the goal of reducing to literals. 
We start with root labelled with formula to check and at every step one node is expanded (only once).
If a path contains contradictory formulas, then add leaf with X. Once all nodes along a path have been expanded, path to no contradiction terminate with O. Once expanded, we can check for contradictions so that we can see if a given formula is satisfiable or not by checking if there exist at least one leaf O.
### Refutation Principle
Given $\Gamma = \{\varphi_1, ..., \varphi_m\}$ with $m$ being a finite number, Gamma models phi, $\Gamma \models \varphi$, if and only if $\Gamma \cup \{\neg \varphi\}$ is un-satisfiable.

If $\Gamma=\{\varphi_1,...,\varphi_m\}$ is finite, this is equivalent to saying that $\Gamma \models \varphi$ if and only if $\varphi_1 \wedge ... \wedge \varphi_m \wedge \neg \varphi$ is un-satisfiable. This is also a logical implication.

# DPLL procedure for SAT
## Decision Procedures - Automated reasoning

- **model checking** : $I \models \phi$ Does the interpretation satisfy $\phi$.
- **satisfiability**: $\exists^? I:I \models \phi$ Is there a model of $\phi$?
- **logical implication**: $\Gamma \models^? \phi$ is every model of the set of formulas $\Gamma$ a model of $\phi$ as well? Check un-satisfiability of $\Gamma \cup \{\neg \phi\}$
Logical implication directly implies satisfiability!
Satisfiability also implies to have logical inference, which asks for a proof. Satisfiability has been resolved with the Tableaux problem, but today we'll see the main one used in algorithms.
# DPLL
## Conjunctive Normal Form (CNF)
This is the form that DPLL asks as an input.

>It's a conjunction of clauses, which means that the disjunctions of literals (or-connected) are conjunct together (and-connected).


$(p \vee \neg q \vee r) \wedge (q \vee r) \wedge (\neg p \vee \neg q) \wedge r$

A formula in **CNF** has the following shape:
$$\bigwedge_{i=1}^m(\bigvee_{j=1}^{n_j} l_{i,j})$$
The issue now is to see if we can _transform a generic formula into an equivalent CNF one_. Yes! But it requires at worst to check all possible interpretations (and here the $NP-complete$ problem)
### Equi-satisfiability
We'll relax equivalency with equi-satisfiablity:
>Given two formulas $\phi$ and $\phi'$, they are equi-satisfiable iff:
>$\phi$ is satisfiable if and only if $\phi'$ is satisfiable

This can be constructed in poly-time! Better than equivalency transformations. Equi-satisfiability is not equivalency, especially when having more literals in one of them (e.g. $(a \vee b)\wedge c$ is equi-satisfiable to $a \vee \neg a$, but they are not equivalent).
## Tseitin's Transformation
>It converts any propositional formula $\phi$ into an equi-satisfiable formula $\phi'$ in CNF with only a linear increase in time

for any formula, we can create a $3-CNF$ formula.
The Tseitin transformation $T(\psi)$ of $\psi$ is the conjunction of :
- $n_\psi$, with $n_\psi$ being $\psi$ when it is a literal, and being a new propositional letter if not.
- CNF($q \equiv \neg n_\psi$ ) for every non-literal subformula of the form $\neg \psi$ having name $q$
- CNF($q \equiv (n_{\psi_1} \square n_{\psi_2})$)  for every subformula having name q, where $\square \in \{\vee, \wedge, \implies, \equiv\}$ 
### Example
$\psi = (p \vee q) \rightarrow (p \wedge \neg r)$ 
$x_1 = \psi$, $x_2 = (p \vee q)$, $x_3 = (p \wedge \neg r)$
we  define then these three parts:
$CNF(x_1 \equiv x_2 \rightarrow x_3) = \phi_1: (\neg x_1 \vee \neg x_2 \vee x_3) \wedge (x_2 \vee x_1) \wedge (\neg x_3 \vee x_1)$ 
$CNF(x_2 \equiv (p \vee q)) = \phi_2 : (\neg x_2 \vee p \vee q) \wedge (\neg p \vee x_2) \wedge (\neg q \vee x_2)$ 
$CNF(X_3 \equiv (p \wedge \neg r)) =  \phi_3 : (\neg x_3 \vee p) \wedge (\neg x_3 \vee \neg r) \wedge (\neg p \vee r \vee x_3)$

We now can say that $T(\psi) = x_1 \wedge \phi_1 \wedge \phi_2 \wedge \phi_3$ 
## Clauses properties
- If a clause $C$ is obtained by _reordering the literals_ of a clause $C'$, then $C'$ and $C$ are equivalent. (Commutative property)
- If a clause contains _more than one occurrence of the same literal_ then it's equivalent to the clause obtained by deleting all but one such occurrence (Associative property)
- We can represent the clause as a _set of literals_, leaving disjunction implicit.
## CNF properties
- Clause order doesn't matter (Commutative)
-  If a CNF formula contains _more than one occurrence of the same clause_ then it's equivalent to the CNF formula obtained by deleting all but one such occurrence (Associative property)
- A CNF formula can be represented as a set of clauses, which in turn can be seen as a set of literals.
---
Let $\psi = \{C_1, ..., C_n\}$:
- $I \models \psi$ if and only if $I \models C_i$ for all $i = 1,..,n$
- $I \models C_i$ if and only if for some $l \in C, I \models l$
To check that $I$ is an interpretation for $\psi$, we don't necessarily need to know the truth values that I assigns to all literals appearing in $\psi$. Others may not need to be defined to still have $I$ to be an interpretation.

>A partial interpretation is a partial function that associates to some propositional variables of the alphabet $P$ a truth value (either true or false) and can be undefined for the others.

The idea is to apply simplifications to a given formula.
For any CNF formula $\phi$ and a literal $\gamma$, then $\phi|_\gamma$ stands for the formula obtained from $\phi$ by:
- removeing all clauses containing the literal $\gamma$
- removing the literals $\neg \gamma$ in all remaining clauses.
## Unit Propagation
>A **Unit clause** is a clause containing a single literal

If the CNF formula contains a unit clause, then that literal must be evaluated to true. We have a forced choice to do. Once we have evaluated the unit clause to true, ==we can remove the literal in the unit clause from every clause in the CNF formula where the literal is not satisfied, and we can remove every other clause that contains the literal==.
```
UnitPropagation({{p}, {!p, !q}, {!q, r}}, emptyset)
I(p) = true
	-> {{!q}, {!q, r}}
I(q) =  false
	-> {}
```
The procedure for the run above returns $(\{\}, I = \{p\})$.

In the case in which `UnitPropagation` does not have unit clauses we may need to use splitting rules and evaluate both formulas, creating for it a derivation tree.
### Algorithm
Unit Propagation is a sub-procedure which takes the formula as an input and the interpretation of the current sub-formula.
- Given the formula it checks for a unit clause, and if there is it'll extend the Interpretation to satisfy that. From the formula we'll then remove all occurrences of the negated literal of the unit clause, and we'll remove all clauses that contain the literal.
In the case in which we are left with a set of empty clause then our  interpretation satisfies our partial solution; otherwise we need to apply the splitting rule to the clause, by selecting one literal and adding a unit clause of that literal, and running DPLL on that.

```
DPLL(φ, I′)
  (ψ, I) := UnitPropagation(φ, I′);
  if ψ contains {}
    then return ({{}}, ∅)
  elseif ψ = {} 
    then return ({}, I)
  else select a literal λ ∈ C ∈ ψ;
    if DPLL(ψ ∪ {{λ}}, I) = ({}, I′′)
      then return ({}, I′′)
    else 
      return DPLL(ψ ∪ {{¬λ}}, I)
```

DPLL has a time complexity $O(2^m)$, but in most cases it's much faster to build the truth table. 
# First Order Logic (FOL)
It's more powerful and expressive than propositional logic, since it considers attributes and uses $IS-A$ relationships. Everything that concerns propositional logic is finite, while we need a representation that can be of infinite size.

## Objects in FOL
FOL assumes that world is constituted by:
- **Individual Objects**, denoted by *constants* that talk about an objects
	- Mary
	- John
- **Functional means to refer to Objects**, denoted by functions
	- *Italian(fatherOf(Luca))*
- **Properties and relations**, denoted by *predicates*
	- *Person(Mary)*
	- *Person(John)*
	- *Mortal(Mary)*
	- *Siblings(Mary, John)*
- **Quantifiers** that get assigned globally to variables.
	- $\forall x. Person(x) \rightarrow Mortal(x)$
	- $\exists x. Person(x) \rightarrow Mortal(x)$ 

An **Assignment** $\alpha$ for $I$ is a function from the set of variables to $\Delta$. If $\alpha$ is an assignment $I$ then $\alpha[x/d]$ denotes the assignment for $I$ that coincides with $\alpha$ on all the variables but $x$, which is associated to $d$.

A first-order interpretation for the alphabet consisting of *constants*, *functions*, *predicates*is a pair $<\Delta, I>$ :
- $\Delta$ being the interpretation domain, as the set of symbols
- $I$ is a function, called interpretation functions such that:
	- $I(c_1) \in \Delta$
	- $I(f_i) : \Delta^n \rightarrow \Delta$
	- $I(P_i) \subseteq \Delta^n$ 
	In other words, I associates to each constant an element of the domain ∆, to each function symbol f/n a total n-ary function on the domain ∆, and to each predicate symbol Pi an n-ary relation on the domain ∆.
### Free Variables
> A free occurrence of a variable $x$ is an occurrence of $x$ which is not bout to a quantifier.

Def:
- Any occurrence of $x$ in $t_k$ is free in $P(t_1,...,t_k,...,t_n)$
- Any free occurrence of $x$ in $\phi$ or $\psi$ is also free in their logical conjunction
- Any free occurrence of $x$ in $\phi$ is free in $\forall y.\phi$ and $\exists y.\phi$ if $y$ is distinct from $x$

Free variables represent individuals which must be instantiated to make the formula a meaningful proposition.
A variable $x$ is free in $\phi$ (denoted$\phi(x)$) if there is at least a free occurrence of $x$ in $\phi$. 

==Free variables limit from finding satisfiability since they are not assigned==.
### Ground / Open / Closed Formulas
A formula $\phi$ is **ground** if it does not contain any variable. 
A formula is **open** if it contains at least one free variable, **closed** otherwise.
Obviously, all ground formulas are closed. A closed formula is also called sometimes *sentence*, and they ==aren't changed by assignment, since they don't have variables,== so assignment can be omitted.

Interpretations cannot be changed, while assignment can be changed by definition. 
Examples with formulas present at page 30.
## Tableaux Calculus
The Tableaux Calculus is an algorithm solving problem of satisfiability. If a formula in FOL is satisfiable, then there will exist an open branch in the tableaux of this formula. _It may happen that the FOL tableaux is infinite._

The expansion rules for first order semantic tableaux are those for the PL tableaux, but they are extended with the quantifiers.


| Rule          | Formula 1                                   | Formula 2                                      | Explanation                                                        |
| ------------- | ------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------ |
| $\gamma$ rule | $\frac{\forall x.\phi(x)}{\phi(t)}$         | $\frac{\neg \exists x.\phi(x)}{ \neg \phi(t)}$ | Where t is a term free for $x$ in $\phi$                           |
| $\delta$ rule | $\frac{\neg\forall x.\phi(x)}{\neg\phi(t)}$ | $\frac{\exists x.\phi(x)}{\phi(c)}$            | where c is a new constant not previously appearing in the tableaux |
We'll have substitution rules here too. If $\phi(x)$ is a free variable (could be a term or also a function, whatever) and t is a term, we'll use $\phi(t)$ instead of the more precise $\phi[x/t]$ . $\phi[x/t]$ denotes the formula we get by replacing each free occurrence of the variable x in the formula $\phi$ by the term t. This is admitted if t does not contain any variable y such that x occurs in the scope of a quantifier for y (i.e., in the scope of $\forall y$ or $\exists y$).
For example:
- $P(x,y,f(x))[x/a] \longrightarrow P(a, y, f(a))$
- $\exists x.P(x,x) \wedge Q(x)[x/c] \longrightarrow \exists x.P(x,x) \wedge Q(c)$
- $\forall x.P(x, y)[y/f (x)] \longrightarrow$ Not allowed, x is not free
### Universal Quantification Rule
$\displaystyle \frac{\forall x \phi(x)}{\phi(t)}$ , with t being a free variable in x
A term t that occurs in the tableaux denotes an object of the domain, therefore $\phi(t)$ must be true for all terms $t$ that occurs in the tableaux
### Existential Quantification rule
$\displaystyle \frac{\exists x.\phi(x)}{\phi(c)}$ for a new constant c
given the quantifier, we don't know which object holds the property, but we don't know which. For this reason we cannot apply this rule to other terms that appear in the tableaux. Trick is to introduce an unconditioned object, which points to an "unknown" variable. We allow to infer $\phi(c)$ from $\exists x \phi(x)$, where c is fresh.
### Infinite Domain
Differently from propositional logic, in FOL models can be infinite, and so we have an infinite branch in the Tableaux.
==If the formula has such infinite model we can say it's satisfiable, but we can't prove satisfiability with an interpretation.==
Example: ![[Pasted image 20250321100003.png]]
This has infinite representations, since the first tells us that there isn't any interpretation with R having same object, the third is saying that for every object there is an other object associated to the first through R.
The third has transitivity property, but this means that there isn't a single interpretation that satisfy this, and trying to construct one leads to an infinite model interpretation.
### Termination
In contrast to what happens in propositional logic, the tableaux construction is not guaranteed to terminate.
>If the formula $\phi$ that labels the root is unsatisfiable the construction is guaranteed to terminate and the tableau is closed.
>If the formula $\phi$ that labels the root is satisfiable then either the construction is guaranteed to terminate and the tableau is open, or the construction does not terminate.

# Planning
We talked about the deductions based on our observation. ==With planning, we'll perform deterministic actions that change the world and we'll reason on them, to achieve a certain goal.==

> [!Definition]
A **domain** is a representation of the model we are adding in. It's composed of three main parts:
> - **State space**: A state space can consist of finite or infinite states
> - **Actions**: are finite, will be used to move between states
> - **Transition function**: $\delta: S \times A \rightarrow S$. It's the transitional function that transitions from a state to another, given the original state and the action.


# Classical Planning
In classical planning, actions are deterministic. Generalizing we'll have a domain with $n$ possible states, representing all the possible valid configurations.
Actions are (finite) entities that allow the agents to change the world.

These 3 parts ==(state space, action space, transition function) are what defines the domain.==

> [!WARNING]
>In classical planning, effects are always predictable once we do certain actions, and this limits the use cases. (e.g. we cannot model a dice throwing).

The problem consist in a tuple $<D, s_0, G, \alpha>$:
- $D$ = Domain  ($D= <S, A, \delta>$)
- $s_0$ = Initial State
- $G$ = Goal set, containing one or multiple goal states.
- $\alpha : S \rightarrow 2^A$ =  Function that, given a state, returns all of the possible actions from that
## Reachability
Given a tuple $<D, s_0, G, \alpha>$, find a sequence of actions $\pi = (a_1, ... a_l)$ such that:
- $s_{i+1} = \delta(s_i, a_i) \ \forall i = 0, ..., l-1$
- $a_i \in \alpha(s_i-1)$
- $a_l \in G$
If it satisfies the requirements above, $\pi$ is called a (solution) plan for the problem $P$. If we represent states as nodes, and actions as edges, we can model reachability as a path finding problem in graph!
*Uninformed search* is when we don't take advantage on knowledge of the entire domain, we won't get a solution but we'll only talk about existence of the solution 
```
bool Search(D, s_0, G){
	set Marked = {s_0}
	set Frontier = {<eps, s_0>} // open set, <plan,state> pairs
	while Frontier not empty{
		state i = Frontier.pop()
		if i in G{
			return True
		}
		for a in alpha(i){
			j = delta(i, a)
			if j not in Marked{
				Frontier.push(j)
				Marked.push(j)
			}
		}		
	}
	return False
}
```
This is not ideal - The state space becomes incredibly large as we'll record all possible plans, becoming a exponential space. We may consider different extraction policies, maybe by using BFS (which was the one i've implemented first in the algorithm, whoops).ù

We'll create a function that is decisional over the desirability of taking that action $f:S\rightarrow R$, and create a **best-first search**.

```
bool BF-Search(D, s_0, G){
	set Marked = {s_0}
	set Frontier = {s_0} // open set, contains set of states while we search
	while Frontier not empty{
		<path, state> <p,s> = extract pair s.t. max{f( <path, state> in Frontier)}
		if i in G{
			return <p,s>
		}
		for a in alpha(i){
			j = delta(i, a)
			if j not in Marked{
				Frontier.push(<p°a, j>)
				Marked.push(j)
			}
		}		
	}
	return False
} 
```
What to use as function $f$? -> **Manhattan Distance**: Sums of horizontal and vertical distance to the goal. We may use this to expand nodes that have shorter Manhattan distance (in certain situations it may not be the best one, think of maze).

### Informed Search
Apriori we can use some optimizations so that we don't consider redundant/useless paths (like loops). We are _restricting_ the search, by also considering its costs.
==**Informed/Heuristic Search** uses a heuristic function==, which easily computes the distance from the goal. In our simplified Wumpus, a heuristic function may be the distance of horizontal/vertical movements needed to go to the goal. 

Evaluation function uses $f(n) = g(n) + h(n)$, where
- $g(n)$ is the actual cost of reaching $n$
- $h(n)$ is an _estimate_ of cost to reach the goal from $n$ 

|                                                                                                                                                                                                                                                                                                                                                                                                                 |                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| While expanding the tree, we may see that we get back to a state previously discovered. Being there with a longer path, we'll see that $g(s)$ has a higher value than what has been previously calculated, so we discard it (loop!)<br>The process is called **pruning** the tree, making it more efficient.<br><br>We add the cost to best-first search to consider this and to check what nodes to disregard. | ![[Pasted image 20250403140502.png\|400]] |
> A heuristic function h is __admissible__ if it does not overestimate the cost of reaching a solution for all states. If A* uses an admissible heuristic function, then it is OPTIMAL.

We modify the Best-first search by extracting the $<p,s>$ which has the minimal $\{g(p) + h(s)\}$ with $g(p)$ the cost of the plan given the number of nodes in the plan itself. We add a node to the Frontier iff it hasn't been seen before or if the cost is lower than what it has been reached before (by checking Marked that now contains the node and the cost).
## Heuristic function
First step is finding when an admissible Heuristic function is "good". Since the function returns an estimate which is never overestimated, if we have two functions $h_1, h_2$ we should choose the one which returns an estimation closer to the actual distance - for example $h_1(s) < h_2(s) < d(s,g)$ (and so the one which has a bigger value), since it provides a better estimation. In this case we say that $h_2$ **dominates** $h_1$.
# Planning Domain Definition Language
**Also shortened to PDDL**. Compact way to write deterministic planning. Among the first planning language, coming from *STRIPS: Standard Research Institute Planning System*. We'll first see ==STRIPS-based PDDL==, then ADL (==Action== Description Language)-based PDDL. They are not cross-compatible.
### Presented with examples:
Blocks Worlds example: We are given a set of boxes $(A,B,C)$.They can be layed down on a table flat or they can be stacked. A robotic arm may pick boxes and move them around in the XY axys, doing actions: `Move`, `MoveToTable`. We wil model this domain using PDDL:
$D = <S, A, \delta>$
by creating our sets of states, which are described by predicates, the actions and the transition function which is defined in the effect.
A *State* will then be the sets of all possible predicates valid for a specific moment in time
## Domain File
```PDDL
(define (domain BlocksWorld)
	(:requirements :strips :negative-preconditions) ; This is a comment
	
	(:predicates
		(on ?b1 ?b2 - object)
		(onTable ?b - object)
		(clear ?b) ; not necessary to write type if is `object`
	) ; This allows us to represent the States
	
	(:action moveFromTable
		:parameters (?b1 ?b2)
		:precondition (and (clear ?b1) (clear ?b2) (ontable ?b1))
		:effect (and (on ?b1 ?b2) (not (onTable ?b1)) (not (clear ?b2))) ; We
				; have negative-precondition 
				; to add the negative precondition
	)
	(:action moveToTable
		:parameters (?b1 ?b2)
		:precondition (and clear(?b1) (on ?b1 ?b2))
		:effect ( and(not (on ?b1 ?b2)) (onTable ?b1) (clear ?b2))
	)
	(:action moveFromBlock
	:parameters (?b1 ?b2 ?b3)
	:precondition (and (clear ?b1) (clear ?b3) (on ?b1 ?b2))
	:effect (and (not (on ?b1 ?b2)) (clear ?b2) (on ?b1 ?b3) (not( clear ?b3)))
	)
)
```
When defining a domain, we need to be careful about a set of problems that can arise, some of them solved by PDDL:
- **Qualification Problem**: Specifying the condition for which an action can be executed (solved with `precondition`)
- **Frame Problem**: Specifying what changes in a system. To deal with this, we'll define only what changes, and if it isn't mentioned it didn't change.
- **Ramification Problem**: Concerned with the indirect consequences of an action. Strictly connected to the frame problem.
## Problem File
Concerns with the initial state and the goal state
```
(define (problem BlocksWorldProblem)
	(:domain BlocksWorld)
	(:objects A B C)
	(:init (onTable A)
		   (onTable B)
		   (onTable C)
		   (clear A)
		   (clear B)
		   (clear C)
	) ; we are working with the closed world assumption (like DBs) where
	  ; everything that isn't mentioned is automatically false
	
	(:goal (and (on B C)
				(on A C)
		)
	)
)
```
Given these two files, we can create a *Transition system*. This will be automatically created by the PDDL Planner.
##### Example

|                               $s_0$ ->                               |   -> Action ->    |                                              -> $s_1$                                              |
| :------------------------------------------------------------------: | :---------------: | :------------------------------------------------------------------------------------------------: |
| ontable a<br>ontable b<br>ontable c<br>clear a<br>clear b<br>clear c | moveFromTable a b | -- removed DEL LIST<br>ontable b<br>ontable c<br>clear a<br>clear c<br>-- added ADD LIST<br>on a b |
For _any states_ in $s \in S$ we will:
1. Consider all actions $a$
2. Check the precondition and keep actions that satisfy them
3. For all remaining actions compute the successor state $s'$
Transition systems can be expanded online, and not necessarily precomputed!

As we can see, `strips` version of PDDL doesn't contain any quantifier, and it's more closely related to propositional logic. 
## ADL extension
```
(define (domain BlocksWorld)
	(:requirements :adl) ; quantifiers and negated preconditions
	(:types block)
	(:predicates
		(ontable ?b - block)
		(on ?a ?b - block)
	)
	(:action move
		:parameters (?b1 ?b2 - block)
		:precondition (and    ; calculated before applying action
			(forall (?b - block) (not (on b ?b1)))
			(forall (?b - block) (not (on b ?b2)))
		)
		:effect (and          ; calculated after applying action
			(on ?b1 ?b2)
			(forall(?b - block) (when(on ?b1 ?b) (not(on ?b1 ?b)))
								; conditional effect!
			when(ontable ?b1) (not(ontable ?b1))
		)
	)
)
```
With ADL we have way more flexibility.

| Feature                      | STRIPS                          | ADL (Action Description Language)         |
|:---------------------------:|:--------------------------------:|:-----------------------------------------:|
| **Preconditions**           | Conjunction of literals only     | Allows conjunctions, disjunctions, and quantifiers |
| **Effects**                 | Add/delete lists (simple effects)| Allows conditional effects and quantifiers |
| **Expressiveness**          | Limited                          | More expressive and closer to first-order logic |
| **Negative Preconditions**  | Not supported                    | Supported                                 |
| **Usage Complexity**        | Simpler to parse and plan with   | More complex but more flexible            |
## Fully Observable Nondeterministic (FOND) Planning
In FOND planning, for a given state and an action we have many possible outcome states. Observation of the action outcome is necessary. Formalizing, we have $\delta:S \times A \rightarrow 2^S$
Planning becomes more challenging, since the outcome of the $\delta$ function is nondeterministic.

To do this, we will create a **policy function** $\pi: S \rightarrow A$ which tells us for every state what action to do. A policy is a solution if all possible states will get you to the goal states.

We'll have a plan if there is a path in the tree which contains a goal tree (these kinds of trees are called **and-or trees**, for which we'll do an **and-or search**. We may also encounter loops, for which we have to backtrack.

```c
/* 

input:
	- D is the Domain
	- s_0 is the starting state
	- G is the Goal Set
output:
	- Policy / fail
*/

Policy AO-search (D, s_0, G){
	return OR-search(D, s_0, G, eps);
}
```
sigma parameter is the path that we have taken up to the node, so that we can detect loops. At first, delta is empty (so is called epsilon).
```c
Policy OR-search(D, s, G, sigma){
	if (s in G)
		return pi_0; // Empty policy
	if (s occurs in sigma)
		return fail;
	for every action a in alpha(s){
		pi =  AND-search(D, s, a, G, sigma U {s})
		if (pi != fail)
			return pi U {<s,a>};
	}
	return fail;
}
```

```c
Policy AND-search(D, s, a, G, sigma){
	pi = pi_0; // Empty policy
	for every (s' in delta(s, a)){
		pi' = OR-search(D, s', G, sigma);
		if (pi' == fail)
			return fail;
		pi = pi U pi'
	}
}
```

## Non Deterministic Planning in PDDL
**How to represent domain, in a compact way?**
we'll introduce a variant of PDDL such that we can express non-deterministic actions, using the `oneof` key. 
- **oneof**: allows to specify a set of possible effects.
	- `oneof(e1 ... en)`, where each $a_i$ is a deterministic effect. 
	  After executing the action, one and only one effect will be applied, which is not known before the execution.

# Situational Calculus
First-Order Language to specify (deterministic) dynamic domains. Functions are in FOL.
## Sorted language
Feature of situation calculus, which has object sorts (kind of as types).
Object domain can be partitioned into three subsets:
$\Delta = (Objects, Actions, Situations)$
- **Actions**: Represent the actions that can be executed in the domain
- **Situations**: Represent possible world histories
### Actions
We need syntax to denote features: we'll use Action Types, which corresponds to PDDL schemas. $\mathcal{A} = \{A_1/a_1, ...,  A_n/a_n\}$
Example:
- $\mathcal{A} = \{put-on-table/1, pickup-from-table/1, put-on-block/2 ,pick-up/2\}$
$pick-up(b_1, b_2)^I = act_4$
With functions we represent actions terms, and we return actions.
A special predicate `Poss(a,s)` is used to indicate when action $a$ is executable in situation $s$, verifying its preconditions, and returns $True$ or $False$.
### Situations
In the situation calculus, a dynamic world is modeled as progressing through a series of situations as a result of various actions being performed within the world. A **situation** represents a history of action occurrences.
- $s_0$: situation where no action has been performed
From this first situation we can execute actions are have different situations.

$do(a,s)$, where $a$ is an action term (e.g. `put-down(b)`) and `s` is a situation term (e.g. $s_0$ itself), returns another situation that is the result of applying the action $a$ over the situation $s$.

> [!WARNING]
> We will _not_ be talking about states, which they don't exist in Situation Calculus.

$\Sigma$ is the set of constraints, foundational axioms of Situational Calculus.
### Fluents
**fluents** are dynamic predicates where Truth value may change from situations to situations
$Friends(p,s,s_0)$
$\neg Friends(p,s, do(steal(p, Tablet),s_0))$
Non-fluents are predicates which values never change
## Precondition Axioms
Some actions may not be executable in a given situation. The restrictions on the performance of actions are modeled by literals of the form $Poss ( a , s )$ , where $a$ is an action, s $a$ situation, and $Poss$ is a special binary predicate denoting executability of actions.
We will model this with $\leftrightarrow$ relations
Example:
- $Poss(move(x), s) \leftrightarrow \exists y. AgentAt(y,s) \wedge Right(y,x)$
	- This means that it's possible to execute the `move` action, in a given situation, if and only if there exists a fluent AgentAt(y,s) and that there is a non-fluent `right`

The precondition axioms are all taken in the $D_{AP}$ set, with is the Domain of Action Precondition Axioms
### Effect Axioms
Given that an action is possible in a situation, one must specify the effects of that action on the fluents. This is done by the effect axioms. For example:
- For the action $move(x)$ : Given that we already specified the preconditions we need to specify the effect of the action
	- after executing the action, in the successor situation the agent will move to $x:AgentAt(x, s')$. We'll write it ass $\forall s\forall x.AgentAt(x,do(move(x),s))$ . We need tho to check that the Agent is in _only one position_, so we'll need to add another statement to complete this with:
		- $AgentAt(x,do(move(x),s))$
		- $AgentAt(y,s)\wedge x\neq y \rightarrow \neg AgentAt(y, do(move(x), s)$

It is also possible to specify conditional effects, which are effects that depend on the current state.
#### Frame problem
When dealing with effects it's imperative to also deal with the frame problem, and so we ask ourselves how to model every effect, even what is not changing. For example, the objects that the agent has before executing the $move(x)$ action will need to remain in the agent's inventory.
To deal with this we'll write the axioms in **normal form**, where on the right we'll have an atomic formula with only the affected fluent. As an example $a = move(x) \rightarrow AgentAt(x,do(a,s))$ where we have the form $\gamma \rightarrow F(x,do(a,s))$ which will solve the frame problem.  The action should be written as a variable.
#### Explanation
We can describe the following effect
$$
\forall xys. AgentAt(y,s) \wedge x \neq y \implies \neg AgentAt(y,do(move(x),s))
$$
> For every x, y and state s, if the agent is at y and x != y, then the agent, after executing move(x), will not be anymore in position y.

as, writing in a more generalized way
$$
\forall xys. A(y,s) \wedge C(x,y) \implies \neg A(y,do(Act(x),s))
$$
$$
\forall x \forall y \forall s. \neg(A(y,s) \wedge C(x,y)) \implies (a=Act(x) \implies\neg A(y,do(a,s)))
$$
We can drop all parenthesis, since they are all conjuctions
$$
\forall x \forall y \forall s. \neg A(y,s) \vee \neg C(x,y) \vee \neg a=Act(x) \vee \neg A(y,do(a,s))
$$
..and then we associate them using the negation of disjunction rules to get
$$
\forall x \forall y \forall s. \neg (A(y,s) \wedge C(x,y) \wedge a=Act(x)) \vee \neg A(y,do(a,s))
$$
And this is the normal form for the negated effect!
$$
\forall x \forall y \forall s \forall a. A(y,s) \wedge C(x,y) \wedge a=Act(x) \implies \neg A(y,do(a,s))
$$
which, since we don't have the $x$ term in the right-hand part of the formula, we can transform it in an existential quantifier (dropping universal quantifiers)
$$
\exists x( A(y,s) \wedge C(x,y) \wedge a=Act(x)) \implies \neg A(y,do(a,s))
$$
### Explanation Closure axioms
This helps to create SSAs that automatically solve the frame problem, by combining all action and effect axioms. For `move(x)` we will isolate all axioms that affect the fluent.
For example, `AgentAt(x,s)` is affected just by move(x). We'll collect these two axioms with the positive and negative form:
- $\exists y. \gamma^+(x,y,a,s) \rightarrow  F(x,do(a,s)$
- $\exists y. \gamma^-(x,y,a,s) \rightarrow  \neg F(x,do(a,s)$
Getting back to te example, for `AgentAt(x)` we have:
1. $a = move(x) \rightarrow AgentAt(x,do(a,s))$
2. $\exists x. a= move(y)AgentAt(x,s)\wedge x\neq y \rightarrow \neg AgentAt(x, do(a, s)$
3. $a = exit() \wedge AgentAt(x,s) \rightarrow \neg AgentAt(x,do(a,s))$
Assuming we are observing the following situations
- $\neg AgentAt(x) \wedge AgentAt(x,do(a,s))$ ==We know that the action $a$ must be $move(x)$, since there is **No other action that affects AgentAt**==. ($\rightarrow a = move(x)$)
- $AgentAt(x,s) \wedge \neg AgentAt(x, do(a,s))$ This could be happening for two different actions, since they have, and they both can be happening at the same time. We are explaining why we got into this situation. ($\rightarrow \gamma_1^-(x,y,a,s) \vee \gamma_2^-(x,a,s)$)
These kinds of axioms are called **Explanation Closure Axioms**

We are basically explaining out what are the actions that can justify a given situation, and by doing this we are writing out what hanges and what doesn't.
## Successor State Axioms
to get into Successor State Action we have to make an assumption. We assume that:
- Axioms satisfy the integrity conditions, and so there are no two axioms that contraddict each other. So $A(x_1, ..., x_n) = A(y_1,...,yn) \implies x_1 = y+1 \wedge ... \wedge x_n = y_n$
- Axioms need to have unique names

The successor state axioms "solve" the frame problem in the situation calculus. According to this solution, the designer must enumerate as effect axioms all the ways in which the value of a particular fluent can be changed, *"explaining"* how the fluents could've been changed by a set of actions. (*regards the Explanation closure axiom*).

Given a list of normalized effect axioms:
- $\exists \overrightarrow{y_1}. \gamma_1^+(\overrightarrow{x}, \overrightarrow{y_1},a,s) \rightarrow F(\overrightarrow{x}, do(a,s))$  
-  $\exists \overrightarrow{y_2}. \gamma_2^+(\overrightarrow{x}, \overrightarrow{y_2},a,s) \rightarrow F(\overrightarrow{x}, do(a,s))$  
- ...
-  $\exists \overrightarrow{y_m}. \gamma_m^-(\overrightarrow{x}, \overrightarrow{y_m},a,s) \rightarrow F(\overrightarrow{x}, do(a,s))$  
We can create SSAs for the fluent F like:
- $F(\overrightarrow{x}, do(a,s)) \leftrightarrow (\bigvee_i \exists \overrightarrow{y_i}. \gamma_i^+(\overrightarrow{x}, \overrightarrow{y_i},a,s)) \vee (F(\overrightarrow{x},s) \wedge \neg(\bigvee_j \exists \overrightarrow{y_j}. \gamma_j^-(\overrightarrow{x}, \overrightarrow{y_j},a,s)))$

This basically means "The fluent $F$ would only be true over the execution of action $a$ if and only if performing $a$ in $s$ would make it true, or it is true in situation $s$ and performing $a$ in $s$ would not make it false." ==This **solves the frame problem**, since it specifies both when F changes and also when it doesn't.==

---
# Concluding - Basic Action Theory
For BAT we need to specify the domain.
The domain is based as $D=\Sigma \cup D_{UNA} \cup D_{s_0} \cup D_{AP} \cup D_{SSA}$ , where
- $\Sigma$ : Foundational axioms of SItuational Calculus
- $D_{UNA}$ : Unique Names for Actions
- $D_{s_0}$ : Description of Initial Situation (Unique)
- $D_{AP}$ : Action Precondition Axioms (character `Poss(a,s)`)
- $D_{SSA}$ : Successor State Axioms (Specifies how axioms change the state of the domain)
### Legality Task
GIven these tools we can evaluate the **Legality (or executability) task**: Given a sequence of actions $\rho = a_1, ..., a_n$, check whether every action in the sequence is executable, through the Action Precondition axioms
### Projection Task
Given a sequence of actions $\rho = a_1, ..., a_n$, and a formula $\phi$ (which must talk about a state of situation $s$) check whether $D \models \phi (do(a_n, do(a_{n-1}, ...,do(a_1, s_0))))$, that is..check whether $\phi$ holds in the situation $s_n$ resulting from executing $\rho$ starting at $s_0$.
# Regression
Way to transform a formula of future situation into a formula about the initial situation.
For example, the following formula $AgentAt(B, do(move(C,do(move(B,do(move(A,S_0)))$ can be expressed as a series of actions that will make the agent move $A \rightarrow B \rightarrow C \rightarrow B$, which we know it can't be possible.

We will create that formula as $\phi(B,s_3)$ and we'll regress it $R[\phi(B,s_3)] = \phi'(..., s_0)$. Now $\phi'$ can be evaluated on the first state ($D\models \phi'$) This is thanks to the **Regression Operator**, which is defined recursively:
- If $\phi$ is a situation independet atom, which mentions a non-fluent, then $R[\phi] = \phi$
- If $\phi$ is a (relational) fluent of the form $F(x, s_0)$ then $R[\phi] = \phi$
- If $\phi$ has the form $Poss(A(t), \sigma)$ with associated precondition axiom $Poss(A(t), s)\leftrightarrow \pi_A(t,s)$, and with $\sigma$ the situation term $do(A(x_a),do(...,s_0))$ then  $R[\phi] = R[\pi_A(t, \sigma)]$. 
	For example: 
	- $\phi = Poss(move(B), do(drop(), s_0))$ 
	- $\sigma = do(drop(), s_0)$ with $\pi_A$ being $\exists y. AgentAt(y,s) \wedge Right(y,x)$
	- $R[\phi]= R[\exists y. AgentAt(y,do(drop(),s_0)) \wedge Right(y,B)]$, which is the right-hand side of the AP axiom
- If $\phi$ is a (relational) atom of the form $F(x, do(\alpha, \sigma))$, with $\alpha$ being action term $(A(x), A(\overrightarrow{t}))$ and $\sigma$ the situation term, then we'll take the SSA $F(\overrightarrow{x},do(a, s)) \leftrightarrow \Phi_F(\overrightarrow{x},a,s)$ (for which we can see we have no "do" action). $R[F(x,do(\alpha,\sigma)] = R[\Phi_F(x,\alpha,\sigma)]$
- If $\phi$ is a combination:
	- If $\phi = \neg \psi$, then $R[\phi] = \neg R[\psi]$ 
	- If $\phi = \exists x. \psi$ then $R[\phi] = \exists x.R[\psi]$
	- if $\phi = \gamma [\vee / \wedge] \psi$ then $R[\phi] = R[\gamma] [\vee / \wedge] R[\psi]$ 
	- If $\phi = \forall x. \psi$ => $\neg \exists x. \neg \psi$  then $R[\phi] = R$

## Regression Theorem
if $\phi$ is a *regressable formula*
$D \models \phi \implies D_{s_0} \cup D_{una} \models R[\phi]$  
This gets rid of every thing about situations, action preconditions and successor state axioms! In fact, we should be able to evaluate if the formula is a representation of a model just by the regression over $s_0$