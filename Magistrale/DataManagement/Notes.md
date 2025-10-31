An information repository that integrates and reorganizes data collected from sources of various kind and makes them available for analysis and evaluation, aimed at planning and decision making.

Example: _Sapienza University of Rome_:
- **Day by day operations:
	- transactions dealing with classroom scheduling, lectures, exams, events, professors, etc..
- **Decision support operations:
	- Analysis of trends, average student grades, number of graduated students, etc..

One of the main aims of Data Warehousing is to maintain _separate_ **On-Line Transactional Processing (OLTP)** and **On-Line Analytical Processing (OLAP)**, so that each task has its Data Warehouse to get data from.
# Data Warehousing
The goal of a Data Warehouse (DW) is to deal with OLAPs alone, since it deals with the trend analysis. 

> [!Data Warehousing]
> It's a collection of data that supports decision-making processes and makes them available for OLAP. It allows to do:
> - Subject-oriented analysis. Puts an emphasys on the subjects that will use the DW
> - Integration and consistency. Given the fact that DWs take advantage of multiple data sources it's important to store them in a unified way.
> - Data evolution. It should be possible to do analysis over multiple timeframes
> - Non-volatile and permanent. Data is never deleted, and they should be viewed as read-only databases.

![[Pasted image 20250306120106.png]]
To deal with unification of data, we'll deal with *ETL tools*.
### ETL
ETL processes extract, integrate and clean data from Operational Sources, to eventually fed the data warehouse. In the abstract level, ETL processes produce a single, high-quality and detailed data source, that feed the Data Warehouse. They consist in four phases:
- Extraction
- Cleaning
- Transformation
- Loading
## Multidimensional Data Model
The principle basic foundation for how users see the DW. 
Organization-specific *Facts* that are the subject of the analysis are represented as cubes where:
- Each cell contains a measure (which is the *fact*)
- Each axis represents a dimension of interest for the analysis
- Each dimension can be associated with a **hierarchy** of dimensional attributes _used to aggregate data stored_ in cubes.
![[Pasted image 20250306121716.png]]
This supports also the idea of *hierarchies*, by grouping together different values for the same axys of "similar" attributes. This is possible with **Aggregation**.
## Data Mining
>It's a technique aimed at discovering information hidden in the data, showing "a bigger picture" by analyzing patterns and discovering **inductive rules**. This can be done in multiple ways, like pattern recognition, fuzzy logic, neural networks ...
### Association rules
It can be possible to create **association rules**, which make it possible to determine logical implication rules that exist in databases, that weren't outright present as an integrity constraint.
For example, in a purchasing transaction containing `{shoes}` tends also to contain the transaction of `{socks}`.
By *looking* at the data we discover new association, similarly to a machine learning pattern.
### Clustering
We can also find **clusters** of data in a multidimensional space, in which data behaves in a similar ways. We can use this to, for example, segment customers into categories.

This, given the data discovered through data mining, can lead for example in decision trees and time series analysis
## OLAP
It's the most popular way to get informations stored in a data warehouse. OLAP users are able to start complex analysis sessions, where each outcome is dependendent on the preceeding step, creating a pipeline of some sort.
An *OLAP session* consists of a navigation path that corresponds to an analysis prodcess for facts, accordingto different view points. At every step of the session, an OLAP operator is used, which transforms the last output into a new one.
### Operators
- **Roll-up** operator causes an increase in data aggregation, removing a detail level. It traverses up in the hierarchy by being more generic.
- **slice** reduces the number of cube dimensions after setting one of the dimensions to a specific value
- **dicing** is the more general approach of slicing, by selecting more than one dimensions, or a range for a given one.
- **pivoting** changes the structure of the visualization
- **drill-across** combines data in different cubes to obtain a new cube.
#### Functional Dependency
If $R(A_1, A_2, ..., A_n)$ is a relational schema, a *functional dependency* on R is a statement of the form
$$ A_{i1}, A_{i2},...,A_{ik} \rightarrow A_j$$
such statement is satisfied in an instance r of R if for every tuple $t_1, t_2$ in r: $t_1[A_{i1},A_{i2},...,A_{ik}] =t_2[A_{i1},A_{i2},...,A_{ik}]\rightarrow t_1[A_j] = t_2[A_j]$
==In a hierarchy, what it's lower in the hierarchy _functionally determines_ the higher value in the hierarchy.== We'll have a tuple for every path from leaf to root.
## MOLAP
Uses a non-relational model. Can be more efficient in data warehousing (since it directly models multidimensionality), but it has the downside of having a different system per vendor (most likely closed source).
## ROLAP
Basically we will be implementing OLAP based on the same DBMS strategy. It's motivated by the fact that it's being studied plenty. A specific schema form is needed to represent multidimensional schemas -> Star/Snowflake Schema.

It requires more processing time to perform the OLAP operations, but it supports greater amounts of data.
![[Pasted image 20250313105424.png]]

| store | city | region |
| ----- | ---- | ------ |
| a1    | b5   | c2     |
| a2    | b2   | c1     |
| a3    | b2   | c1     |
| a4    | b1   | c1     |
| a5    | b1   | c1     |

>Q: Is the $h_1$ table used a good representation of our domains in terms of a table?
>A: NO, it's may be better to have separate table and then connecting them with a relation. We may not be interested in the whole attributes of the table. It also slows down the update/addition in the table, since ==we need to respect the functional requirement!==

It may have sense to create that kind of table when the hierarchical information is **static** (table denormalization). ==A Data Warehouse is _mostly static!_== so it may have sense to use the $h_1$ representation.
## Design Methodology
In a general database design model we do:
- Conceptual Design
- ER Schema
- Logical Design
- Relational Schema
We should change the model, since ER schema *does not* model the multidimensional cube. We'll have then:
- Conceptual Design
- __Dimensional Fact Modeling (DFM) schema__
- Logical Design (ROLAP)
- Relational schema
## Dimensional Fact Modelling
![[Pasted image 20250313120141.png|300]]
Conceptual representation of the DFM consist on a set of _fact schemata_. Each one models facts, measures, dimensions and hierarchies.
A DFM schema uses:
- A **fact type** is a concept relevant to decision-making processes. It typically models a set of events taking place within an organization (e.g., sales, shipments, purchases, and complaints, etc.). It is essential that a fact have dynamic properties or evolve in some way over time.
- A **measure** is a numerical property of a fact and describes a quantitative fact aspect that is relevant to analysis (e.g., each sale is measured by the number of units sold, the unit price, and the total receipts). It's unit/s by which a fact is measured.
- A **dimension** is a fact property with a finite domain and describes an analysis coordinate of the fact (typical dimensions for the sales fact are products, stores, and dates).
#### Basic Constructs
- **Dimensional attributes** are dimensions and all of other possible attribues that describe them. For example, when we talk about a _product_ we may describe it by it's _type_, _dimension_, _category_ etc.. 
- A **Hierarchy** is a directed tree whose nodes are dimensional attributes, which model many-to-one associations between dimensional attributes.
- A **Descriptive attribute** is functionally determined by a dimensional attribute of a hierarchy and specifies a property of it. They usually don't add useful levels of aggregations.
- A **Cross-dimensional attribute** is a descriptive attribute whose value is defined by a combination of two or more dimensional attributes, even from different hierarchies.
- We can have *optional attributes*, maked with `*` in the case of measurements and `|` in case of optional arcs between descriptive attributes. We can also have optional dimensions, by using the same `|` of arcs.
#### Coverage
A coverage can be specified on two or more arcs that exit the same dimensional attribute A. It can be:
- *total*: Every value of A is associated to a value for at least one of the child attributes of A
- *partial*: There are values for A for which all children are undefined
- *disjoint*: Every value of A is associated to a value for at most one of the child attributes of A
- *overlapping*: Values of A exist linking to values of two or more children.
#### Convergence
Is an integrity constraint, which asks that a particular attribute pointed by a -> is the same in both the arcs the two attributes that are on the tail of the arrow.
#### Shared Hierarchies
We may want to avoid repeating the same portion of hierarchies in a fact schema, that are the same in the two. It's drawn with $\odot$ 
#### Multiple Arcs
we may want also to model a many-to-many relations between dimensional attributes, instead of many-to-one. This is done with a double-lined arc.
### Integrity Constraints in DFM
One can always add integrity constraints as separate sentences added to graphical implementation. It's possible to add sentences to the DFM to represent this.
## Modelling DFM onto ROLAP
### Star Schema
Most basic one. It's constituted by 
- A set of relations $DT_1, ..., DT_n$ called **dimension tables**. Where each one corresponds to a dimension. Every $DT_i$ features a primary key and a set of attributes
- A **fact table** referencing all dimension table. A FT primary key is the composition of the set of foreign keys $k_1,...,k_n$ referencing dimension tables.
We'll use *surrogate keys* that use a unique identifier for every tuple in the dimension table.
![[Pasted image 20250320160128.png|600]]
![[Pasted image 20250320161632.png|600]]
As in the case of DFM, one can always add integrity constraints as separate sentences added to the graphical representation. By default, all attributes are non-null, but we can use asterisk to model the appearance of null values.
#### Some comments
- Dimensional tables are completely denormalized, which means that a join is sufficient to obtain all data connected to a certain dimension, but we'll need to have high redundancy in the data
- Only fact tables contain tuples, at the chosen aggregation level. If we want to have finegrained details we may have very big fact tables!
### Snowflake Schema
The other approach of representation, based on fractals. It's the *normalized* schema of the relational OLAP.
![[Pasted image 20250320170422.png|600]]
They are especially useful on cross-dimensional attributes, so that we don't repeat values multiple times for different dimensions, and also shared hierarchies so that we can snowflake the schema on the first shared attribute, and multiple arcs.

>[!Notes]
>Here starts the actually important part
# Database Buffer
At the physical level, a d ata base is a set of database files, where each file is constituted by a set of pages, stored in physical blocks of data. The database buffer is what makes the database access its files, since the DBMS cannot directly talk to secondary storage, and to do query on a DB we first need to load the pages in memory. The size of a block (and therefore of a page) is exactly the size of the portion of storage that can be transferred from secondary storage to main memory, and back from main memory to the secondary storage.

![[Pasted image 20250424101057.png]]The buffer manager uses the following primitive operation
- **Fix**: Loads a page in memory. Function invoked when we need a page from secondary storage to the buffer. For each frame F in the buffer, the manager maintains :
	- Information about which page it contains, through the **Page table**
	- **pin-count(F)**: stores how many transactions are using the page contained in F
	- **dirty(F)**: tells if the contaent in the page has been modified from the last load
	Using a replacement policy (find LRU frame with `pin-count(F) = 0`, queue or fail if else), if a requested page isn't in the buffer we find a new frame that can host our requested page. If `dirty(F) =  true` it stores the changed value of the page then the changes are written in secondary storage, then puts P into that frame F.
- **Unfix**: Releases a page
- **Use**: Registers the fact that we want to modify a page. Writes the `dirty` bit to 1, and adds a unit to `pin-count`.
- **Force**: synchronous transfer to secondary storage. All active pages of a transaction are written in secondary storage when the transaction commits
- **Flush**: asynchronous transfer to secondary storage. The active pages of a transaction that has committed are written asynchronously in secondary storage through the flush operation. Generally more efficient.
# Transactions
A transaction models the execution of a software procedure constituted by a set of instructions that in particular may read from and write on a databased, and that forms as single logical unit. Usually we have a `begin` and `end` instruction, so that a transaction creates a **single atomic operation**.
A transaction must support ACID properties:
- **Atomicity**: For each transaction execution, either all or none of the action have their effect.
- **Consistency**: each transaction executed brings a database in a correct state (no violation of integrity constraint).
- **Isolation**: each transaction execution is independently of any other concurrent transaction executions.
- **Durability**: if the transaction execution succeeds, then the effects are registered permanently in the database.
## Concurrency
The throughput of a system is the number of transactions per second (tps) accepted by the system. Generally, we want a DBMS to be approximately *1.000 / 10.000 tps*, and so the system should support a high degree of concurrency among the transactions that are executed.
Even if single transactions enjoy the ACID property, we need to make sure that even concurrent ones do. This is possible by applying scheduling techniques, to ensure that there aren't any *anomalies* that could break ACID.
## Schedule
Given a set of transactions, a sequence S of actions of such transactions respecting the order within each transaction is called a schedule on the set of transaction, or simply a **schedule**.
A partial schedule is a prefix of a total schedule. 
A (total) schedule S is called serial if the actions of each transaction in S come before every action of a different transactionso there is *no interleaving*. A schedule S is *serializable* if there exists a serial schedule on S' **equivalent** on S. (kind of linearizability in dependable distributed systems). Two schedules S1 and S2 are said to be **equivalent**  if, for each database D, the execution of S1 starting from D produces the same outcome as the S2 starting from the same D.
# Serializability
Generally, a schedule S on {T1,T2,…,Tn} is serializable if there exists a serial
schedule on {T1,T2,…,Tn} that is “equivalent” to S. It's difficult to express equivalence in this case, since we would need to formally prove that for _every_ input, the output is the same in both schedules.
### Anomalies
We want to classify the patterns that make a schedule non-serializable, and we call them *anomalies*. There are 4 anomalies for which we'll discuss:
1. **Reading temporary data**: a transaction is trying to read data that another transaction is working on but has not finished with it.
2. **Update loss**: We may be losing some transactions for interleaved execution
3. **Unrepeatable read**: Happens if two consecutive reads are executed of the same data on the same transaction
4. **Ghost update**: a ghost process changed data, has to do with integrity constraint. Even though the single units are not breaking integrity, the concurrency doesn't
We can create a decidability algorithm, if we use just Database operations for all of our schedule. ==We'll drop all non-database actions for this reason (`read`, `write`, `commit`, `rollback`), and for this reason we will drop local variables, since otherwise the problem is non-decidable (and thus, we aren't even able to solve a problem we don't know how to define).==
We will then categorize the scheduler on the basis of the type of serializability that it can achieve.
#### Assumptions
To make the next types of serializability more sensical, we will need to do some assumptions:
- No transaction reads or writes the same element twice (unrepeatable read)
- No transaction reads an element previously written (update loss)
- No transaction executes the rollback command
## View Serializability
Weakening notion of serializability, that makes it decidable.
Preliminary definitions:
- In a schedule S, we say that ri(x) READS-FROM wj(x) if wj(x) preceeds ri(x) in S, and there is no action of type wk(x) between wj(x) and ri(x). The READS-FROM relation associated to S is 
	- $\displaystyle READS-FROMS = \{\ <r_i(x),w_j(x)> | r_i(x)\ READS-FROM\ w_j(x)\ \}$
-  In a schedule S, we say that wi(x) is a FINAL-WRITE if wi(x) is the last write action on x in S. The FINAL-WRITE set associated to S is 
	- $\displaystyle FINAL-WRITES = \{ w_i(x) | w_i(x)\ is \ the \ last\ write\ action\ on\ x\ in\ S \}$
This gives us a decidable way to check for equivalence for every schewdule
Let S1 and S2 be two total schedules on the same transactions. Then S1 is **view-equivalent** to S2 if S1 and S2 have the same READS-FROM relation, and the same FINAL-WRITE set

A total schedule S is **view-serializable** if there exists a **serial** schedule S' that is view-equivalent to S.
It's still an NP-Complete problem, and we don't know how to check view-serializability if not by checking everything.
## Conflict Serializability
We'll introduce the notion of **conflict** of actions, whenever two actions belong to different transactions, they operate on the same element, and at least one of them is a write actions.

Given a sequence S of actions, we can build set of **conflict relation** of S. $conf(S) = \{<p,q> |\ p,q\ \text{are conflicting and p preceeds q in S}\}$ 
Given a conflict set, we can define the commutativity rule for a sequence S, if p,q are adiacent actions in S belonging to different transactions, and they are such that <p,q> is not in conf(S), then the sequence p,q can be replaced by the sequence q,p (in other words, p and q can be swapped), in which we resolve the conflicts. 

Two schedules are _conflict equivalent_ if $S_1 \rightarrow S_2$, which means that $S_1$ can be transformed into $S_2$ through a sequence of applications of the commutativity rule, based on the fact that the two actions exchanged are not in $conf(S_1)$.
If $S \rightarrow S^\prime$ and $S^\prime$ is a serial schedule, then $S$ is conflict-serializable

**Theorem**: Two schedules s1 and s2 are conflict-equivalent if and only if conf(S1) = conf(S2) i.e. there are no actions ai of Ti and bj of Tj such that:
- ai and bj are conflicting
- the mutual position of the two actions in S1 is different from their mutual position in S2
This removes the swapping part, which implies we can check conflict-equivalence in polynomial time.

Given a schedule S on {T1,…,Tn}, the precedence graph P(S) associated
to S is defined as follows:
- the nodes of P(S) are the transactions {T1,…, Tn} of S
- the edges E of P(S) are as follows: the edge Ti -> Tj is in E if and only if there exists two actions Pi(A), Qj(A) of different transactions Ti and Tj in S operating on the same object A such that:
	- Pi(A) appears before Qj(A) in S
	- at least one between Pi(A) and Qj(A) is a write operation
**Theorem (conflict-serializability)** A schedule S is conflict-serializable if and only if the precedence graph P(S) associated to S is acyclic.
### Conflict-serializability is not enough
System cannot use conflict-serializability, because the graph may be too big and the burden of control mechanism would be too big.
In practice, however, the “transaction and concurrency control manager” must provide an algorithm (also called protocol) for concurrency control. Such an algorithm corresponds to the method implememented in the scheduler, one of the basic modules of the concurrency control manager. The **scheduler** outputs a schedule which is serializable and prevents conflicts.
We'll still create schedulers that produce conflict-serializable schedules.
To do this, the scheduler will be able to **Block scheduled transactions**, to then resume later.
For a scheduler s, ==Gen(s) denotes the set of all schedules S such that there is an input schedule S' such that S is the output produced by s while processing S'==. In other words, Gen(s) *is the set of schedules* that s can generate in output.
![[Pasted image 20250505133337.png|500]]
However, contrary to view-serializability, conflict-serializability can used in practice, in particular, in some sophisticated applications where concurrency control has to be taken care of by a specialized module, that can impement the SGT (Serialization Graph Testing).
# Concurrency Control through Locks
In commercial system, we use **"locking schedulers"**. With this method, a transaction must get a permission to execute and lock a specific element.
There are locks for reading and writing, but for simplicity we will have an exclusive lock on an element. The lock operation *means that the exclusive use of element A for the database is asked in order for transaction $T_i$ to operate on A*. 
### Well-formed transaction
- **Rule 1**: every transaction that appears completely in a schedule is well formed, which means that no lock/unlock is issued more than one per transaction, and every read/write action is contained in a critical section
- **Rule 2**: The schedule with locks is legal, which means that if no transaction in it lock an element A when a different transaction has a lock on A.
### Passive Locking Scheduler
It's simple, uses a Lock table, wich is a data structure that the scheduler uses with contains information about which transaction holds the lock. When processing a step $o_j(x)$ of the input lock-extended schedule S, the passive locking schedules proceeds as follows:
- If x is locked by $T_j$ then it proceeds
- Else $T_j$ is blocked and executed later on
### Active Locking Scheduler
An active locking scheduler can proceed even though the input scheduler doesn't ask for locking. The scheduler understands the need to grant locks, granting locks without the schedule actively asking them. It basically gets as input the schedule, without explicit lock/unlock commands.
>Ghost update: Isolation cannot be ensured with the use of locks

2 phase locking:
A locking scheduler foillows 2-locking phase protocol if for every transaction all locks precede all unlocks. We will be talking about a **growing phase**, in which all locks will be issued for a transactions, and a **shrinking phase**.
Combining A 2PL and a locking scheduler we get:
- Schedule generated is legal
- All transactions are well formed
- all lock ops precede all unlock operations
We denote Gen(2PL) the sets of schedules generated by a 2PL scheduler. { DT(S) | there exists a schedule S’ such that S is the output of a 2PL scheduler with exclusive locks when processing S’ }
Checking whether $S \in Gen(2PL)$ is not easy! We need to check if we can insert exclusive locks and unlock commands into S such a way that the resulting sequence of actions can be generated by a 2PL-exLock
## 2PL and Conflict-serializability
Th. If $S \in Gen(2PL)$ then $DT(S)$ is conflict-serializable.
Proof is based on induction over number of transaction. for N=1, then DT(S) is serial, and so conflict-serializable. Now given that schedule S with N-1 transactions is conflict-serializable, we need to prove this for N transactions.
Let's consider that the transaction $T_i$ does the first unlock operation $u_i(X)$. Suppose we have a $w_I(Y)$ in $T_i$. Suppose that there is a conflicting action $w_j(Y)$ in S preceding $w_i(Y)$. 
Since $T_i$ is the first transaction that executes an unlock operation we either have that right before or after $w_j(Y)$, and so S is not in Gen(2PL) with is a contraddiction.
# Shared locks
With exclusive locks, a transaction reading A must unlock A before another transaction can read the same element A. It's too restrictive, since two read operations do not create conflicts, so we'll create the *shared lock time*. We denote with $sl_I(A)$ the comand for the transaction $T_i$ to ask for a shared lock on A, while we keep the *exclusive lock* (or *write lock*) $xl_i(A)$ for write operation.

A scheduler should need to do decisions, making the scheduler even more complicated, choosing what to allow and what to reject. Several methoss can be chosen:
 - First come first served
 - Give priorities to shared locks
 - Give priority to transaction asking for lock upgrae
all policies shouldn't have *starvation*
Even with shared locks we can have conflict-serializability!

## 2PL with Shared Locks
With exclusive locks, a transaction reading A must unlock A before another transaction can read the same element A. It's too restrictive, since two read operations do not create conflicts, so we'll create the *shared lock* paradigm. We denote with $sl_I(A)$ the comand for the transaction $T_i$ to ask for a shared lock on A, while we keep the *exclusive lock* (or *write lock*) $xl_i(A)$ for write operation.
This will slightly change the rules for well-formed transactions and legality of a schedule. It is legal to go from a shared lock to an exclusive lock, thanks to a _lock upgrade_ operation, which doesn't need for the transaction to first be unlocked.
This will be making the scheduler even more complicated, choosing what to allow and what to reject. Several methods can be chosen:
 - First come first served
 - Give priorities to shared locks
 - Give priority to transaction asking for lock upgrae
all policies shouldn't have *starvation*
Even with shared locks we can have conflict-serializability!
## Deadlock Management
Even with 2PL, deadlock is still possible, see slide for example. Generally, probability of deadlock grows linearly with number of transactions and quadratically with lock operations. We will explore three possibilities of deadlock management:
1. **Timeout**: System waits a fixed timeout period $t$, then transaction waiting for the lock is killed. Too simplistic, we may encounter starvation
2. **Deadlock detection**: We use a wait-for graph, that the scheduler maintains, where edges indicate that the source is waiting for a destination transaction to release a lock. If a cycle appears, kill one of the involved ones. More complex, since we need to keep track of the graph, but better
3. **Deadlock Prevention**: We use a wait-die graph, with every transaction having a priority associated. In the case of a conflict for a lock, $T_i$ is allowed to wait for $T_j$ only if $T_i$ has a greater priority, otherwise $T_i$ is killed. This works, because in a cycle of unique priorities, we will always have a node with lowest priority.
# Recoverability of transactions
Given the system that we built, we still have an issue regarding the `rollback` operation, since serializability is not enough to satisfy ACID properties. This is testified by the **dirty read anomaly**.
### Dirty Read
We consider two transactions T1, T2 both with commands READ(A, x), x = x+1, WRITE(A,x). We consider the rollback of T1 right after the write.
![[Pasted image 20250511172415.png]]
$T_2$ reads an element written by a transaction that doesn't exist anymore. It's a Write-Read anomaly. We need to consider that in a rollback we shouldn't have any effects on the database. We could use the *cascading rollback*, and roll back whatever transaction that has used objects of the rolled-back operation. This can be destructive, because this would be needed to do to all of the others.

In order to capture the idea of having transactions that, if rolled back, have no anomalies, we'll talk about **recoverable schedule**. A schedule $S$ is recoverable if no transaction in S commits before all other transactions it has read from, commit.
Example:
- $\{w_1(A), w_1(B), w_2(A), r_2(B), c_1, c_2\}$ is recoverable
- $\{w_1(A), w_1(B), w_2(A), r_2(B), r_3(A), c_1, c_3, c_2\}$ is NOT, since $T_3$ reads from $T_2$ but, it commits before it.
Every serial schedule is recoverable, but serializability is *independent* from reocverability. Reocverable schedules may still suffer from cascading rollbacks, so we will call the class of schedules **ACR** (Avoids Cascading Rollbacks). A schedule S belongs to ACR if every transactions in S reads values that are written by transaction that have already committed. 

Given the complexity of dealing with specific cases, we may want to get a stricter version of schedules, that are more easily checked for. We will introduce the concept of 
- **Strict Schedules**: we say that in a schedule S a transaction $T_i$ *writes on* $T_j$ is there is a $w_j(A)$ in S followed by $w_i(A)$ and there is no write action on A in S between there two actions. A schedule is *strict* if every transaction reads/writes only values written by transaction that have already committed. When a transaction $T_i$ rollback it's immediate to determine which are the values that have to be stored back in the database to reflect the rollbacks of $T_i$, since it's the last transaction to write over them. $strict \subset ACR$ 
- **Rigorous Schedules**: Although strict schedules avoid the cascading rollback, they do not ensure conflict-serializability. A schedule S is *rigorous* if for each pair of conflicting actions $a_i$ and $b_j$ appearing in S (appearing in this order), $T_i$ commits $c_i$ between $a_i$ and $b_j$
## Recoverability and 2PL
2PL is used in practice. We need to modify 2PL so that we take into account the concept of recoverability.
We use the **strict 2PL protocol**: a schedule S follows the strict 2PL protocol if it's 2PL and all exclusive locks of every transaction T are kept by T until either T commits or rollbacks. Every schedule following the strict 2PL protocol is both strict and serializable.
Most schedulers use an even stronger **strong strict 2PL protocol**, whcih asks that schedule follows the 2PL protocol, and *all locks* of every transaction T are kept by T until either T commits or rollbacks (not just exclusive locks!). This implies rigorousness.

It follows LOCK -> COMMIT -> UNLOCK methodology

Every schedule following strong strict 2PL protocol is rigorous. Also, every schedule S following the strong strict 2PL protocol is serializable, and the commit order of S is also a conflict-serializable order. Indeed, we can show that every ss2pl schedule S is conflict-equivalent to the serial schedule S' obtained from S by ignoring the rolled back transactions, and by choosing the order of transactions determined by the order of commit.

![[Pasted image 20250511184226.png]]
# Timestamp-Based concurrency control
Another concurrency-control strategy, based on unique timestamp. We associate to every transaction $T$ a timestamp $ts(T)$ that is unique ambong the active transactions. we assume that the logical times coincide with the transaction number $T_i :=  ts(T_i) = i$, and so we'll use $t_i$ to indicate the physical time of a given action.

Timestamps induce a total order on transaction, so every schedule respecting the timestamp order is conflict-serializable. It's conflict-equivalent to the serial schedule respecting the timestamp order. Doesn't use locks, but deadlock is still possible
### Algorithm
a timestamp-based scheduler maintains the following data for each element X:
- rts(x) : highest timestamp among the active transactions that have read X.
- wts(x) : highest timestamp among the active transactions that have written X (timestamp of last transaction that wrote X).
- wts-c(X) : timestamp of the last *committed* transaction that has written X
- cb(X) : a bit that is false if the last transaction that wrote X has not committed yet, true otherwise (so if the last transaction either commits or aborts).
The idea is that the system checks whether the logical time of the action is coherent witht the timestamp order, otherwise it kills it.
### Rules:
1. **Case 1a Read OK**:  Every action has both a physical (regarding the action in itself) and logical (regarding the timestamp of the transaction). *logical time is greater than the transaction that wrote the element*, while the *physical time is greater than the LAST write operation*, so the **time is coherent**, read is OK and schedule goes on.
	- We are not talking about the *recoverability*, for now! We check for the commit-bit of (X), which is false: In this case we are talking about strict recoverability. Transaction $T_2$ is put into a *waiting state*, waiting for $T_1$ to either abort or commit.
2. **Case 1b Read Too Late**: Physical time of $r_1(x)$ is t4, while logical time is $ts(T_1)$, that is less than the logical time of $w_2(X)$. $T_1$ gets killed, and its actions rolled back. (read compared to write)
3. **Case 2a Write OK**: Physical and logical time are coherent. Similar to read ok, we also check commit bit.
4. **Case 2b Thomas rule**: $w_1(X)$ compared to both $r_1(X)$ and $w_2(X)$. Physical time not coherent with logical time. If the commit bit of X is true, then we ignore the conflict of $w_1(X)$, pretending like it was executed before $w_2(X)$ (since in the serial schedule $T_2$ would be executed after $T_1$. If the cb is false then we wait for the commit.
5. **Case 2c Write too late**: $w_1(X)$ is incoherent with a **read** action, then transaction is aborted.
Generally, when we abort a transaction, it means that we roll it back and we add it again afterwards.
**Deadlock** can still occur, but we can use the same algorithms used for lock-based scheduling.
# Multiversion concurrency control
Until now we have assumed that every element in the DB has a single version. However, modern system uses a version control system. We let the transactions access whatever version they seem fit. Each legal write action creates a new version, and each read can access the version it wants, as long as it doesn't break conflict-serializability. ==Every read action is never stopped==, since we always have a valid versions. Everything is transparent.

When the transaction concludes, it will successfully commit only if the values updated by the transaction have not been changed externally since the snapshot was taken.

By using a multiversion timestamp-based method there won't ever be a read too late issue, since the transaction will just read from another version previous to that.
# Concurrency control in SQL
SQL is created with only three different anomalies in mind:
- **Dirty read**: transaction reads an element from a transaction not committed yet.
- **Nonrepeatable read**: transaction reads same element twice (isolation property broken).
- **Phantom read**: New kind of anomaly, occurs when a transaction $T_1$ executes a range query, another transaction $T_2$ inserts or deletes tuples in that range $T_1$ executes the same range query and finds different results. Can be avoided by range locks.
To go over these issues, SQL allows the user to choose `ISOLATION LEVEL`, which are 4:
- *Read uncommitted* (no anomaly ruled out)
- *Read committed* (dirty read ruled out)
- *Repeatable read* (nonrepeatable read ruled out)
- *Serializable* (no kind of anomalies possible)

**Postres** uses, as the lowest minimum isolation level (and also the default) the *read committed*, so no dirty read will be possible. The  concurrency control strategy of PostgreSQL is a sort of multiversion control combined with (implicit and explicit) locking. Write locks are asked only at the transaction end, while read locks are released as soon as SELECT operation is performed. Deadlock management is based on recognition.
PostreSQL uses locks as **an active scheduler**. -> 2PL
# File Organization
![[Pasted image 20250702150900.png]]
### Relations, files, pages and records
- A relation is a set of tuples (records). 
- Every record is contained in a page, and has a tuple `<space, slot-number>`
- Every page is on a DB file, which is a set of pages, which represent relations.
- A relation could be stored in different pages, or files.
Pages are a mean of transport from **secondary storage** to **buffer** of the DBMS.
#### Cost model (wrt exec time)
We'll consider our model with following data:
- **B**: Number of pages in file
- **R**: Number of records per page
- **D**: time for R/W poeration to/from secondary storage (tipically 15ms)
- **C**: Average processing time per record (tipically 100ns)
The operation analyzed witll be:
- **Scanning** the record of a file
- **Selection based on equality** which is the cost of loading pages with relevant records, and for locating records in the pages (search based on relation key)
- **Selection based on range of values** similarly of the equality-based seleciton
## Simple File Organization
### Heap
As the professor called it, it's the woman's handbag.
Contained with no special order of storage. To add it costs $O(1)$, to search it's $O(n)$. Every page has a header page, and from there we have a double linked list of pages, linked by pointers. Pages are distinguished from full pages and free pages.
- Scan: $O(B)$
- Equality selection: $O(B)$
- Range selection: $O(B)$
- Insertion: $O(1)$
- Deletion: $O(1)$ if identified by rid, $O(B+Y)$ if record specified through equality or range selection, with $Y$ being the number of pages with records to be deleted
### Sorted
Records are sorted within each page on a set of fields ("search key"), and pages are sorted according to the sorting of the records.
With sorted pages we have a scanning advantage, since we can use binary search with $O(\log B)$. We may also use interpolation search: if the searck key values are numeric, and uniformly distributed in the range (Kmin, Kmax), and if K is the value to search, then, assuming that the distance between addresses is analogous to the distance between key values, we can choose as tentative address.
$\displaystyle i = a_1+\frac{(K-K_{min})}{(K-K_{max})} \times (a_n-a_1)$ 
- Scan: $O(B)$
- Equality selection: $O(\log_2 B)$ with binary search, while we have $O(\log_2 \log_2 B)$ as the average case in interpolation search.
- Range selection: $O(B)$
- Insertion: $O(B)$, since even if we use binary search we may need to shift everything, which has linear cost. Even if we use overflow tables we are paying for that access, which is $O(B)$.
- Deletion: $O(1)$ if identified by rid, $O(B+Y)$ if record specified through equality or range selection, with $Y$ being the number of pages with records to be deleted
### Hashed
It's a static file organization, in which pages of the relation are organized in a group, with each group being a bucket. A **bucket** consists of one page, being **primary page** and the other pages called *overflow pages*.
The search key is always here, it's used to seach for a record R with a given value k for a search key. From k, we calculate a hash function corresponding to k, and with that we access the correct bucket.
We are using, as an assumption, that pages are kept at about 80% occupancy 
A good hash function should be *uniformly distributed* (modulo is a good start).
- Scan: $1.25B \rightarrow O(B)$
- Equality selection: $O(B)$
- Range selection: $O(B)$
- Insertion: $O(1)$
- Deletion: $O(1)$ 
The idea of external sorting is to sort based on pages, and not record. Using a simple merge sort on the single records would have a memory cost too high:
- We read whole pages into buffer, we do in-memory processing, we write the blocks in the disk and then we repeat.
In fact, since the cost of getting from secondary storage to memory is so much higher compared to the single operations, we'll do cost calculation based solely on this.
#### Sorting with 2-way sort, using 3 frames
1. We sort each page (so we have B fragments sorted)
2. For each pair of pages we merge such two pages into one run, merging them together
3. Pass 2: for each pair of runs, merge such runs (each of 2 pages) into one run
4. ...
5. We have sorted all of the data
This has a cost of $O(B \log_2 B)$, since we have 1 page for each fragment, and we have B pages. $2 \times B \times (\log_2 B + 1)$. the $2 \times$ is becase we need to get the input and write the output. Generally, we will have more than 3 frames, and this means that we can have even better performance, by having less passes. With more frames $F$ in the buffers we can do B/F runs, and we do F-1 runs to merge. (K-Way sorting).
We write in secondary storage only when the buffer full.
## Index-based
An index is any method that takes as input a property of a set of recerdda, and "quickly" finds the location of the record with that property.
An index-based relation R comprises of:
- **Index files**: which contain both *data entries* and *index entries*
- **Data files** containing the data records.
We can organize our index in three ways: **sorted**, **tree-based**, **hash-based**.
### Properties of an index
1. Organization 
2. Structure of data entries
3. Clustering
4. Primary/secondary
5. Dense/sparse
6. Simple/Composite key
7. Single/Multi level
#### Structure of data entry
There are three main alternative techniques  for storing data entry whose search key value is k (we say this k*)
1. k* is a data record in itself
2. k* is a pair (k, r), with r being a pointer that allows the access of the data record whose search key is equal k
3. k* is a pair (k, r-list), with r-list being a list of references. Useful if we have many records with the same search key.
#### Clustering
An index (for data file F) is strongly clustering when the data entries are stored sorted according to the value of the search key, and also the data file itself is sorted. Sorting index is kept coherent with the sorting of the data file. We say that an index is *weakly clustering* if, for every value V of the search key, all the tuples of the indexed data file with value V for the search key used in appears in the same page of the data file.
#### Primary Secondary Index
A primary key index is the one which the search key is the key of the relation. Otherwise is called *non-primary* (also called *secondary index*).
#### Dense/Sparse key
An index is dense if every value of the search key that appears in the data file appears also in at least one data entry of the index. An index that is not dense is sparse. Basically, in a sparse index we will have one index entry per page of the data entry, which will also be clustering.
#### Single/Composite key
A search key is simple if constituted by a single field, otherwise composite.
#### Single/Multi - level index
This is the case in which we may have multiple indexes, and we have as data entries ones of another index. We can create a tree-based index based on this.
## Sorted Index
Suppose we have a file (which contains one relation). If for example we want to store the file with all records sorted. Suppose we have 1000 pages and we want to search for a particular record. We need $\log_2(B = 1000) = 10$ entries for a binary search. 
The idea of **sorted index** is to create another sorted file, with the pages that contain data entries which has $<value, pointer>$ tuples (with $pointer$ being $<page.id, slot.id>$, which are sorted on the interested attributes (it's a **clustered index**). The number of pages will be proportional to $2/ \text{\# attributes}$, since now every data entry has only two values. $\frac{B}{N}$ With $B$ number of pages.
Since a data entry (key and pointer) takes in general much less space that a complete data
record, we use many fewer pages for the index than for the data file.

- **Drawback**: Adding/deleting a value in the data file means that we need to also add an entry to the index page *to keep it up-to-date*. It's a sort-of investment. Inserting a data entry in a dense index could be the same as inserting a data entry in the data file, or we can use *local overflow tables*, hoping they don't grow too much (most common one).
This means we have a **clustering sorted index**, which can be primary of secondary (depending on the search key chosen). Even here we may have sparse and \[strongly/weakly] dense.