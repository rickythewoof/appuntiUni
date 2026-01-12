# Network Automation
Refers to the branch of the _management plane_ of routers, which is responsible of configuration of network devices(for example, address/name assignment, configuration of which routing protocol to use).
Ideally, we want to centralize the management, such that no single network device needs to be accessed through CLI with specialized instruction set.
To do this, we need to define some Requirements.
- **R1**: A configuration management protocol must be able to distinguish between configuration state and operational state.
- **R2**: Safety regarding concurrency. A conf management protocol must support primitives to prevent errors due to concurrent config changes. Basically remove race conditions by applying a lock.
- **R3**: Be transaction-oriented: Devices should be able to decide whenever to keep current configuration or apply the new one (*accept* new config if and only if all network have accepted the new config, otherwise *rollback*).
- **R4**: We should be able to distinguish between different configurations (running, next, candidate), and all devices should be able to hold multiple configurations.
- **R5**: It should be distinguished between distribution and activation of configuration
- **R6**: A configuration managemnt protocol should clearly state regarding persistency of configuration changes
- **R7**: A configuration management protocol should log all config changes
- **R8**: Full support of dump and restore of changes
- **R9**: FUlly compliant with all tools and vendors

For this we have 2 different protocols:
## Simple Network Management Protocol
Simpler, is based on the use of 3 objects:
- **Agents**: The network devices that are controlled
- **Manager**: also Network Management System, is the C&C server
- **Managament Information Base**: A description of the internal state of any device. Composed on Object Identifier and the value, all organized in a tree-like structure.
### Polling and Trapping
It's the difference between for example PS2 and USB devices.
The NMS can be configured to periodically have the SNMP managers poll the SNMP agents that are residing on managed devices using the get request, or they can use Traps, which are unsolicited messages that get generated on an event.
## Netconf
Successor of SNMP. It's human-readable, transaction-oriented and supports more security.
The Netconf client is the manager (Network Management System), while the servers are all of the network devices. 
We can write simple python tools (`ncclient`) to interact with network devices, by querying them or setting them up.
It's based on a 4-layer stack (kind of like a ISO/OSI network stack):
1. **Secure transport**: Is what keeps a secure communication channel between client and server. Uses SSH.
2. **Message layer**: Envelopes, encapsulated in a common XML File Format. We may have `rpc` or `notification` envelopes. (First is synchronous, second is async).
3. **Operations**: The operation inside of the envethat we want to execute. We may use directives such as `get` or `get-config`
4. **Content**: The actual payload, or the content of interest

As per specification, netconf supports all of the different configuration types (`running`, `startup` -the one that will be loaded at next startup-, `candidate` -last being the draft configuration-)
Communication is done through XML type of messages:
### Protocol
After establishing a secure session, both NETCONF protocol send a hello message to announce the _protocol capabilities_, supported data model and the server's session ID.
```
S: <hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	S: <capabilities>
		S: <capability>
			S: urn:ietf:params:xml:ns:netconf:base:1.1
	S: </capability>
		S: <capability>
			S: urn:ietf:params:xml:ns:netconf:capability:startup:1.0
	S: </capability>
		S: <capability>
			S: urn:ietf:params:xml:ns:yang:ietf-interfaces?
			S: module=ietf-interfaces&amp;revision=2012-04-29
		S: </capability>
	S: </capabilities>
		S: <session-id>4<session-id>
S: </hello>
```

After that we'll send command through RPCs. The Remote Procedure Call (RPC) protocol consists of a `<rpc/>` message followed by an `<rpc-reply/>` message.
```
C: <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
	C: <get-config>
		C: <source>
			C: <running/>
		C: </source>
	C: </get-config>
C: </rpc>

S: <rpc-reply message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0"
	S: <data><!-- ...contents here... --></data>
S: </rpc-reply>
```
## YANG Data Modelling Language
Vendor comply with standardization companies, so that we have a universal way to define. For example, the IETF defined this in RFC 6020 in 2010, and uses a compact C and Java-like syntax focused on human readability. A data model is simply a well understood and agreed upon method to describe "something"

YANG models the way in which commands get sent, while XML is the way that those commands are sent.
The idea of YANG is to create a standardized way to query the device

| Node Type   | Holds Data? | Can Have Children? | Is a Collection? | Typical Use                      |
| ----------- | ----------- | ------------------ | ---------------- | -------------------------------- |
| `leaf`      | Yes         | No                 | No               | Single value like a hostname     |
| `leaf-list` | Yes         | No                 | Yes              | List of values like IP addresses |
| `container` | No          | Yes                | No               | Grouping related items           |
| `list`      | No          | Yes                | Yes              | Array of records like interfaces |

# Software Defined Networking
The idea behind SDNs is to get programmability in the control plane, by controlling the rules for which a packet is sent/forwarded. We'll introduce then the concept of **Generalized Forwarding**, decoupling the forwarding choices from the hardware.
### Generalized forwarding
In general, with the classical forwarding metrics, we use information about the destination to choose where to forward a specific packet. We want to generalize more the idea, by relaxing the constraint and:
1. Match on more than one field
2. Increase the number of actions
3. Apply multiple actions on the same packet.
We'll base this on a tuple `<match, action>` with match being the field we're interested in, and the action being the thing we want to used.
## SDN Routing
We need to "forget" about the various network devices and just use one only, which is a SDN-capable switch, which behaviour is controlled by the control plane.
## OpenFlow
Standard, defines the set of messages that the controller can use to interact and instruct te devies on the protocol to use. Differently than Netconf, we are now *dealing with the control plane*. We now have a standardized set of instructions that directly interfaces with the hardware, and so the packet goes through a pipeline of flow tables, in the ingress and at the egress. ==We have now separated the control plane, which now can be centralized to a single entity, from the data plane==.
![](https://lh7-qw.googleusercontent.com/slidesz/AGV_vUd2NAU28smCFjZqHpEO6C4m5iyL15GB8kWKXhfUCwgH1cpV0W1IIG598WABgdoOdNs8E994pm4smAB1rudHrygiPbq3HSx3MirJ7cgwv8xZX3t8e5M7oLb0JqBiDXRpkTLfgQvZ_R-FhYumnydWbl23q4X8k6rs=s2048?key=MARJQDFv5dPs5bZio3cRMw)
The openflow specification defines 3 different tables:
1. **Flow tables**: Contains the actual matches. Contains the packet headers that are needed to be analyzed, and applies actions accordingly.
2. **Group tables**: Generally called from a flow table, these can have a set of actions triggered by one or more flows
3. **Meter tables**: Tables containing some perfomance-related actions, along with containing analytics about different flows
We may have both physical, logical and reserved ports. Some of the reserved are :
	- **ALL**: specifies all ports that the switch can use for forwarding, only used for output
	- **CONTROLLER**: Represents the control channel between switch and controller
	- **TABLE**: represents the start of the Openflow pipeline. Packets get redirected here to the first flow table.
	- **IN_PORT**: Represents the packet ingress port, and can be used only as output port(??? nonsense)
	- **ANY**: special value used in some Openflow commands when no port is specified, cannot be used as ingress nor output.
	- **LOCAL**: Represents the switch’s local networking stack and its management stack. Can be used as an ingress port or as an output port
	- **NORMAL**: Represents the traditional non-Openf1low pipeline of the switch. Can be used only as an output port and processes the packet using the normal pipeline
	- **FLOOD**: Represents flooding using the normal pipeline. Can be used only as an output port. It sends the packet out on all ports except the incoming port and the ports that are in blocked state
### Messages
It's the data type that controls the controller <-> switch communication, where TCP is used. There are three classes of messages:
- controller-to-switch
- switch-to-controller (asymmetric)
- misc (symmetric)
#### Controller-to-switch messages
- (**features - configure)** operation set to query and set switch configuration and parameters
- **modify-state** which controls the flow entries in the Openflow table
- **packet-out** which controller can use to send the current packet out of a specific port
#### Switch-to-controller messages (the interesting one)
- **packet-in** where switch sends the packet and its control to the controller
- **flow-removed** notification of a flow table entry deleted at the switch
- **port status** informs the controller of a status change on the port level
### Reactive vs Proactive

| Reactive                                                                                                                                                                                                                                                                                               | Proactive                                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| In general, in the reactive kind there is a connection between controller and switch so that first new flow type will trigger the controller to insert flow entries. It's more efficient in terms of flow tables, has little flow setup time, but has limited utility if control connection gets lost. | In this, the controller pre-populates the flow table in the switch. It's more resistant to control connection drop, but it must be correctly configured with aggregated rules. |
## Virtual Networking
Computer systems typically consist of a _set of networking devices_ (eth0, eth1 etc.), which are associated with a physical network adapter, who is responsible for placing the packets onto the wire. In the world of virtual networking, a degree of internal plumbing is required to patch, tunnel and forward packets within the system.
This "internal plumbing" is built using virtual networking devices, such as - TUN, TAP and Veth Pairs
- **TUN**: It provides a Point-to-Point interface, so that we can analyze, send and receive IP packet traffic. it's only L3
- **TAP**: It provides too a P2P interface, but can also work with raw Ethernet packets
- **Veth**: Veth devices are created **as a pair** of connected virtual ethernet interfaces. They are useful to connect components like: LXC Containers, VMs, Host <-> Guest, etc..
### Isolation
Isolation can come in multiple ways (Virtualization and contenainerization). To do containerization, we will use some of the tools that the linux kernel gives us:
- **cgroups** which are a metering system, useful to allocate and limit resources for a given cgroup (like CPU, memory, _network_ usage)
- **namespaces**: Are a way of limiting the scope of processes, so that they can see only a container. The linux kernel has 6 types of namespaces: *pid, net, mnt, uts, ipc, user*
	- The *network* namespaces provides an isolated network stack. The idea would be to create different network namespaces, and then connect them together with a Veth pair. (which is a L2 network link).
### Switches -> Open vSwitch
It's a production-quality, multilayer virtual switch, which supports openflow as well as other. It has a set of components that control the behavious
- **ovs-vswitchd**: A daemon which implements the actual virtual switch along with a companion kernel module for flow-based switching
- **ovsdb-server**: A lightweight database server that ovs-vswitchd queries to obtain its configuration
- **ovs-vsctl**: Utility for querying and updating the configuration of ovs-vswitchd
- **ovs-ofctl**: Utility for querying and controlling OpenFlow-capable switches and controllers.
## Controllers
### ONOS
Open Network Operating System (ONOS[^1]) is an open source SDN network OS
- Architectural targets
    - High availability, scalability
    - Strong abstraction
    - Strong modularity
    - Protocol and device behavior independence
Given that by centralizing the Controller logic we create a Single Point Of Failure, ONOS can be distributed, thus having both high availability and high scalability
## POX
POX is a python-based SDN controller, mainly used for teaching and reseatch. Based on two main layers:
- **Core Layer**:
	- Offers event management, OpenFlow APIs, packet libraries, Python-based APIs etc
- **Component Layer**:
	- Stock and custom components
### OpenFlow with POX
Event handling in POX fits to the publisher/subscriber paradigm; so certain object publish events and the broker notifies the objects subscribed to the event.
Events are all instances of the subclass `revent.Event`. A class that raises events (which so it's a source):
- interits `revent.EventMixin`
- declares which events it raises in a class-level variable called `_EventMixin_events`
#### Events in OpenFlow
- **ConnectionUp** event is fired in response to the establishment of a new control channel with a switch
	- is raised only on the nexus
	- its .ofp attribute is an ofp_switch_features
- **ConnectionDown** event is fired when a connection to a switch has been terminated
	- this event is raised on both the nexus and the Connection itself
	- this event has no .ofp attribute
- **PortStatus** events are raised when the controller receives an OpenFlow port-status message from a switch
	- its .ofp attribute is an ofp_port_status
- **FlowRemoved** events are raised when the controller receives an OpenFlow flow-removed message from a switch
	- event's .ofp attribute is of type ofp_flow_removed
- **Statistics** events are raised when the controller receives an OpenFlow statistics reply message from a switch
	- each type of statistic (flow, switch, etc.) has is own event
- **PacketIn** event is fired when the controller receives an OpenFlow packet-in message
	- additional attributes are: port, data, parsed, ofp
- **ErrorIn** event is fired when the controller receives an OpenFlow error message

# Network Function Virtualization
A softwarized network is represented by a set of physical and virtual network functions (VNF), interconnected to provide a network service to end users.
Deals with network softwarization, tha goes from a classic Network Appliance approach of having tailored-made devices. Legacy, needs specialization, fragmented, and vendor-dependent. We can go from a vertical scaling (very costly), to horizontal scaling, in which we can create clusters of devices.
### Some Use-Cases:
- **NFVIaaS**: New service business model. We can put datacenters and network connectivity to create NFVI, that can be used to run virtualized network functions (as an example, Virtual Operators do this).
- **VNFaaS**: (We are now talking about Virtual Network Functions!) Similarly to SaaS. For example we may want to develop a service (VPN, Firewall ... ) in which the user just needs to put a provider equipment and then everything is done trhough that
- **VNF Forwarding Graphs**: A VNF Forwarding Graph defines the sequences of VNFs that the packet traverses. In other words, a VNF Forwarding Graph provides the logical connectivity between virtual appliances (i.e. VNFs).
### Orchestrator
Automates the process of the VNFs lifecycles. MANO is the Management And Orchestration which has been proposed as a standardized architecture.
## NFV Architectures
![|600](https://lh7-qw.googleusercontent.com/slidesz/AGV_vUdWhoAc2cUadKlH5_RZ95NvVNZovcB4sHmYpvakTSm0tGGy6SHOPlE_OS9a1F4fDASVpwxroBK5kxITx-RxHsvZp_Ui_9ALbPYnoIuJyG9Xccl2-5aV9IrZDoB9cyBH-v_umANp1_txsGUtEKgYSBnsQWVHzBQ=s2048?key=SQ0GOLAgXPhtRAccSCs06w)
Main architecture components
#### NFVI
Set of physical resources that allow the provisioning of a nework services. The NFV Infrastructure (NFVI) is a network of nodes, each virtualizing computation, storage, and networking, and able to host VNFs, that provides the transfer layer.
It's composed by both the software (virtualization) and the hardware platform.
#### Service plane
The Service Plane is populated by VNFs that can be provided alone, or chained to realize more complex Network Services (NS). Basicallty, the runtime space in which the VNF run. A NFV, or a whole service chain, can be mapped to one ore more VMs, and it's the point of the VNF Manager inside of the orchestrator to manage them
#### Management and Network Orchestation (MANO)
Composed by three different blocks:
- **VIrtual Infrastructure Manager** Controls the computing resources of the VNFI
- **VNF Managers**: usually 1:1 with the VNFs in the service plane, manage the lifecycle of the associated VNF instance
- **NFV Orchestrator**: deals with where to deplow the VNF.
It's the compositor, which dynamically creates, destroys and scales Network Services by controlling the VNFs
#### Operation Support System (OSS) and Business Support System (BSS)
Skipped, but generally important. Software plaform for which the customer can interact with the different network elements. 
## NetVM
Is one of the most popular **KVM-based NFV platform**. It's an NFV environment built over the KVM platform and the intel DPDK Library. Avoids the virtualization overhead when moving packets between VMs in the same host machine, by connecting all VMs together with a *shared memory* and without the use of the Hypervisor.
## Network Service Creation

|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The figure shows a deployment of the NFV Architecture, in which:<br>- **OSM** is used as *NFVO* and *VNFM*<br>- **OpenStack** is used as *VIM*<br>OSM has a Northbound interface with the APIs that allow the use of an OSM GUI<br>in the Southbound interface there are the APIs needed to interact with OpenStack<br>The targeted Network Service is composed of the following functions:<br>Firewall, DPI, Encryption, Data Monitoring, and Decryption<br> | ![](https://lh7-qw.googleusercontent.com/slidesz/AGV_vUdfGQ47IxToCvwRkerJ_Zo44Vsw4z2-8AXgNpleQ2l54poL_DyjDoNKC5ok-bUvjT5187j-wlhIkPKMJhg_4S3p1Kj5V3VLt4Lnl-V7lYkcZuFQ8V5lLgSEzD-8jB-1UHzVUNQgEdsWrBoafjZVWfPJU5YJ4Cnq=s2048?key=SQ0GOLAgXPhtRAccSCs06w) |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                                         |
OpenStack is an environment that sits on top of the different machines and orchestrates the creation, management and destructions of virtual machines. ==It's not an hypervisor, but it manages them.== It's composed of two types of node:
- **Controller**: Manages all services that are needed for the OpenStack Environment
- **Compute**: Runs the hypervisor to run instances and the Networking Service agent to provide connectivity
Every type of node are connected to both the *Provider* and *Management* network.

The second step regards the creation of the VNF Descriptors (VNFD) of each VNF composing the NS, and the NS Descriptor (NSD) of the NS (which **MANO does**):
- The descriptors are configuration models written in YAML or JSON
- The **VNFD** contains information about a single VNF. *It is used by the VNFM during the instantiation process* and the management lifecycle of the VNF
- The **NSD** is used to describe in detail the structure of the NS, and the interconnections between all VNFs.
Once the descriptors are created, it is possible to upload them inside OSM

We may want to chain VNF together so that each packet follows a strict path, and thus create a **Service Function Chain (SFC)**.
## Networking Slices
In case of a Softwarized Network, a NS is represented by a VNF Forwarding Graphs. An instance of a FG is called a **Network Slice** (implementation of a network service, represented by a slice). The creation of a network slice means solving a problem of optimization, so that we select the optimal place to instantiate a VM, the correct resources and the optimal network interconnection.

==This is an NP-Hard problem, and the Orchestrator is in charge of solving it.== The orchestrator doesn't have a global view of the system, but it just knows the overall characteristic of the datacenter -without knowing server type/count etc-, abstracting it.
![|500](https://lh7-qw.googleusercontent.com/slidesz/AGV_vUeRsKx_vtaZFX7ial8KCsvT66ZBMLsWyxbtoYwKF2dHDr6XGnyRkfllNPXMscZmiaXlt37UgjPUVd38NWPeQDeWKRiYghuyoh4lvmK69KIDwxCHKYg0iHUbh1wcCwdXZFWfg5i4TlEuoqd51eEZTebmt24RSWA=s2048?key=80oXZdpB5R4FDi2LBo6BkQ)

To find a "good enough" resource allocator we'll use a greedy heuristic algorithm, which will find a locally optimal association. We use the greedy heuristic algorithm called **AVMVPH**, which runs in polynomial time. Works on two steps:
- Maps the VNFs leaving the smallest processing capacity available[^1]
- Once mapping is complete logical links are mapped in the Substrate Graph by choosing shortest paths.
## Service Function Chaining (SFC)
This new way of thinking of the network in terms of NFV and SDN opens up a new way to do networking, based on softwarized components:
- VNF can be activated and deactivated on the spot
- VNFs can be moved in the cloud however they find it best fit
- Connectivity among them can be designed on the fly by means of SDN
### What is it?
Service Function Chain (SFC) may be defined as the sequence of VNFs that a packet (or flow of packets) must traverse. An SFC is not a simple forwarding: a flow can *bounce* off the same VNFs on the same ports without creating conflicting situations (it's stateful, meaning that the Packet Forwarding must store the packet history).
As it's VNF and NS, SFC is an Overlay architecture, unaware of the underlay build with p2p nodes. To do this, *the overlay can use packet tunneling techniques such as IPsec which connect to SFFs*.
### Logical Service Plane Elements
- **SFC Classifiers**: Classifies the incoming traffic based on policies, and adds the correct SFC header with SFP Identifier
- **Service Functions**: They are responsible for processing the packets along the chain. They may be SFC aware or not, depending on if some SFC information needs to be processed.
- **Service Function Forwarders**: Responsible to forward traffic from one Service Function to another, according to the SFC header
- **SFC Proxies**: Responsible to rempove and insert SFC-related encapsulation data on SFC-unaware Service Functions.