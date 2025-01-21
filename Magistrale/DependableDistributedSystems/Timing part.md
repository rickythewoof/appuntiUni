# Timing Assumptions
A subset of processes that need to create a distributed system may have two different kinds of times:
- **Synchronous System**: in these kinds of system we have a known upper bound on what we can expect different things to take or to be.
	- **Synchronous Processing**
	- **Synchronous Communications**
	- **Synchronous Physical Clocks**
- **Asynchronous System**: We cannot do any sort of assumption on the time difference, so we cannot be sure that a system not responding is because it has crashed or that it's taking long.
	- **Asynchronous Processing**
	- **Asynchronous Communications**
	- **Asynchronous Physical Clocks**
Modelling these kinds of systems is hard, the first is more lenient while the second asks way more.
# Synchronizations Of Physical Clocks
We will want for out algorithms to work to be synchronized, but what would that mean?
- **Internal Synchronization** refers to the fact that every process is synced to each other, and we have an upper bound on their difference. More specifically $| C_i - C_j | < D$ $\forall i,j = 1,2,...,n$ $i \neq j$. We can say that all clocks _agree_ on a time difference of D
- **External Synchronization** refers to having a centralized time server S, and every process synchronizes to it. More specifically $| C_i - S | < D$ $\forall i = 1,2,...,n$ 
We can do some interpretations on this. For example, we can say that External synchronization => Internal Synchronization (with a bound of $2D$). The inverse cannot be said.

A Hardware Clock is said to be correct if its drift rate is always limited to a certain value $\rho>0$. More correctly we know that
$$
1-\rho \le dC/dT \le 1+\rho
$$
### Christian's Algorithm

Christian's algorithm is a method for achieving external synchronization using a centralized time server. Each process sends a time request to the server, which responds with the current time. The process estimates the round-trip delay and adjusts its clock as follows:  
$$T_{adjust}= T_{server} + \frac{T_{request} + T_{reply}}{2} $$
where $T_{request}$ is the time the request was sent, $T_{reply}$ is the time the reply was received, and $T_{server}$ is the server's time. This approach minimizes the synchronization error but can be less effective with variable network latencies. In general, it's accuracy is $\pm (RTT/2 + min(T_{request}, T_{reply}))$

### Berkeley's Algorithm

Berkeley's algorithm achieves internal synchronization without a central time server, basing itself in a master/slave approach, more resilient to crashes than Christian. 
The master process pm sends a message with a timestamp t1 (local clock value) to each process of the system (pm included).
When a process pi receives a message from the master, it sends back a reply with its timestamp t2 (local clock value). When the master receives the reply message it reads the local clock (t3) and compute the difference between the clocks $\Delta=(t_1 + t_3)/2 – t_2$. A designated coordinator polls all processes for their current time and calculates the average clock value:  
$$T_{average} = \frac{\sum_{i=1}^n T_i}{n}  $$
Each process is instructed to adjust its clock by the difference $\Delta T_i = T_{average} - T_i$. This ensures synchronized clocks across all processes, considering clock drift and differences.
### Network Time Protocol (NTP)

NTP is a robust protocol for external synchronization that considers round-trip delay and clock offset. It's the standard to synch different clocks from all over the internet using _external_ synchronization directives. Based on a remote reading procedure like Christian's Algorithm and it's based on a hierarchy

---
# Logical Clocks
In a lot of distributed applications it's not important to define _when_ things happened, but more the order in which they did. For this reason, the use of logical clocks to define an important relationship of **Happened-Before**, which is a relationship that tries to capture causal relationship between two events. We will note with ->i the ordering relation between events in a process $p_i$, and -> the happened before in any two events.
### Happened-Before
Two events $e$ and $e\prime$ are related to a happened before relationship if:
- $\exists \ p_i | e \rightarrow_i e\prime$
- $\exists m | e = send(m) \wedge e\prime = deliver(m)$
- $\exists e,e\prime,e\prime\prime | (e\rightarrow e\prime) \wedge (e\prime \rightarrow e\prime\prime)$ (Transitive relationship of happened-before)
This means that two events that do not fit into any of these three criteria can be considered, by this relation, as concurrent, and we will note this as $e_i || e_j$.
## Scalar Logical Clock
This is the simplest way to introduce a logical clock, that will be used to timestamp events. We can see that if $e \rightarrow e\prime$, then $ts_e < ts_{e\prime}$.
Each process will initialize its logical clock $L_i = 0$, and it'll get increased of 1 when it generates an event (which can be *send* or *receive*). We can see a big issue of this implementation. Although it satisfies the property that if e happened before e' it'll have a timestamp strictly less than e', we cannot guarantee the inverse. This means that we will not know, given the timestamp, what is the event that happened before another!
## Vector Clock
Similar to a scalar clock, but with the difference that every process has a *vector* of integer counters, with size N. Similarly to a scalar logical clock, the vector clock can be attached to a message m.
Each process will initialize its vector clock $V_i$ to an array of zeroes. It'll increase the value based of itself when it generates an event.
When $p_i$ sends a message m we'll increase $V_i$ and timestamps m with ts =$V_i$.
When $p_i$ receives a message m containing the timestamp ts it'll update its $V_i[j] = max(ts[j], V_i[j]) \forall j = 1,...,N$ and increases $V_i$

![[Pasted image 20250118125131.png]]
Given this new implementation we have that:
- if V(e) < V'(e) then e->e'
- if V(e) $\neq$ V'(e) then e || e'