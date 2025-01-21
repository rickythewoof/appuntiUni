We may have three different kinds of ordered communication
# FIFO Order
We'll have another property added, since it's completely orthogonal with regards to reliability specification.
## Property
- **FRB1 - FRB4**: same as properties in the reliable broadcast (integrity, no creation, no duplication, agreement)
- **FRB5**: _FIFO delivery_ - if some process broadcasts message $m_1$ before it broadcasts message $m_2$, then no correct process delivers $m_2$ unless it has delivered $m_1$ first.
That property does not imply causality order between processes, but just that messages from one process will get delivered in the same order.
![[Pasted image 20250120111638.png]]
This can be done by implementing on the broadcast communication the idea of a local sequence number that every process will need to look before FIFO_delivering a message.
# Causal Order
We'll add a guarantee of delivery using a causa-effetto relationship to maintain the order. We'll follow the happened-before directives.
## Property of CORB
- **CRB1 - CRB4**: same as properties in the reliable broadcast (integrity, no creation, integrity, agreement)
- **CRB5**: _Causal delivery_ - if some process broadcasts message $m_1$ that potentially caused a message $m_2$ (ie $m_1 \rightarrow m_2$), then no correct process delivers $m_2$ unless it has delivered $m_1$ first.
We can correctly assume that **Causal Order => FIFO Order**. To do this we'll use the vector clocks implementations.
![[Pasted image 20250120112927.png]]
# Total Order (atomic communication)
Causal order may still not be enough! Two events that happened at the same time may still be delivered at different times. We need total order. A total order (reliable) broadcast abstraction orders all messages, even those that are not causally related. We may have:
- **Reliable Broadcast**: processes agree on the same set of message they deliver
- **Total Order**: processes agree on the same sequence of messages.
Total order is not related to FIFO and Causal Order, since we may agree totally on a universal order which is not FIFO.

![[Pasted image 20250120113929.png]]
## Specifications
Usually composed by four properties:
- **Validity** - Guarantees that messages sent by correct processes will eventually be delivered
- **Integrity** - Guarantees that no duplicate messages are delivered
- **Agreement** - Imposes constraints on the set of messages to be delivered
- **Order** - Imposes constraints on the order of messages to be delivered
---
## Total Order specification
(Non uniform) Validity and (uniform) integrity come directly from broadcast specification, so we usually don't impose restrictions on that. We'll study then Total Order in regards to \[uniform/non-uniform\] Agreement and Order.

|            | **Uniform**                                                                                                                                                 | **Non-Uniform**                                                                                                                                                       |
| ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Strong** | If some process TODelivers some message $m$ before message $m\prime$, then a process TODelivers $m\prime$ only after it delivers $m$                        | If some correct process TODelivers some message $m$ before message $m\prime$, then a correct process TODelivers $m\prime$ only after it delivers $m$                  |
| **Weak**   | If process $p$ and $q$ both TODeliver message $m$ and $m\prime$, then $p$ TODelives $m$ before $m\prime$ if and only if $q$ TODelivers $m$ before $m\prime$ | If correct processes $p$ and $q$ both TODeliver message $m$ and $m\prime$, then $p$ TODelives $m$ before $m\prime$ if and only if $q$ TODelivers $m$ before $m\prime$ |
Strong implies ordering over the same set of messages, while weak implies ordering only.
This table doesn't say anything about the agreement!
## Implementation
Total order specification relies on two major components:
- **Reliable broadcast** - To guarantee that everyone got the same set of messages
- **Consensus** - To guarantee that everyone got the same order

| Reliable Broadcast $\downarrow$ Consensus $\rightarrow$ | **Uniform**  | **Non-Uniform**                                                                                           |
| ------------------------------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------- |
| **Uniform**                                             | TO(UA, SUTO) | TO(UA, WNUTO), Not SNUTO because faulty process delivers $m_2$ before $m_3$, while $m_3 \rightarrow m_2$  |
| **Non-Uniform**                                         | TO(UA, WUTO) | TO(NUA, WNUTO). Not SNUTO because faulty process delivers $m_3$ before $m_4$, while $m_4 \rightarrow m_3$ |
