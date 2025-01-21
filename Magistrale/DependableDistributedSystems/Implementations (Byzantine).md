Recalling that a Byzantine process may act arbitrarily, create and drop messages, delay messages and alter them, it's important to deal as much as possible with the possible issues of introducing a Byzantine process (protecting process against attacks is important, but it's also important to limit damage once in)
# Authenticated Perfect Links
It's our basics to create a good p2p messaging system that ensures that a threat cannot create fake messages by spoofing messages
## Properties
- **AL1**: _Reliable delivery_: if correct process sends a message m to a correct process q, then q eventually delivers m;
- **AL2**: _No duplication_: No message is delivered by a process more than once;
- **AL3**: _Authenticity_: If some correct process q delivers a message m with sender p, and process p is correct (we may want to guarantee it regardless of correctness), then m was previously sent to q by p. -> We may use Cryptographic signing processes.
# Byzantine Broadcasts
## Byzantine Consistent Broadcast
### Properties
- **BCB1**: _Validity_ - if a correct process broadcasts a message m, then every correct process will eventually deliver m (from the use of PL)
- **BCB2**: _No duplication_ - No message is delivered more than once. (From PL)
- **BCB3**: _Integrity_ - If a process delivers m with sender p, then p broadcast message m.
- **BCB4**: _Consistency_ - If some correct process delivers message m and another correct process delivers message m', then m = m'.
This is done by sending a SEND packet with the message m to every process, which reply with an ECHO packet to everyone.
We'll send the delivered event if and only if:
$$
\#(\{p\in\Pi |echo[p]=m\}) > \frac{N+f}2
$$
We are assuming that $N > 3f$ .
In case the original sender is indeed byzantine we cannot guarantee that every correct process will deliver the message
## Byzantine Reliable Broadcast
### Properties
- **BRB1**: _Validity_ - if a correct process broadcasts a message m, then every correct process will eventually deliver m (from the use of PL)
- **BRB2**: _No duplication_ - No message is delivered more than once. (From PL)
- **BRB3**: _Integrity_ - If a process delivers m with sender p, then p broadcast message m.
- **BRB4**: _Consistency_ - If some correct process delivers message m and another correct process delivers message m', then m = m'.
- **BRB5**: _Totality_, or _Agreement_ - If some message is delivered by any correct process, every correct process eventually delivers the message.
This is done by adding a part on the previous Byzantine Consistent Broadcast specification, through the use of a READY step, which basically copies the previous ECHO step to ensure that we'll have a majority of correct processes with the same process
# Safe Registers
We will try and implement a register that is capable of providing some sort of strengths against Byzantine processes, and that has the same properties of the equivalen Regular Register.
Intuitively, we want to:
- **write operations** sends <v, ts> to servers and wait for _enough_ ACKs;
- **read operation** sends a read request and wait for _enough_ replies.
Using the concept used in the broadcast is not enough, since everyone should run the write operation ("_All or nothing_" approach)
We'll use Masking quorums
### Masking quorums
Assumption changes to a more stringent $N > 4f$, so that we'll see write/read requests successfully terminated once we have a number of acks/read response  more than $\frac{N+2f}2$. It closely resembles atomic registers.
![[Pasted image 20250121142710.png]]
## Regular Registers
We may use two different strategies:
### Using Cryptography
The writer signs every timestamp/value pair, and readers store it together with the signatures. Any non-valid signature gets ignored.
We check only at reading, since the writer is assumed to be correct (otherwise he could arbitrarily write anything to everyone, since it could sign itself).
With this system we can guarantee that we are safe from Byzantine interference if number of ACKs (or read responses) are more than $2f$. 
### Not using cryptography
The writing process p uses two distinct phase to write a new value, since only one phase wouldn't be enough to ensure everyone got the new write value. We'll implement then:
- **pre-write**: the writer sends a PREWRITE message to everyone, with the current timestamp-value pair, waiting for $N-f$ PREACK messages.
- **write**: Writer sends simply an ordinary WRITE message with current timestamp-value pair, and then waits until it receives ACK from $N-f$ processes.
Basically it sends a write update two times, so that a majority of correct processes has the update locally saved.
# Consensus
Ideally we want the same properties as the crash failure environment, for this reason we will define two different validity requirements
## Weak Byzantine Consensus
In this kind of weak form we formulate a validity property that's valid if and only if all processes are correct.
### Properties
- **WBC1**: _Termination_ - Every correct process will eventually decide.
- **WBC2**: _Weak validity_ - If all processes are correct and propose the same value v, then no correct process decides a value different from v, and in this context if some process decides v, then it was proposed by some process.
- **WBC3**: _Integrity_ - No process decides twice.
- **WBC4**: _Agreement_ - If a correct process decides _v_, then every correct process will eventually decide _v_ too.
## Strong Byzantine Consensus
In this requirements we ask a bit more in the case that there is a byzantine process
- **SBC1**: _Termination_ - Every correct process will eventually decide.
- **SBC2**: _Strong validity_ - If all processes are correct and propose the same value v, then no correct process decides a value different from v. Otherwise, a correct process may decide a value that was proposed by some correct process or the special value $\square$. 
- **SBC3**: _Integrity_ - No process decides twice.
- **SBC4**: _Agreement_ - If a correct process decides _v_, then every correct process will eventually decide _v_ too.
## Byzantine Generals Problem
Each general starts with its own value v(i), that must be communicated by the i-th general to the others, and then each generals uses a method to combine the values of v(1),...,v(n) to choose a plan of action. We'll select f(v) as the function method to choose the plan, which must be defined in a way that:
1. all loyal generals decide upon the same plan of action -> deterministic function
2. a small number of traitors cannot cause the loyal generals to adopt a "bad plan" -> we can base the vote v(i) upon a majority vote among them.
The issue becomes of how a loyal general should communicate with other loyal generals.
We'll change the wording: the general that gives out the order is the **commander**, while the others are **lieutenants**
### Oral Message communication model:
- every message that is sent is delivered correctly
- message source is known to the receiver
- message omissions can be detected
We'll inductively define protocol OM($f$), with $f$ being the max number of byzantine processes:
- for $f$ = 0:
	- commander sends its value to every lieutenant. Each one uses the value he receives from the commander, or uses default value if receives no value.
- for $f$>0 (gossip):
	- commander sends the value to every lieutenant, and for each i, let $v_i$ be the value the lieutenant receives from the commander, or else RETREAT if he receives no value. (the lieutenant i acts as the commander in algorithm OM($f-1$) to send the value $v_i$ to each of the N-2 other lieutenants).
	- For each i and j such that i != j, let $v_j$ be the value lieutenant i received from lieutenant j in step 2, or else RETREAT. Lieutenant i uses the same value majority.
There will be sent N*$f$ messages, strongly inefficient!
We can use Cryptography to validate what the commander tells.