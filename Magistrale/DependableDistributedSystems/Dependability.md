# Introduction to Dependability
The definition tells us that "Dependability is the capability of a system to deliver a service that can _justifiably_ be trusted", or also "Dependability is the ability of a system to avoid service failures that are more frequent and more severe than is acceptable". With the two definitions we want to put in perspective different things, with the first concentrating more on what is that we design such that the system is trusted (like replication, access control, byzantine resistance), and with the other concentrating more on the availability of the system.
## Dependability attributes
- **Integrity**: Absence of improper system alterations. (Also security)
- **Availability**: Readiness of correct service. (Also security)
- **Reliability**: Continuity of correct service. 
- **Safety**: Absence of catastrophic consequences on the user(s) and the environment.
- **Maintainability**: Ability to undergo modifications and repairs.
Our main goal then becomes to limit the kinds of failures (caused by faults) that can lead our system to a crash, and so a loss of availability, and we'll do it analyzing the entire life cycle of our system that consists of two main phases:
- **Development**:
	1. Initial idea and requirements elicitation
	2. Analysis
	3. Design
	4. Development
	5. Testing
	6. Deployment
- **Use**:
	1. Deployment
	2. Maintenance
	3. Review
	Role of the maintenance is to repair of modify the system to correct and prevent errors, and to adjust or add new functionality.
![[Pasted image 20250123122400.png]]
The usual plan of action to detect and recover complex systems is to create a control loop that

| **ANALYSE** $\rightarrow$ | **PLAN** $\downarrow$    |
| ------------------------- | ------------------------ |
| **MONITOR** $\uparrow$    | **EXECUTE** $\leftarrow$ |
All of this while interacting with the environment to sense information and actuate plans based on them.
# Availability
We need to define this by also introducing the reliability:
- The *reliability* of a system is the probability that it is functioning properly and constantly over a fixed period of time;
- the *availability* is the time fraction in which a system is operational.
Given this we introduce the *Mean Time to Failure* (and the relative failure rate $\lambda$), the *Mean Time to Recover* (and relative recover rate $\mu$) and *Mean Time Between Failures*.
The system can be only in two states, so $p_{up} + p_{down} = 1$, and given the flow in flow out principle $\lambda*p_{up} = \mu*p_{down}$ we can see that
$$
A = p_{up} = \frac{\mu}{\mu + \lambda} = \frac{MTTF}{MTTF+MTTR} = \frac{MTTF}{MTBF}
$$
Thus, to increase our availability, we need to decrease failure rate, or decrease the time to recover.
## Interconnections
So far we have studied the availability of a component, but in a distributed network we use multiple components all interconnected. (We will consider that component availability is independent from one another)
### Serial
in a serial connection, $K$ entities are all chained and the system works if all component work together. Only one component failing is enough to make everything fail.
$$
A_{serial} = \prod{Ai}
$$
### Parallel
In a parallel interconnection a system is available if there is at least one that is. So this means that it stops being available if all components fail.
$$
A_{parallel} = 1-\prod{Ai}
$$
### Hybrid M out of N
The system works as long as there are at least M correct entities, so we'll calculate the probability given that at most K = N-M entities may fail
$$
A = 1- \sum_{i = 1}^K{\binom{N}{i}A_C^{N-i}(1-A_c)^i}
$$
