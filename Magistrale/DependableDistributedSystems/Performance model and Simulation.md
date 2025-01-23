# IT Capacity Planning
We have two definitions possible:
- Consists in estimating components such as *storage, hardware, software and connection infrastructure* resources required over some future period of time to correctly support service provisioning.
- Alternatively, it's also the process of predicting when service levels will be violated as a function of the workload evolution, as well as the determination of the most cost effective way of delaying saturation.
As with dependability, both definitions are correct but they concentrate on different topics. One is at the design stage, and the other is on the usage stage of things. 
We'll create a capacity planning model through the use of different methodologies that go with:
1. Environment understanding
2. Workload characterization
3. Workload model, validation and calibration
4. Workload forecasting
5. Performance/availability model development and calibration
6. Performance/availability prediction
7. Cost analysis (regards to Performance&Availability)
This is to create business/investment plans for the future
## Understanding environment
In this phase we want to learn what kind of:
- **Hardware**
- **Software**
- **Network**
- **SLA** (availability models)
- whatever else that can impact performance
## Workload model
The workload of a system is the sets of all input that the system receives from its environment in a given period of time.
## Performance model
This model analyzes and *predicts* performance metrics based on system and workload parameters. Outputs are usually response times, throughput, utilization, queue length. This is the final output that our capacity planning wants, that together with a cost model makes for investment planning.
We can create a model at two different scope levels

| System-Level                                                                                                                                                                                                   | Component-Level                                                                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| System is considered a black box, in which details are not represented, and we only consider throughput $X_0(k)$ of our black box, representing the average throughput as function of the number of requests k | Every resource is explicitly taken into account, and counts on the performance modeled, and relationship between resources are modeled (typically through network queues) |
### Performance modelling through queuing systems
We can model the throughput of our system-level model as a population generating workload at rate $\lambda$, while the system distributes services to servants, which will process works with a rate $\mu$. Depending on the difference in rates, request may be queued. 

Our queue system to performance model will have:
- Population (p)
- Number of servants s
- Arrival Schema (A)
- Service Schema (B)
- System Capacity (c)
- Queue Policy (Z)
This makes us able to create a standardized notation, which is called **Kendall Notation**
$$
A/B/s/c/p/Z
$$
We'll also add new metrics to analyze a system in a steady-state

| Notation | Meaning                                  |
| -------- | ---------------------------------------- |
| $N$      | Average number of users in the system    |
| $N^q$    | Average number of users in queue         |
| $T$      | Average time spent by a user in a system |
| $T^q$    | Average time spent by a user in queue    |
From Little's Theorem we can assume the following things, given a steady state:
- $N = \lambda T$
- $N^q = \lambda T^q$
- $T = T^q + 1/\mu$
We can derive an utilization factor $\rho = \lambda/s\mu$. If $\rho \ge 1$ there can be no steady state, since the arrival rate is higher than what the servants can deal with.

## Cost Model
this focuses on the bare costs, like hardware, software, telecommunication, personnel ...
# Elasticity
IS the degree to which a system can adapt to workload changes by provisioning and de-provisioning resources automatically. The idea is to always offer the best possible resource allocation, while being able to adapt to demands without causing downtime, or under-provisioning.
We can adapt by doing a dynamic scalability, which can be of two directions
- Vertical (scale-up): We allocate more powerful resources. Grows exponentially in price/capability.
- Horizontal (scale-out): We allocate more resources with the same capacity. This makes the scalability linear and can also guarantee better distributed properties.