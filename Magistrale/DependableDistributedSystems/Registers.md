**DEF**: a register is a shared variable accessed by processes through read/write operations. Usually it's implemented via hardware on the CPU itself, but we want to implement the abstraction in a distributed message passing system, where there is no physical shared memory.
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
# Implementation
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