### Why?
- **Fault tolerance**: in a case of crash we may want to restart the system, but in that case memory gets lost: we want to be able to restore an image of the system. Assuming $p$ is the probability of an object to fail, it's availability is $1-p$
- Considering independent failure, replicating an object in n nodes means that now O's availability is $1-p^n$
## System Model
Processes interact with set of objects X located at different sites, and replicas of an object x are noted $x^1, x^2, x^3, ..., x^l$, and we assume a process $p_j$ crashes exactly when $x^j$ does too.
# Consistency
We need to define a set of criteria which tells the result of an operations. We have 3 different consistency ones:
- **Linearizability**
- **Sequential Consistency**
- **Causal Consistency**
# Linearizability
Considering the precedence relationship and concurrency relation between two operations, an execution E is linearizable if there exist a sequence S including all operations of E such that:
1. for any two operations $O_1$ and $O_2$ , such that $O_1$ < $O_2$, then $O_1$ appears before $O_2$ in sequence S
2. The sequence S is _legal_, which means for every object x the subsequence of S of which the operations are on x belongs to the sequential specification of x.

| ![[Pasted image 20250121104318.png]] | ![[Pasted image 20250121104330.png]] |
| ------------------------------------ | ------------------------------------ |
|                                      |                                      |
## Sufficient Condition for linearizability
These two conditions directly affect the replication techniques, as they make possible to order all operations in a deterministic way for everyone
### Atomicity
Given an invocation, if one replica of the object handles this invocation, then every correct replica of x also handles the invocation
### Ordering
Given two invocations, if any two replicas handle both invocation, they handle them in the same order

---
## Replication Techniques
We have two main techniques, one more centralized than the other
### Passive Replication (Primary Backup)
- The **primary** part is the one directly handling the communication with the client, and given an object x, prim(x) returns the primary of x.
- The **backup** part interacts with prim(x), and replaces the primary in a crash event
Primary replica gets the operation and makes every backup update the replica with the operation, waits for everyone's **ACK** to send back the response.
#### Failure handling
1. **Primary failure after message sent**: If the client receives the answer no problem, since a new primary gets selected. If client doesn't receive the answer it'll send back the request after a timeout. New primary will recognize duplicate and will send back the result without update
2. **Primary failure before sending update messages**: no issues, the client will re-transmit to new primary.
3. **Primary fails after sending update message but before receiving all ACKs**: We'll need to elect new leader among the correct replicas.
### Active Replication
In this case everyone is equal to every other process, the client needs to send the operation to every replica, and should wait for everyone's response. To guarantee both _atomicity_ and _ordering_ we need **Total Order Broadcasting**. It's more crash resilient.

---
# Replication as a way to scale DBMS
## Requirements
- **Transparency**: Clients must have the illusion to interact with a single object
- **Consistency**: Operations should have results as if they are executed on a single object -> **Linearizability**, concurrent object must behave in a sequential matter.
## Properties
- **Consistency**: "every request receives the same, right, deterministic response"
- **Availability**: "every request should eventually terminate with a response"
- **tolerance to network Partitioning**: It may happen that a network may get partitioned into groups that cannot communicate with one another!
### CAP Theorem
_“Of three properties of shared-data systems (Consistency, Availability and tolerance to network Partitions) only two can be achieved at any given moment in time.”_
Cannot meet all three at the same time, what we want to meet depend on what are our interest.

![[Pasted image 20250121112354.png]]