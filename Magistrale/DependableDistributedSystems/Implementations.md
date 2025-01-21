# Point-To-Point Links
First interface in which we connect two different processes together and we make them talk.
## Fair Loss P2P link
Simplest kind of link. One process sends a message to another, with no assumptions or tests to see if the receiving end actually received the message or not. Just sends once.
### Issues of FLP2P:
- The sender must take care of the re-transmissions if it wants to be sure that a
message m is delivered at its destination. -> Stubborn Link
- The specification does not guarantee that the sender can stop the re-transmission
of each message. -> Quiescent implementation of Stubborn Link
- Each message may be delivered more than once. -> Perfect Link
### Specifications
We'll have 3 Main properties:
- **FL1**: _fair loss_ - If a correct process p infinitely sends a message m then a receiving correct process q will deliver it an infinite number of times.
- **FL2**: _Finite duplication_ - If a correct process sends to another correct process a message m a finite number of times, then the receiving process will need to deliver if a finite number of times
- **FL3**: _No creation_ -  If a correct process delivers a message m with sender p, then p sent the message m.
## Stubborn P2P link
This is a module that once it sends a message m to a process q, then it'll start to infinitely send that message q.
## Specifications
we'll have two properties:
- **SL1**: _Stubborn delivery_ - If a correct process p sends a message m to a correct process q, then q will deliver it an infinite number of times.
- **SL2**: _No creation_ - If a correct process delivers a message m with sender p, then p sent the message m.
We'll also briefly create a quiescent implementation based on the delivery, or our network would quickly saturate and go down!
## Perfect P2P link
This is the last step of creating a good point to point directive. It'll use both fair loss point to point links and stubborn ones. It's the basics of having a good and reliable system
## Specifications
Properties are:
- **PL1**: _Reliable delivery_ - If a correct process p sends a message m to a correct process q, then q will eventually deliver m. 
- **PL2**: _No duplication_ - No message is delivered by a process more than once.
- **PL3**: _No creation_ - If a correct process q delivered a message m with sender p, then p sent that message.
## Implementation
![[Pasted image 20250118113044.png]]

# Distributed Mutual Exclusion
Given a set of processes P and a set of resources, we want to access resources exclusively and we want to design a distributed abstraction.
We'll do the following assumptions:
- The system is asynchronous
- Processes are not going to fail (always correct)
- Processes communicate by using perfect point-to-point links
Our properties need to follow this:
- **ME1**: _Mutual exclusion_ - at any time t at most one process p is running the critical section.
- **ME2**: _No-deadlock_ - There always exists a process p able to enter the Critical Section.
- **ME3**: _No starvation_ - every request() and release() operation eventually terminate. 
### Logical Clock-based ME
#### Lamport method
Created by Lamport, it's based on the use of a counter that stores the operation history. Every process $p_i$ will have both a local counter and a queue where CS access requests are stored.
A process $p_i$ will have the following rules:
- **request to access CS**: $p_i$ sends a request message, attaching ck to the request, to all other processes, and adds its request to the local Q
- **request reception from a process $p_j$** : $p_i$ puts $p_j$ request (along with timestamp) in its queue, and sends back an ack to $p_j$
$p_i$ will enter the CS if and only if:
- $p_i$ has in its queue a request with timestamp t
- t is the smallest timestamp in the queue
- $p_i$ has received an ack with timestamp t' from any other process and t' > t
### Coordinator-based ME
There is a special process (centralized) we'll call coordinator that collects requests and grants permission to enter into CS. It's pretty easy, coordinator grants CS privileges with a deterministic algorithm.
### Token-based ME
The basic idea is like the _patata bollentes_, in which there is a token that gets exchanged between processes and that whoever gets the token can access CS. To establish fairness there will be a ring to exchange deterministically the token.
#### Algorithm
```
Init
	state = idle
	next = p(i+1)mod N
	if self = p0
		trigger pp2pSend(TOKEN) to next

upon event request()
	state = waiting

upon event pp2pDeliver(TOKEN)
	ifstate == waiting
		state = CS
		trigger ok()
	else
		trigger pp2pSend(TOKEN) to next

upon event release()
	state = idle
	trigger pp2pSend(TOKEN) to next
```

### Quorum-based ME
The basic idea of this method is that every process votes to see who gets access to CS. A process enters it if a large enough subset of processes vote him.
To guarantee resiliency, each process $p_i$ has an associated _voting set_ $V_i$ with these properties:
- $p_i \in V_i$
- $\forall i, j, V_i \cap V_j \neq \emptyset$ (there is at least one common member for each pair of voting set)
- $|V_i | = K$ (same load principle)
- each $p_i$ is contained in $M$ voting sets=
The Maekawa's algorithm is not deadlock-free! If two processes compete for entering CS, and they have a voting sets with 2 common processes, if they receive the request differently (one receives request before the other one, but the other in reverse) we'll have that no one will have a set of replies equal to $|V_i| -1$
#### Algorithm 
```
Init
	state = released
	voted = false
	Vi = get_voting_set(i)
	replies = 
	pending = 

upon event request()
	state = wanted
	for each pj in (Vi\pi) do
		trigger pp2pSend(REQ, i) to pj

upon event pp2pDeliver(REQ, j)
	if state == held OR voted == true
		pending = pending  {i}
	else
		trigger pp2pSend(ACK, i) to pj
		voted = true

upon event pp2pDeliver(ACK, j)
	replies = replies  {j}

when |replies| == |Vi|-1
	state = held

upon event release()
	state = released
	replies = 
	for each pj in (Vi\pi) do
		trigger pp2pSend(REL, i) to pj

upon event pp2pDeliver(REL, j)
	if |pending| > 0
		candidate=select_next(pending)
		pending = pending \candidate
		trigger pp2pSend(ACK, i) to candidate
		voted = true
	else
		voted = false
```
# Failure Detection
Considering the two timing assumpions (Synchronous vs Asynchronous processes) we want to create a Failure Detector algorithm, which is an oracle providing info about failure state of a process.
## Perfect failure detector
Possible in the case of synchronous system. A heartbeat packet gets sent, and if after 2 Timeouts events (that we know, since we have synchrony assumption, and that this value is equal to $\Delta$) a process doesn't reply with a heartbeat reply then it gets considered dead, and a Crash event gets triggered.
### Properties
- **PFD1**: _Strong completeness_ - Eventually, every process that crashes is permanently detected by every correct process.
- **PFD2**: _Strong accuracy_ - if a process p is detected by any process, then p has crashed.
## Eventually perfect failure detector
We can create a failure detector which will eventually tell us the status of a process correctly, we do not know when the system will have synchrony so we cannot base ourselves to a specified maximum timeframe, but that will be dynamically adjusted. So the notion of detection becomes a suspicion, and a process suspected of crash may get removed from suspicion if an answer gets detected.
### Properties
- **EPFD1**: _Strong completeness_ - Eventually, every process that crashes is permanently suspected by every correct process.
- **EPFD2**: _Eventual strong accuracy_ - Eventually, no correct process will be suspected of failure.
# Leader Election
## Perfect leader election
Generally speaking having assumption on synchrony of a process may be too limiting, so we may create a Leader Election so that we can be sure of an alive process we can base ourselves on.
### Properties
- **LE1**: _Eventual detection_ - Either there is no correct process, or a correct process will be eventually elected as leader
- **LE2**: _Accuracy_ - If a process is a leader, then other previously elected leaders have crashed
We'll base our knowledge of crash on a Perfect Failure detector, and in a case of a crash event that got the leader we'll select another with a deterministic algorithm from the alive processes and we'll elect that as leader.
## Eventually perfect leader election
In case we cannot do assumptions on time we'll have suspicions we'll use an eventually perfect FD, that will remove and add dynamically processes on the suspected list of dead processes. We'll also say that we'll trust the most not suspected process in rank, so that even if a process is wrongly suspected of crash, it'll be trusted again to be the leader by that process.
# Broadcast communication
Implementing a broadcast communication paradigm is essential on a system based on multiple process. _Do remember: For now, focus has always been on communication between two processes_
## Best effort broadcast
In this case we'll send messages based on a best-effort approach, in which process gets sent and if it's a correct one then every one will deliver that. If the sender fails then processes may disagree on the delivery status of the message!
### Properties
- **BEB1**: _Validity_ - if a correct process broadcasts a message m, then every correct process will eventually deliver m (from the use of PL)
- **BEB2**: _No duplication_ - No message is delivered more than once. (From PL)
- **BEB3**: _No creation_ - If a process delivers m with sender p, then p broadcast message m.
Basically it sends message (with PL) to every process one by one.
## Regular reliable broadcast
We'll try to fix the issues arisen by the assumption that the sender may fail, by introducing agreement property.
### Properties
- **RB1**: _Validity_ - if a correct process broadcasts a message m, then every correct process will eventually deliver m (from the use of PL)
- **RB2**: _No duplication_ - No message is delivered more than once. (From PL)
- **RB3**: _No creation_ - If a process delivers m with sender p, then p broadcast message m.
- **RB4**: _Agreement_ - If a message m is delivered by some correct process, then m is eventually delivered by every correct process.
This is still imperfect, since if both sender and a subset of receiving processes fail, then we'll still have processes that delivered m and others that didn't. We may use a lazy implementation (in which in the case of failure of the sender every receiving process that delivered m will re transmit to everyone), or an eager one, in which whoever delivers m will re transmit it back (useful when we are in asynchronous systems and so we don't have a perfect FD).
## Uniform reliable broadcast
In uniform reliable broadcasts we remove the assumption that to have agreement we need to have correct processes, by having ACKs for every correct process that delivers.
### Properties
- **URB1**: _Validity_ - if a correct process broadcasts a message m, then every correct process will eventually deliver m (from the use of PL)
- **URB2**: _No duplication_ - No message is delivered more than once. (From PL)
- **URB3**: _No creation_ - If a process delivers m with sender p, then p broadcast message m.
- **URB4**: _Uniform agreement_ - If a message m is delivered by a process, then m is eventually delivered by every correct process.
This means that even if a message is delivered by a perfect link, the delivery from the broadcasts perspective is postponed until every correct process receives it, or in the case of asynchrony that a majority of processes got the message (assuming that there are a majority of correct processes!)
# Consensus
If for any reason we need to reach consensus between a group of processes on a value that has been proposed we need to study algorithms. **Generals consensus problems**.

Generally, no algorithm can guarantee to reach consensus in an asynchronous system, even if just one process crashes.
## Flooding Consensus
The idea is that everyone sends to everyone their proposals, and before choosing and deciding, a value can be selected only when no failures happen during communications ($proposals[round] = proposals[round-1]$).
### Properties
- **C1**: _Termination_ - Every correct process will eventually decide.
- **C2**: _Validity_ - If a process decides _v_, then the value was proposed by some process.
- **C3**: _Integrity_ - No process decides twice.
- **C4**: _Agreement_ - If a correct process decides _v_, then every correct process will eventually decide _v_ too.
## Uniform consensus
in here properties are pretty similar, but it guarantees also uniform agreement. This is based on removing the check between two rounds, and instead waiting for the N-th round to decide. When we propose we'll send back every proposal to everyone.
### Properties
- **C1**: _Termination_ - Every correct process will eventually decide.
- **C2**: _Validity_ - If a process decides _v_, then the value was proposed by some process.
- **C3**: _Integrity_ - No process decides twice.
- **C4**: _Uniform agreement_ - No two processes decide two different values.
## Paxos Consensus
Family of algorithm that provides a viable solution to consensus in asynchronous settings, guaranteeing safety and proceeding only if the network behaves in partial synchrony.
The idea behind paxos is having three types of processes:
- **proposers**: Processes that propose a value;
- **acceptors**: Processes that must commit on a final decided value;
- **learners**: Passively assisting processes that obtain the final decided value.
The idea is that a proposer sends its proposal to the acceptor, which chooses the first proposed value received and informs everybody about its choice. If there are multiple acceptors we'll need to choose the first most accepted value.

Issue is when several values are concurrently proposed by different proposers; none of them can reach needed majority, and we have deadlock. -> We can allow multiple proposals to be accepted, but all accepted proposals must have same value. We'll accept a value if and only if it have a unique number that is bigger than the one that we want to accept!
**If a proposal with value v is chosen, every higher-numbered proposal issued by any proposer has value v**.
### High-level algorithm expression:
- **Phase 1**: prepare request <-> response
	- A proposer chooses a new proposal version number n, and sends a prepare request (PREPARE, n) to a majority of acceptors, asking if that version number already has a suggested value
	- If an acceptor receives a prepare request (PREPARE, n) it'll answer by sending a promise not to accept any more proposals numbered less than n, and suggests the value v' of the highest numbered proposal that it has accepted if any (answering $<ACK, n, n\prime, v\prime>$, else $\emptyset$ (answering $<ACK, n, \emptyset, \emptyset>$)
	- if an acceptor receives a prepare request with n _lower_ than n' from any prepare request it has already responded, it sends out $<NACK, n\prime>$.
- **Phase 2**: accept request<-> response
	- If the proposer receives responses from a majority of the acceptors, then it can issue an accept request (ACCEPT, n, v) with number n and value v, that can be the highest-numbered proposals among the responses, or the proposer's own proposal if none was received.
	- If the acceptor receives the accept request, it accepts the proposal unless it has already responded to a prepare request having number greater than n.
Since proposers can race each other to propose, compromising liveliness, we'll "elect" them
We'll now create multiple (1,1) instances of (1,1) Atomic register, so that every process can read what's written by the process and when every register has been read send back the value associated with the highest (most updated) timestamp.
# Registers
A register is a shared variable accessed by processes through read/write operations. Usually it's implemented via hardware on the CPU itself, but we want to implement the abstraction in a distributed message passing system, where there is no physical shared memory.
More in depth, the two operations that a process can do on a register are:
- **read() -> v**: returns the "current" value v of the register, without modifying the content of it;
- **write(v)**: it writes the value v in the register, and returns $true$ at the end of the operation.
Both operations start with the invocations and terminate when the corresponding response is received, a failed operation is one where the response is never received because of a process failure.

We'll denote (X,Y) a register where X number of processes can write to it an Y can read it.
Given two operations o and o', _o precedes o'_ if the response event of o precedes the invocation event of o', otherwise they are said to be concurrent.
## Regular Register
we'll base our regular register on two properties
### Properties
- **Termination**: if a correct process invokes an operation, then the operation eventually receives the corresponding confirmation;
- **Validity**: a read operation returns the last vale written or the value concurrently written;
## Atomic Register
we'll add one property over the regular one
### Properties
- **Termination**: if a correct process invokes an operation, then the operation eventually receives the corresponding confirmation;
- **Validity**: a read operation returns the last vale written or the value concurrently written;
- **Ordering**: If a read returns $v_2$ after a read that it precedes it has returned $v_1$, then $v_1$ cannot be written after $v_2$.
## Implementation
## (1, N) Regular Register
### Fail-Stop
We'll use a **Fail-Stop** algorithm, in which processes can crash but the crashes can be reliably detected by all other processes. We'll use both **perfect p2p links** and **Best-effort Broadcast**.
This implementation relies on the fact that if a *write()* operation gets done, then it sends in broadcast the new value to every process, and then waits for their ack before sending the writeReturn operation.
#### Issue
This implementation relies on the Perfect failure detector for validity, so in the case it's not perfect we cannot ensure it. To remove the issue we implement fail-silent
### Fail-Silent
This new algorithm relies on the idea that process crashes can never be reliably detected (like in async systems). The idea is that each process locally stores a copy of the current value of the register, and each value written has a unique timestamp associated. Both the writer and the reader processes uses a set of witness processes to track last written value.
- On the **write** operation we use, as before a BeB to send to everyone our new write operation, sending with it the value and the associated timestamp. A receiving process will register it as the new value iff the new ts is bigger than the one saved, and sends the ACK back to the sender. If the original writer receives more than N/2 ACKs then it triggers the writeReturn
- On the **read** operation we do something similar, by asking everyone their last value along with a reading identifier. If we receive more than N/2 values then we will return the highest value returned.
## (1,N) Atomic Register
The algorithm uses 2 distinct parts:
- We use a (1,N) regular register to build a (1,1) Atomic Register
- We use a set of (1,1) Atomic registers to build a (1,N) Atomic Register
### Step 1
The idea is to use the (1,N) regular register to have not just a value, but a $<ts, val>$ tuple, so that we'll be able to send back the last readReturn value if and only if the stored value on the rr if higher than the one that the atomic register has inside of it. 
**correctness of ordering property** derives from the validity property and from the fact that the read tracks the last value read and its timestamp. A read operation always returns a value with timestamp greater or equal to the one of previously read value.
### Step 2
We'll now create multiple (1,1) instances of (1,1) Atomic register, so that every process can read what's written by the process and when every register has been read send back the value associated with the highest (most updated) timestamp.