# Tech Ingredients
### Hash Functions
given a particular string of bytes, a hash function is a One-Way-Function that creates a string of bytes of a fixed lenght. A good hash function should be uniformly distributed over the output space, so that for a random $x$, given $y \in Y$, $P(H(x) = y) = 2^k$

To be more specific, we'll be using **cryptographic hash functions**, which are hash function that are strongly collision-resistant.

the computation of the hash function for the blockchain works by 
```
1. reverse_bytes()
2. double_sha()
```
### Merkle Trees
Validating that a transaction belongs to a block can be done with the Merkle Root check. To prove the validity of a block it's enough to check the header and see if the hash connects to the block beforehand. 
To properly check that a transaction is valid and _finalized_ we need to wait, so that eventual forks will get removed and we'll converge to a unique story.


![[Pasted image 20250306152424.png|600]]
To check that a transaction belongs to a specific block we need the transaction by itself, all of the neighbors of the path from the transaction to the root, and the Merkle Root. This makes the proof of the existance of a transaction in a block runnable in $O(\log n)$   
[https://learnmeabitcoin.com/technical/block/merkle-root/](https://learnmeabitcoin.com/technical/block/merkle-root/)
### Block Structure
A block in the blockchain contains various structures necessary to link blocks together, a nonce so that Proof of Work is possible, and the list of all the transactions along with the merkle root.
- **Previosus Block Hash**
- **Block Hash**
- **Merkle Root**
- **Nonce**
- **Difficulty**
- ...
#### UTXOs
UTXO stands for *Unspent Transaction*. It's the chain of spent money. When someone *spends* bitcoins, what happens is that as an output we'll have two UTXOs, one containing the actual payment, and the other containing whatever is left in the wallet.
To spend or unlock a Bitcoin UTXO, you follow these steps:
- Create a transaction, including the UTXO as an input
- Specify the recipient address (essentially, its public key) and the amount to send
- Sign the transaction with the private key corresponding to the input UTXO
- Broadcast the transaction to the bitcoin network
We calculate an address balance by calculating its UTXOs. 
>[!WARNING]
>Given the transparency and openness of bitcoin, anyone can follow the chain of UTXOs. Because of this, for every transaction received we should use a new address (since generating adresses is as easy as calculating a new public/key pair).

Differently, Ethereum works out of States.
## Bitcoin Validation Rules
- For each input, look in the main branch and the transaction pool to find the referenced output transaction. If the output transaction is missing for any input, this will be an orphan transaction. Add to the orphan transactions pool, if a matching transaction is not already in the pool.
- For each input, if the referenced output transaction is a coinbase output, it must have at least COINBASE_MATURITY (100) confirmations.
- For each input, the referenced output must exist and cannot already be spent.
- Using the referenced output transactions to get input values, check that each input value, as well as the sum, are in the allowed range of values (less than 21m coins, more than 0).
- Reject if the sum of input values is less than sum of output values.
- Reject if transaction fee would be too low to get into an empty block.
- The unlocking scripts for each input must validate against the corresponding output locking scripts.
## Types of Nodes
## Full Node
verifies and relays the transactions and the blocks to the network. To check the validity of pending transactions, it has to independently validate the complete copy of the blockchain.
## Light Node
Connects to full nodes to interact with the blockchain. Namely, it uses full nodes as intermediaries. It needs only the chain of the block headers to operate. It can ask selected content of block bodies (i.e., the transactions) to full nodes when needed. Light nodes do no need to trust a specific full node, since full nodes provide the required information equipped with Merkle proofs. The amount of resources and storage needed is several orders of magnitude lower than that of a full node, while achieving a very high level of security.
## Client node
relays on 3rd-party servers and trusts them with the blockchain and interacts with it with API to access. (e.g. Infura).
# Consensus
One of the biggest issue of concurrency is a _lack of a global clock_, so we don't have an atomic measure of time because they are spatially separated.
#### Assumptions
We are assuming that links are reliable, or otherwise there is NO way to achieve consensus. Nowadays it's a fairly reasonable assumption, especially with TCP.
In the case of nodes we can assume tw o faults:
- **crash-failure**: Node stops working completely without warning
- **byzantine**: Node behaves arbitrarily, with the specific interest in a malicious behavior. Adversarial Context, in which nodes maliciously choose to alter, block or to not send message.

What we are interested in is to get a deterministic function, in which we achieve consensus among **correct components**, such that we have:
- *Agreement*: All correct nodes decide on the same output value.
- *Termination*: All nodes eventually decide.
- *Validity*: Value that has been decided it must have been proposed by some node.

### Crash failures
> [!WARNING]
> In the case of asynchronous communication, it's enough to have one faulty process to never achieve consensus. -> Termination property broken.
> The idea behind the FLP Impossibility result is that a node cannot distinguish between a faulty node and a node that is taking too long of a time to answer.

To combat this we will introduce a fault detector based on a timeout. If a node is taking too long to answer it's considered faulty. -> *Ben-Or's protocol*. The ideas is what's behind *Paxos* and *Raft* protocols.
### Byzantine Consensus
We'll use the idea of the **oral message paradigm**, in which we exchange point-to-point messages such that:
- Every message that is sent is delivered correctly.
- The receiver of a message knows who sent it.
- The absence of a message can be detected. (__termination__)
We have the idea of a commanding general that will make the proposal (__validity__) (in case of Proof of Work the leader is the one who solved the puzzle) that needs to be propagated everywhere so that all loyal lieutenants obey the same order (__agreement__).
In this case we need to have more than two-thirds of the nodes to be honest ($n \ge 3m+1$, with $m$ being number of Byzantine). (3 generals 1 byzantine does not have a solution!).
![[Pasted image 20250306161626.png|500]]
Problem is that we don't have knowledge of every node, and also since we have one-to-one communication we have quadratic overhead!
## Solution:
Instead of every node agreeing on a value, all the nodes agree on the probability of the value being correct. We’re growing the longest chain, and each new block lowers the probability of a malicious node trying to build another valid chain.
The consensus can in principle “change” over time, but more times passes the less probability of the agreement being different. Works if a single node make the proposal.

To reach consensus on the longest branch we need to be informed before the situation will change: if the network is slow a node can be come of the longest branch when it's no longer the longest. No consensus, potentially. 

We __Slow down__ the proposal of block adding by adding a timer, trustable by everybody. This is done by adding the a proof that enough time has been passed. Nonce used to solve the puzzle (and so prove that, in average, enough time has passed to propagate the previous blockchain), and with this we can adjust the difficulty based on the network delay.
## How much time is good?
It's a compromise between having a short timer (and so more probability of having forks) and a longer one (which makes it less probable, but slows down the blockchain).
This also makes it good w.r.t. _Partitioning_, because statistically the biggest partition will grow faster.
### Cheating
We need to have a ==cheat resistant timer== that is:
- Impossible to solve quickly
- Easy to verify
- Adjustable
- Based on common knowledge
For this reason we will use **Proof of Work**. Cheating is not possible, since the timer/puzzle can be proven to have been solved by everyone. Whoever solves the proof first will be the leader that will be able to add a transaction to a list of blocks.

Having a Proof of Work means that if the majority have the control of the power, and most are loyal, an attack like 51% will not be possible.
This is one of the biggest issues! Majority of bitcoin nodes are in China, so a government-mandated attack may break bitcoin security.
## Incentive
the strongest piece that makes full nodes participate in the bitcoin mining. When a block gets added by a leader, it retrieves the fees that every transaction have needed to be paid up along with the money that the block has generated.
Bitcoins are created each time a new block is mined. The rate of block creation is adjusted every 2016 blocks to aim for a constant two week adjustment period (equivalent to 6 per hour.) The number of bitcoins generated per block is set to decrease geometrically, with a 50% reduction every 210,000 blocks, or approximately four years. The result is that the number of bitcoins in existence will not exceed 21 million.
## Safety and Liveness in PoW
To recap:
- **Liveness**: Every transaction is eventually committed by all honest nodes
- **Safety**: honest nodes do not commit different blocks at the same height → single consistent history
We'll use [this explanation of the paper's proof](https://decentralizedthoughts.github.io/2019-11-29-Analysis-Nakamoto/)
### Assumptions
1. Longest chains win
2. Broadcast of blocks
3. $k$-confirmation commit
We have Poissonian process to model PoW, since it's memory-less.
where (considering $\alpha > \beta$)

|  Symbol  | Meaning                                                                         |
| :------: | ------------------------------------------------------------------------------- |
| $\Delta$ | Upper bound on network delay                                                    |
| $\alpha$ | Collective honest mining rate                                                   |
| $\beta$  | Collective malicious mining rate                                                |
|   $g$    | =$e^{-\alpha\Delta}$ discount factor of honest mining rate due to network delay |
|   $k$    | number of confirmation needed to commit                                         |
|   $T$    | Gap time between two block (inter-arrival time)                                 |
>**Definition 4(i).** _Suppose an honest block B_ _is mined at time t_. If no other honest block is mined between time t−Δ and t, then B _is a non-tailgater_ (otherwise, B _is a tailgater_).

We are considering a model in which blocks are not aware (_tailgaters_) and aware of the previous block. In lemma 5(i) of the paper, ==non-tailgaters do not have the same height, and so they contribute to the longest chain and so to liveness.==

We want to then measure the probability of non-tailgaters
$$ P(T > s) = e^{-\alpha s} = e^{-\alpha \Delta} = g$$
In the expectation, the number of non-tailgaters is $g\cdot\alpha$ 

> **Definition 4(ii).** _Suppose an honest block B_ _is mined at time t. If no other honest block is mined between time t−Δ_ _and t+Δ, then B_ _is a loner._

A loner is the only honest block at its height. In other words, a _loner_ is an honest block that _does not tailgate_ and _is not tailgated_. Loners are shown in purple in the previous figure. Loners will grow as $g^2\cdot\alpha$.

In view of the delay, we now know that Nakamoto consensus guarantees safety and liveness if $g^2\alpha > \beta$. If we have enough time to propagate the block then all of this works ($T >> \Delta$).
# From Proof of Work to Proof of Stake
[https://courses.grainger.illinois.edu/ece598pv/sp2022/lectureslides2021/ECE_598_PV_course_notes12_v3.pdf](https://courses.grainger.illinois.edu/ece598pv/sp2022/lectureslides2021/ECE_598_PV_course_notes12_v3.pdf)

The move is based on the fact that the $\text{nonce}$ part needs to be removed, because it's the basis of the PoW that we want to remove. For a given node, we will have a key pair public/private for signatures. We will use the public part to prove the stake of a given node.
The idea is that the probability of choosing a node as leader should be proportional to its stake, and shouldn't be bount to merkle trees (since that gives an unfair advantage, different positioning of transactions give multiple different values), but still depend on it, or a malicious actor may change content of transactions.

To resolve this we'll ==chain the block contents together with hashes==, but this makes it possible for an attaker to bribe an honest node that owns a block to change its content. This is solved by using *Key Evolving Signatures*, which will create a link of signatures. By asking honest nodes to destroy the keys used to sign a block, we will ensure immutability of the contents of honest blocks. 

To prevent the attacker on bribing a possibly known winner in the future, we'll use *Verifiable Random Functions*, which depend on the secret key, that will generate a pseudo number along with a proof of correctness.
The last sketch of a Proof of Stake, not based on a mathematical challenge, is 
$\displaystyle \text{VRF}(prev\_hash, ts, sk_n) < T \cdot stake_n$  
### Nothing at stake attack
The fact that now computational cost has been removed, and this doesn't check that the previous hash used is the actual latest, means that any attacker node can run alternative trees with ease using the same stake every time.
In this case, the number of NaS nodes grow exponentially, but the depth grows only linearly!
Given this, we can say that the protocol is safe as long as the adversarial hashing power is less than $\beta < 1 / (1+e)$. 

To set a specific block as a starting point we'll use a Genesis block for every $epoch$.
Differently from Bitcoin's UTXOs, the Ethereum blockchain works by state shifting. We have a World state $\sigma_t$ that contains a map between address and account state.

## RANDAO
For each epoch (every 6.4 minutes) we will execute RANDAO.
We will use RANDAO Algorithm, which is a random, deterministic algorithm to get a committee of people to agree on a common random number; with it we divide the active validators into *32 slots* (12 seconds each), each with:
- **1 proposer**: The proposer will get transactions from the mempool and decide on an arbitrary order for a block to be created, and assign the block to its slot. A validator may not propose a block for it being offline or out-of-sync, and won't get the reward.
- **A committee of 128 nodes**: The newly created block is then propagated to other validator nodes, who rerun the transactions in the block and validate the data signatures. If they find it valid, they submit a vote to the Ethereum network to attest to the block. Based on these blocks and attestations, the network builds a consensus to continue the chain.
![[Pasted image 20250617103432.png|500]]
THis process, although secure (an attacker has a very low chance of controlling at least 2/3 of the committee), is extremely slow.
## Algorand
#### Delegated Proof of Stake
The core idea behind this (which is the core process behind algorand) is that the community empowers a few special users, the delegates, to choose the next block, at least for a while. (For example, in EOS, the number of the delegates is 21.) Relying on their honesty for a long time is risky, and even assuming that there is an ironclad guarantee that all the delegates will remain honest forever, they can easily be attacked. In particular, they can be brought down by a denial of service (DoS) attack.

Using **Bounded Proof of Stake**, where anyone can put money in the system in a bond-like manner. This though gets the control of the blockchain on the hands on a small part of the economy. The fine given for misbehaving is way less than what it can be gotten from acting maliciously with great amount of money.
### Pure Proof of Stake
This calls for a new method, where money is never put hostage, and is the core idea behind **Algorand**.
 a very high level, in Algorand, a new block is constructed in two phases.
- In the first phase, **a single token is randomly selected**, and its owner is the user who proposes the next block. Who wins the lottery (using previously discussed VRF, for every single token of theirs) is a leader.
- In the second phase, **1000 tokens are selected among all tokens currently in the system.** (This is done through the same lottery based on VRFs). The owners of these 1000 tokens are selected to be part of a phase-2 ‘committee', which approves the block proposed by the first user. They run a Byzantine general agreement algorithm, so that they all agree on what the proposal is, and commit.
Using this approach, we can also see that **algorand never forks**, since although is possible to have multiple proposers, a validator will validate only the proposer with the lowest hash. We are always talking of an agreement protocol, which means that everyone will agree on the same set of nodes at last.
### Voting Steps
1. **Block Proposal**: Once an account is selected by the VRF, the node propagates the proposed block along with the VRF output, which proves that the account is a valid proposer.
2. **Soft Vote n1**: Each node in the network will get many proposal messages from other nodes. Nodes will verify the signature of the message and then validate the selection using the VRF proof. Next, the node will *compare the hash from each validated winner’s VRF proof to determine which is the lowest* and will only propagate the block proposal with the lowest VRF hash. This process continues for a fixed amount of time to allow votes to be propagated across the network
3. **Soft Vote n2**: In this step we confirm agreement on the selected proposal. This is the part in which a voting committee will be elected by the VRF. Each chosen account will have a *weighted vote* based on their account balance.
4. **Vote certification**: A NEW committee checks again the block proposal for validity, and if it is they will vote again to certify the block, iterating on the process until a quorum is reached.
### Binary Byzantine Agreement
![|400](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUewE4Id4jpn0_Bs_-Q1esO5ZeWzRDt7IKrf1xaO2q7cE6k5icmvA9hG7a7lvPAY0-00JwV0QPcgV2TVmNuU6nC16L5tT5nBoaxeqnsZZY-2GZVd-UOlF-YXw4Hc1_DwZG2UEdoJbI9K-Iz32-zxDjFvJwq0_tg6=s2048?key=bCvMfXrI3i0NH3nHjRWf1w)
```
n=3t+1 and t-byzantine fault tolerance (t malicious)

If #i(0) ≥ 2t + 1, 
	then i sets bi = 0.
Else, if #i(1) ≥ 2t + 1, 
	then i sets bi = 1.
Else
	i sets bi = c ← randomly and independently selected bit
```
Algorithm works on three steps, and a node $i$ which outputs $b_i = 0$ if in agreement. Given that at least $2t+1$ nodes are honest, we will reach consensus.
## IOTA
We use a DAG in this case. The benefit is that it allows for greater scalability and eliminates the need to pay transaction fees to miners, and the blockchain technology that uses DAGs is **The Tangle**. The idea is not to append transaction to a single chain, but _approving_ the tips of the DAG (at least one, at most two) by appending another transaction to them. The newly added transaction is unapproved, while the tips we appended to are now approved.
### Avoiding Lazy Tips and Keeping the DAG updated
A lazy tip is one that approves old transactions rather than recent one. THis doesn't help network, as we are not adding new approved transactions.
We need to balance out:
- Randomly selecting a transaction to append to doesn't help -> lazy tip
- Forcing the participants to only approve recent transactions is clashing with the idea of decentralization.
To give a solution to this we will use a random walk, which from the root we will go back and randomly choose a path. We'll add a bias so that we are more likely to walk towards an overall "heavier" transaction path. Still adding randomness is important, as otherwise we may have never-approved transactions.
We will still use the idea of the longest chain, so that transactions are considered valid only if they are part of a "long enough path"
### Double-Spending attacks
Using a DAG we can say that a transaction is considered valid only with a confidence percentage. In general, an attacker with high enough computational power can push another more favourable spending over another transaction, and by adding a lot of tips to it make it more confident.
**This attack is a risk if Alice can send more transactions than everyone else combined, or close to it.** If the blockchain is active enough it won't be a problem, but the IOTA DAG is not big enough. Every two minutes, a *milestone transaction* is issued by the IOTA Foundation, and all transactions approved by it are considered to have a confirmation confidence of 100%, immediately.
This removes a part of decentralization, but it's just a temporary solution
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcszHeO3hPAKWg2FxdOoqoU3haL0h3TvikEjT5Ec2HDWY0DJNgZOc9z7vwJ_LN8nZawEccg_8VK-HrnbSuimzy6Ddh56eBnYPFpyTocKaTFFnAVzxUY_dIfoJFoSkAkWHwiMY-_WRJKGeUeFftosrbslNvHRdUG=s2048?key=bCvMfXrI3i0NH3nHjRWf1w)# Ethereum
Differently from Bitcoin's UTXOs, the Ethereum blockchain works by state shifting. We have a World state $\sigma_t$ that contains a map between address and account state.
# Ethereum
Differently from Bitcoin's UTXOs, the Ethereum blockchain works by state shifting. We have a World state $\sigma_t$ that contains a map between address and account state.
## Accounts
The world state is a mapping between address and account state.
An account is an object, mapped by the address, that exists in the world state and contains:
- Address
- Account state:
	- **Nonce** (counter used to keep track of the sent transactions and agree on a total order)
	- **Balance**
	- **Storage hash**
	- **Code hash**
An account state can contain EVM code and storage, so that smart contracts can be run in the Ethereum Virtual Machine by a sort of Global Computer.
Accounts can be of two possible types:
- **Externally Owned Accounts (EOA)**: Is a more typical account that contains balance and can be used to make payments and such, and doesn't contain storage nor code. It is controlled by the owner trough the use of a Private Key.
- **Contract Account**: The type of account actually capable of storing data and running EVM code. It is not controlled by a private key.
## Transactions
A transaction is a single, atomic, and cryptographically-signed instruction that makes the world state $\sigma_t$ transition to $\sigma_{t+1}$. It's submitted by an external actor.
There are mainly two types of transaction:
- *Contract Creation* where a new account gets created
- *Message Call* used to for example connect smart contracts together. It's basically RPC.

| Field        | Notes                                                                  |
| ------------ | ---------------------------------------------------------------------- |
| nonce        | used as an account number of txs. Prevents replay attack on signed txs |
| gasPrice     |                                                                        |
| gasLimit     |                                                                        |
| to           | can be 160-bit address or 0, if contract creation                      |
| value        | transferred wei (Ethereum)                                             |
| v,r,s        |                                                                        |
| init or data | Contract creation or message call                                      |
### Merkle Patricia Tree
![[Pasted image 20250320144437.png|400]]
It's not simply a Merkle tree. Given that the contents of it may change over time, with the root not depending on the order of updates but only on the data.
It supports both insertion and update. The Key identifies the path to reach the leaf containing the corresponding value.

| Insertion                                                                                                                                                                                                                                                    | Update                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------- |
| ![\|300](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUcMYnoJlY8rbPXghXh98C0m97oTA3zlE2wN2X2lzunbEn6I1XyT0Z052KapGh2nZxJhL_2vkLP0EaCMI9WpbV_yZ9Rgpl2sV8ZnUfutQPKVBNw-uas-aThnHoWvMb_NmngXU0ln-zhxKFpEfTul0Asc0KlYU9SJ=s2048?key=bme1Bjk6kf1pvg7D3c1roA) | ![[Pasted image 20250320144734.png\|300]] |
![|600](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUe3DmPdPLJ3GWnlQDVMEA2Ql6tCpZj9N8zR_tPtjMG9pCW8SSu0MtNwlfleCs5TuZ4UGSc1pSdqUgspx7H4QEP5qQg2B1e-xWSQNA45tE_EHSuUhw_vl0HouqwArkWMHY65a66tJcCLhe-d1XMc_b-13AkodE0piTobqDPKyQ=s2048?key=bme1Bjk6kf1pvg7D3c1roA)
We then save the hash of the state root (computed via `keccak26()`) as information on the account state.
## Message
A message is what gets passed between two accounts. It may be both Data and Value. It may get both triggered by a *transaction*, for example between two *EOAs*, or it can be triggered by *EVM code*.
The order of all messages is decided by the *consensus algorithm*, RANDAO in the case of Ethereum.

The World state is shared around in a decentralized database, where everyone has a copy of it and that shares it around via P2P RPC calls.
## Ethereum Virtual Machine
It's a state machine, global computer that executes EVM code. It's the runtime of smart contracts.
![[Pasted image 20250320145511.png]]
- The **Stack** contains 1024 elements of 256 bits each. It is managed by PUSH, POP, COPY etc.. operations
- **Memory** is volatile, and it's linearly addressed. Can be accessed with MSTORE/MSTORE8/MLOAD instructions. It's not persistent across transactions.
- The **Account Storage** is a persistent $<key, value>$ database. Accessed with SSTORE/SLOAD instructions.
- **EVM code**, which is immutable, contains the bytecode that the EVM can natively execute. Solidity is an higher-level language that converts to a sort of assembly that then gets encoded to bytecode.
It's not much different than how an actual computer runs in the low-level.
![](https://ethereum.org/content/developers/docs/gas/gas.png)
## Gas
Gas refers to the unit that measures the amount of computational effort required to execute specific operations on the Ethereum network (e.g liters to go from Rome to Milan).

Since each Ethereum transaction requires computational resources to execute, each transaction requires a fee. Gas refers to the fee required to conduct a transaction on Ethereum successfully. Additionally to this, gas is what it needs to be paid per operation executed as EVM Bytecode. Every OP has a cost associated.

Gas fees are paid in Ethereum's native currency, ether (ETH) (e.g. euros per liters). Gas prices are denoted in gwei, which itself is a denomination of ETH - each gwei is equal to 0.000000001 ETH (10-9 ETH). For example, instead of saying that your gas costs 0.000000001 ether, you can say your gas costs 1 gwei.  (It's like Satoshi <-> Bitcoin)
### Endianess of Memory
it's a big-endian order, since it relies on the network byte order.
## Instruction Set
### EVM bytecode
EVM bytecode is a low-level programming language which is compiled from a high-level programming language such as solidity. EVM is a virtual machine which places between OS and application layer to mitigate OS dependency. Thankfully to EVM, Ethereum smart contract can be run on almost any of computers. If you are a Java developer, you can think of JVM(Java Virtual Machine) as the same mechanism. EVM is not human-readable but readable for the machine.
### Contract ABI
We have a Contract ABI. An ABI in computer science is an interface between two program modules. In Ethereum, Contract ABI is an interface a standard of calling functions in a smart contract. Contract ABI is designed for external use to enables application-to-contract and contract-to-contract interaction. For example, if you want to call a smart contract function from your dApp, you call via Contract ABI.
### Compilers
We have Solidity, Viper, LLL. We will use Solidity.
# Scaling the Blockchain
The blockchain has issues in scalability, since security relies on every node processing transactions. Idea is *sharding*,which consists in dividing node pools into processing shards of 100 nodes each.
The Ethereum “mainnet” is divided into smaller, interconnected networks called “shards.” Each shard processes its own transactions and smart contracts parallel to the others, significantly increasing the network’s throughput and helping to reduce gas fees.
## Shards
Through a pseudo-random protocol, eligible validators (the ones that have deposited a stake), are assigned to one of 100 shards.
In shard 1, a validator (proposer) is selected to group transactions into a collation, while other validators (notaries) download the collation and verify validity of transactions. If two-thirds of notaries attest to the collation, it is submitted to the main chain via the VMC (Validator Manager Contract). 
![|550](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfNOQQQbmjfSuLV0IfHhaKdXUL0l-Q9BTg3XY0FAcTXjNdDHJEXgD5aY-nXRG2GYsgYq-JZdVEYCVBXNLHszJ4pUDkdzVZhSv9zU_fa_MYLKPZSVEboWrSaYmV0221dB0P1Eb8v=s2048?key=a8x5tzMRvQXsKfNTBoIPhw)
When validators verify a block, they publish a signature, so that everyone else will need to check 1000 signatures instead of verifying 100 blocks.
We are offloading the block checking to only some of the nodes, while the others will just need to check signatures

We will pass the idea from **Voting** to **Proving**:
> Ideally, we want to have a form of sharding that avoids 51% trust assumption for validity, and preserves the powerful full verification of traditional blockchains. It will use the idea of data availability (proving that something is correct without downloading the entire data -> Merkle Trees, VRF). 
### Rollups
Rollups perform transaction execution outside layer 1 and then the data is posted to layer 1 where consensus is reached. As transaction data is included in layer 1 blocks, this allows rollups to be secured by native Ethereum security.
There are two types of rollups with different security models:
- **Optimistic rollups**: assumes transactions are valid by default, and only runs computation, via a *fraud-proof* computation in the event of a challenge.
- **Zero-knowledge rollups**: runs computation offchain and submits a *validity proof* to the chain
### Fraud Proof Challenge
- to accept the result of a computation, you require someone with a staked deposit to sign a message of the form "I certify that if you make computation C with input X, you get output Y". 
- You trust these messages by default, but you leave open the opportunity for someone else with a staked deposit to make a challenge (a signed message saying "I disagree, the output is Z").
**Only when there is a challenge, all nodes run the computation**. Whichever of the two parties was wrong loses their deposit, and all computations that depend on the result of that computation are recomputed.
### zk-SNARK
Zk-SNARK is an acronym that stands for “Zero-Knowledge Succinct Non-Interactive Argument of Knowledge.” It means that, given a secret knowledge of an origin, anyone that doesn't possess this knowledge can prove rapidly and without interacting with the origin.
It's the natural evolution from fraud-proof, since in its idea, it's not possible to create a claim that is false!

The biggest issue of the zk-SNARKs is that it's hard to compute the proof, even though is easy to verify it.
### Off-Chain Committing Transactions
The ides is still behind a particular kind of rollup. Instead of committing to each transactions, two parties commit in the blockchain to a predetermined fixed value. Two parties then will register "locally" the list of all of their transactions, up until they need to use that channel. Once the channel is considered closed, they commit to the blockchain and get back the differences.
![|450](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdE9wzHGkDiWFV2FmqrGMvRQsNoteaQiMLsL2gphc3QBP9Oc4OzdUSUlJIhnOzMxXSADdYXoj4z7qDTIsP75bf0e4nYNkXj6eWvASKZq2J05V37cdOPOXREe676Juw4uHkLp7ubT3-T69ywaJ5URElUogqds87W=s2048?key=a8x5tzMRvQXsKfNTBoIPhw)
#### MINA Protocol
it's a blockchain which relies on zero-knowledge proof. It remains at a fixed size.
![|400](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUdDKbKCtmgOGpWYs_tGVUb-qBWnFmi0-rwb1dwBbT9E1O2l0V0HOYIOa0dNJVkzD6wYZPrkrRlhsQnHVtYGQRbJ32FfM0rSq5zKZDR5ERqfyN7nzxqENwj7wP7q704ED4lBSiE-onDmPkbPFkjR5PDx1E8WLjip=s2048?key=a8x5tzMRvQXsKfNTBoIPhw)
# Anonymity Levels
Even tho we can create infinite address, if we use the tokens to buy, for example, a physical object, the address gets unequivocally associated to that identity.

A **Mixer** is a service in which money gets put in a pool of money, and you get back another address with that money. ==A mixer service is safe as long as you trust the service in itself.== (Similarly to a VPN, a mixer can see inputs and outputs)

**Commitment**: a prover $P$ hides a secret in the commit phase and opens it to a verifier $V$ in the open phase. We have two phase:
- **Commitment phase**: Prover creates a commitment with a secret and some random value.
- **Open phase**: Verifier checks the commitment without revealing the secret.
It's used for lots of purposes, as for example bidding. Only hashing the value may not work, since of Rainbow Tables we can "revert" the secret from the hash; we add randomness to increase the domain space.
## Wanted Properties
1. **Completeness**: Knowledge will be proven, if it exists
2. **Soundness**: Knowledge can be proven if it's real
3. **Zero-knowledgeness**: Verifier doesn't learn anything from proof.
## Zero-Knowledge Proofs
check [zk-SNARK](https://en.wikipedia.org/wiki/Non-interactive_zero-knowledge_proof). ZK proofs seek to demonstrate that someone knows the secret without revealing it. [Good article with examples](https://rareskills.io/post/p-vs-np). Problem is to _encode zk-SNARK into an arithmetic circuit_.
With **SNARK** we mean a *succinct* proof that a certain statement is true, while also being complete and knowledge sound. [Slides]([https://drive.google.com/file/d/1MxMCDy59rv0UuHkyGG6oZvPZDw6nijAY/view?usp=sharing](https://drive.google.com/file/d/1MxMCDy59rv0UuHkyGG6oZvPZDw6nijAY/view?usp=sharing)
A pre-processing argument system is a triple $(S, P, V)$:
- $S(C)$: public parameters $(S_p, S_v)$ for prover and verifier
- $P(S_p, x, w)$: Proof $\pi$ of the secret $w$
- $V(S_v, x, \pi)$: Accept or reject, without knowing $w$
We'll use the  Asymmetric Public-Key Cryptography.
Prover time is almost linear in $|C|$
![[Pasted image 20250328111722.png|500]]
## Performing a Trusted Setup
After compiling your circuit, you need to perform a trusted setup to generate proving and verification keys.
### Understanding Trusted Setup
- **Trusted Setup:** A process required for zk-SNARKs to generate the necessary parameters for proof generation and verification.
- You can choose between different protocols like **Groth16** and **Plonk**.
## Zerocash
(Idea that evolved from zerocoin and basecoin).
It's a token that uses zk-SNARKs in the commitment. Hiding and Binding are strong w.r.t. statistical attacks. User anonymity is achieved because the proof $\pi$ is zero-knowledge. Spending transactions are then hidden out in the commitment in the CMList, which is assumed to be not invertible; thus the origin of the payment is anonymous.
We also use $s$, which is a serial number, in the commitment phase, so that nobody can reuse the commit.
# Web3
![](https://lh7-rt.googleusercontent.com/slidesz/AGV_vUfLFI_rZ4jpxH2ADQ29KUnEDgVvb9x0eIJD96iDJUch0B8zTuNH-vMubnofTvmIHq_2fATa4M45VgxKoyC9YVtUynqiGMAZWovkyKq1Z_oT3hz6hOYuo7ab4KUAYuYUYw85EJLuKSMIp4fx5vULYcAhzQ=nw?key=JNNzLbD0qPcKHTPLDkeRxQ)
Web3.js is a robust and flexible collection of TypeScript and JavaScript libraries that allows developers to interact with local or remote Ethereum nodes (or any EVM-compatible blockchain) over HTTP, IPC or WebSocket connections.