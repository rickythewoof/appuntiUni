# Internet of Things security
### IoT Introduction
> "Cyberphysical ecosystem of interconnected sensors and actuators which enable intelligent decision making"

We'll talk about:
- **sensors**: Elements that allow to monitor the environment and the context on which IoT systems operate. They collect information about the network, applications but also the physical world.
- **actuator**: Entity responsible for moving and controling a system or mechanism, interacting with the environment.
Usually IoT devices run on **embedded** hardware, designed for low power. Has non-volatile memory, and a way to have **connectivity** (BLE, Wifi, LoRa, Zigbee ... )

Number of IoT devices GREATLY surpassed the number of humans.
## IoT Assets
We need:
- **Infrastructure** : Gateways, Routers, Power Supplies, Security
- **Applications and Services** : Data Analysis, Devices Management, Usage
- **IoT Devices** : Hardware, Software, Sensors, Actuators
- **Communication** : Network and Protocols
- **Information** : At rest, In transit, In use
### IoT Security
IoT security is often weak. Caused by the (sometimes not so) low power, and from an outdated system design. Started with basic security, now better, but devices from early design are still out there and used in compatible fall-back mode. Legislations and stronger security frameworks got put in place just around 2020.
## Stuxnet
Malware created to sabotage Iranian Nuclear Program, and it worked, slowing down development by $\approx$**4 years**. The Iranian project used the plans of an old French Nuclear Power Plant, and so they were implementing an already outdated system.
It exploited the *Programmable Logic Controller* and its software Siemens Step7, to make the centrifuges run at wrong speeds, thus ruining refinery processes.

Although the system was airgapped, and so external connections were blocked, initial spreading factor was through USB devices (and the `autorun.inf` file) and after first infection there was internal network spreading technology, exploiting Windows Print Spooling techniques.

It's a fire-and-forget weapon, and even though just the power plant was the target, it spread elsewhere as collateral damage.

1. Attacks SCADA system MATIC WinCC, by connecting to its database server with hardcoded credentials, by sending malicious SQL code to change view. It was the first known SCADA system to be specifically targeted by malware.
2. Once WinCC gets infected it goes into the step 2, which infects Step7 Software and its project files
3. The final target is the PLC, that was modified so it run at arbitrary speeds while still keeping the sensor values in check. 
## Mirai Malware
Turned IoT Linux devices to remotely-controlled bots used in big botnets. Primarily targeted online consumer devices and cheap home routers. It infected over 60k devices in 20 hours.
Main uses of botnets are:
- **Distributed denial-of-service attacks** (Most popular)
- Spamming
- As a worm
- Manipulating polls / spreading misinformation
- Sniffing traffic
- etc..
### Stages of Dyn DNS Provider attack
1. **Infect the device** by scanning for IoT devices that are accessible over the internet, specifically ports `22`, `23`, `5747` etc.. Once connected it brute-forces default user-pass to login on the device
2. **Protect itself** by killing other processes running on the devie to prevent the owner from gaining remote access once again. It's tethered, meaning that a reboot will remove the malware, but it can be become infected again.
	- Particular note is that it contained a list of known networks in the US to not attack, like the DoD, and the Postal Service
3. **Launch attack** (whenever the Command&Control center orders it). It worked by sending both HTTP and SYN floods. Consisted of sending 21 short-lived attacks of 25 seconds each, and 2 long attacks.
Since we have the [source code](https://github.com/jgamblin/Mirai-Source-Code/) Mirai is constantly changing, and in the Github there are around 3.5k forks!
## Challenges in IoT
We have some big challeghes:
- Very large attack surface, and widespread deployment. The idea of needing an extensive layer to support IoT operations means that each one of them can be hacked.
	- **Sensing laye**r: Sensors can be hijacked to spread false informations
	- **Network layer**: Like all networks, this layer can be subjsect to attacks such as DDoS, Spoofin, rerouting, ...
	- **Middleware layer**: MITM, SQL, Cloud malware injection
	- **Application layer**: Code injection in-app, access control attacks
- Very limited memory/energy requirements/computational power, which further decreases the overall safety of the product. For example, we can do sleep-deprivation attack to drain battery faster
- Cheap devices with very little security in mind flood the market.
### CIA Triad
1. **Confidentiality**: Protection against unauthorized access to or use of confidential information. It may considered sometime as the same thing as _privacy_.
2. **Integrity**: Ensure accuracy and completeness of information to protect business processes.
3. **Availability**: Information and vital services should be always accessible when required.
### OWASP - Top 10 IoT Risks
1. ==use of weak, guessable and hardcoded passwords.==
2. Insecure or unnecessary network services running on the device itself, like Telnet on a app-controlled camera.
3. Insecure Ecosystem interfaces 
4. Lack of a secure update mechanism
5. Use of insecure or Outdated components
6. Insufficient Privacy protection
7. Insecure data transfer and storage
8. Lack of Device Management
9. Insecure default settings
10. Lack of physical Hardening
# Attestation
The natural solution to check for unauthorized binary modifications.
## Remote Attestation
It's a protocol whereby a challenger `Chal` verifies the internal state of a `Prov` device. We want to allow an honest `Prov` node to create an attestation certificate for `Chal` to prove it's in an expected state.
We have two ways to do RA on a device

|      Type      | Meaning                                                                                                                                                                                                      | Pro                                                                 | Cons                                                                                                                                                                                            |
| :------------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Software-based | The attestation program is inside of the "normal" memory. Relies on a challenge-response approach.                                                                                                           | No special hardware is required                                     | If execution can be interrupted then it's impossible to guarantee attestation. It's not strong wrt physical attacks. It's a time-bound attack, so not possible in multi-hop networks.           |
| Hardware-based | Attestation is based on the use of two hardware modules:<br>- **Secure Boot**, to check for unaltered system integrity at boot time<br>- **Trusted Platform Module**, which can be accessed using fixed APIs | Hardware-based solution guarantee a safe code execution environment | Initial implementation of hardware devices can be costly, but now a secure enclave is present even in embedded chips. Implementing tamper resistancy on low-end hardware is not cost effective. |
### Software-based attestation
#### SWATT: SoftWare ATTestation
Based on a 2004 paper. Verifier sends a challenge (using a nonce prevents the replay attack), when the prover sends back a response that contains a memory-content-verification procedure. Based on a protocol `P` comprised of following components:
- $Setup(1^n)$: probabilistic algorithm that, given security parameter $1^n$, outputs a long-term key $k$
- $Attest(k;s)$: deterministic algorithm. Given a key $k$ and a device state $s = (s_p, s_v)$, returns an attestation token $\alpha$ 
- $Verify(k;s;\alpha)$: deterministic algorithm that, given $k, s, \alpha$ returns 1 iff $\alpha$ corresponds to $s$
It's a verification algorithm that basically works by asking the device for a part of known memory content, and expecting to receive back the response within a very strict time-manner.
Purely software-based, but an attacker can replace the verification code with a malicious one. Attacks can be based on redirecting the attestation challenge to a trusted software to get the proper result, but even a simple `if` in the assembly code returns a 13% overhead, which is detectable!
> [!NOTE]
> SWATT is time-based, in which we have a strict time-bound response, and it's not feasible in multi-hop distance

#### SCUBA: Secure Code Update By Attestation
The idea is to *securely recover original code* in the presence of a malicious code. The base station should have complete knowledge of all devices, down to the memory. We have an assumption of using public-key cryptography, which on embedded nodes can take a lot of time! 
> [!WARNING]
> In remote attestation, **TOCTTOU Attacks**, which are time-of-check-to-time-to-use, use the idea that the time between the device attestation and the unaltered code execution cannot be checked!
#### SCUBA-ICE: Indisputable Code Execution
We have untampered code execution, where we check the integrity of the executable and set up an untampered execution environment in which code execution in guaranteed to be atomic and no other code is authorized to run. 
We will then run Indisputable Code Execution, which is selfchecksumming and will check the untamperedness of the code in a timely manner. We may want to collude ICE by *Checksum forgery* or by *Speed attacks*.
### Hardware-based attestation
The idea is to have a trusted, hardware-based platform so that attestation can be done. Schemas for attestation can be:
- Platform Integrity:
	- **Secure boot**: Verifies the system integrity at boot time, with immutable bootloader stored in ROM along with a public key, with which code signature its checked
		- Uses **Trusted Platform Module** which is a cryptographic module. Has platform configuration registers (PCR), accessible via fixed api, and with a cryptographbic hash it's linked one through each other. TPM gets wiped clean at every boot
	- Authenticated boot
- Secure storage
- Isolated execution
	- Trusted Execution Environment
#### Necessary componens
- **Attestation Read Only Memory**: needs to be inside the MCU
- **Secure Key Storage**: Memory region should be inside the CPU, and can be only accessed through attestation code in ROM
- **Memory Control Unit** access control: Control access to the K.
- **Reset and Memory Erasure**: If any error is reported, we perform a hardware reset of the MCU, which will enforce a memory cleanup.
#### SMART
Uses the secure key storage and the memory control unit to -given a challenge- probe the memory in a secure manner, and respond accordingly, sending back the response.
## Hybrid attestation
Hybrid attestation uses the fact that we can run software attestation code in a trusted execution environmnent to probe untrusted software, by means of digital signatures. Prover and Verifier share a common key $K$, and has a random nonce $N$.
The Verifier sends out a nonce $N$, then the device hashes the contents of the untrusted software, and sends back a $\delta = MAC_k(HASH || N)$. The verifier, once received $\delta$, does the same calculations over a trusted device and produces $\delta^\prime$. If $\delta = \delta^\prime$ then the device has been verified correctly
#### TyTAN : Tiny trust anchor for tiny devices
Since designing a completely trusted CPU is expensive, the goal is to design a cheap and secure architecture for low-end embedded system that provides:
1. Hardware-assisted dynamic root of trust
2. Secure inter-process communication
3. local and remote attestation
4. real-time guarantees
![[Pasted image 20250424155054.png]]
Has a real-time OS to manage all of the secure tasks. It's more of a security framework, along with a complete OS, than an algorithm.
### Attestation vulnerabilities
1. Denial of Service
2. No authentication of verifier
3. Sleep Deprivation (to drain battery)
Some mitigation may be checkign that the the verifier and the prover has syncronized clocks, and in ase of software adversary hardware must guarantee the tusted platofm, and confidentiality of key. Adversary may know when the attestation is finished.
## Device Attestation
The idea behind the use of device attestation is the fact that we may want to do an in-device attestation procedure, without the need of an external party requesting it. This is the idea, in a sense, behind Secure Boot. The attestation result can then be, in theory, sent to a secure server so that it can be securely monitored.
#### SEDA: Secure Embedded Device Attestation
Attestation is done over a spanning tree, where each node attests its children and reports to its parents.
Pros is that it scales logarithmically, and that it uses symmetric key criptography which is more efficient, generally.
There is a security assumption: A secure server is storing the symmetric key, which is BAD. In general, we assume that in this system an attacker is only software.
If the shared key gets compromised, along with a non-leaf node, an attacker can arbitrarily change the attestation result of itself and it's lower branch.
#### SANA: Secure Aggregate Network Attestation
Similar enough to SEDA, but with the difference that non-leaf devices are called *aggregators*, which may or may not be part of the devices to be verified. This method also adds security wrt physical attacks. 
The idea is that only provers need to have Trusted Execution Environments, and since the result is signed an aggregator cannot modify it. At most it can just block the sending back of the message.
#### DARPA: Device Attestation Resilient to Physical Attacks
The idea is to broadcast a regular heartbeat to each neighbour, so that every device monitors each other so that TOCTOU attacks are less possible. In the case of a device becoming silent, compromission is assumed. 
In case of an attestation request we can use whatever algorithm, like SEDA, to check.
##### Pro/Cons
It's able to address physical attacks and also software ones; however it's not suitable for dynamic networks and details of compromised devices are not present in attestation reports.

To deal with the issue of dynamic networks with devices that change position we will use a new paradighm based on talking with neighbours, more than trees
#### PADS - Practical Attestation for Highly Dynamic Swarm Topologies
Maybe we don't have a static tree-like structure over a more dynamic structure. We consider the use of **self-attestation**,  and then "consensus" among device to corroborate attestation results, in a gossipping matter. We have some device requirements:
- **Read-Only Memory**
- **Memory Protection Unit**
- **Secure RTC**
Entities of PADS are that only hte provers require a trusted execution environment, where each one creates an *attestation proof*, which is a hash value of the underlying software that gets shared with other nodes in range (so that every device has assigned 2 bits and (good - 10, bad - 00, unknown 11), while verifiers attest individual nodes before getting knowledge about the network.

**Consensus** over the state of the network is done through the sharing of the attestation array (2 bits per device). Once a device gets another attestation array it ANDs it with itselfs and saves it.
We use the AND so that a bad device will always remain bad, even if all but one have it certified as good.
#### Bloom Filter
A space _efficient probabilistic data structure_ that uses the idea of PADS, by using multiple hash functions to select the position of a single element.
When we want to check a device we just recompute the hash values and check the positions. We use probabilistics, since multiple nodes may have written values in the same position. 
With this data type we will never have false negatives, since if we have a 0 for just one of the positions for an object we will know it's not there. (by having 1 on the compromised devices we know that we will never have false negative, better to consider it 100% safe iff none of the bits associated to a device is set to 1).
![[Pasted image 20250508160015.png|450]]
##### Why?
We can estimate how many elements have written in the filter by using $\displaystyle z= -\frac mk\ln[1- \frac X m]$ 
Has an advantage to have a fixed-size list while having a good resiliency wrt device addition, but it cannot be sure if a specific device is compromised.
We need a trusted Real-Time-Clock to keep synchronization over the entirety of networks

*From the bitmask verifier we can estimates the number of compromised devices and know (with uncertainty) if one is compromised or not*
#### SALAD: Secure And Lightweight Attestation of Dynamic Networks
We can use public key cryptography (with broadcast of challenge-responses), which ==has a very big overhead but it's way more resilient== since physical attack of a device doesn't compromise a shared common key.

In all of these scenarios, an adversary can always choose to not participate in the protocol, but it's easy to overcome since it may want to participate to other activities.
# IoT Authenticator
There are several Physical Level Security authentication protocol emerged. Use of passwords can be good, but it may not be enough because of the use of a default password. 
Studies are trying to create a unique password at the physical layer, analyzing unique features of the device that authenticates it uniquely. We have 4 main approaches:
- Comparison of the properties of the physical channel
- Third party authority using XOS and simple multiplication operation
- Using secret keys derived from the channel for encryption
- Concepts of tags generated with encryption or hashing
## PUF - Physical Uncloneable Function
We can use PUFs, which are chips with nanoscale variations, that use their inherent silicon uniqueness to create a fingerprint. That is turned into a strong secret cryptographic key.
Such ==nanoscale variations are noisy by their nature==, so the behaviour can be unexpected.
We resolve this by using a multifactor mutual authenticatory with fuzzy systems. 
1. A PUF provides a key randomly generated $N$, which gets fed into an algorithm $Gen(N) = (\tau, \sigma)$
2. At authentication, a PUF will provide another key $N^\prime \neq N$, which will get fed to $Rep(N^\prime, \tau) = \sigma^\prime$
3. if $\sigma = \sigma^\prime$ then the device is authenticated
We use fuzzy algorithm to counteract the noicy nature of the PUF.

GIven a mutual secret key, we can encrypt the key with the same AES-CTR module, so that we always have dynamic confidentiality keys.
With this we can guarantee:
- Indistinguishability
- Anonimity
- MITM attacks
- Replay attacks
- Masquerading
- Forward Secrey
# Security and Privacy Issues of UAV
UAV networks can be *centralized* in the case of a ground control station, or *decentralized* in which there may be one or more UAV backbones that communicate with each other to organize.
We may have different kind of issues concerning security:
- **Communication issues** : Usual network communication attacks (Eavesdropping, DoS, MITM ...)
- **Hardware issues** : Hijacking, Supply-chain attack, Sleep deprivation attacks, radio frequency module attacks.
- **Software issues** : Operating System attack, tampering signals, and System ID Spoofing.
- **Sensor issues** : GPS Jamming, which forces the UAV to do more choices, which can be injecting noise or spoofed signals. This can happen along other sensory-channel attack.
A good countermeasure way is to apply a ML-based IDS to detect, along with applying good security hygene.
# Security in VR - XR
Extended reality:
- **Augmented Reality (AR)**
- **Virtual Reality (VR)**
- **Mixed Reality (MR)**
Differences that we already know.
### Tracking sensors
1. Used for 3/6DoF motion tracking
2. Used for User Interaction tracking, like the eye/face/finger movement
3. Used for environmental tracking
## Privacy and Security Analysis
Risks are mostly related to privacy. Some of the data is highly private, so knowing how, when, where, and with who the data is captured is important.
We have three types of attacks:
- **Security Attacks**
	- Malware attack
	- Network attacks
	- Password Stealing attacks (application in background recording movements and so estimating the password)
- **Privacy Attacks**
	- De-anonymization attacks
	- Privacy of other users
	- Use of the non-protected sensor IMU data to retreive voice conversations.
- **Environment Attack**
	- Immersive Attacks, like chaperone shifting
	- Overlay attacks
	- Perception manipulation attacks
## Defense
Using a permission-based models, along with actuator noise and local differential privacy.
# Machine Learning Security
Machine Learning is a branch of Artificial Intelligence which bases itself on a training procedure to learn attributes from a class of objects. Little attention has been put on its security, which is an actual issue.

An attacker goal is to fool the classifier, for example by adding noise to an image, or sometimes even changing a single pixel of an image. Some examples are in the slides regarding changing pixels, or adding other images on top to fool a biometric-based authenticator.

The assumption is based on the fact that the training and test set follow the same statistic, and so stochastic noise isn't an issue.
An adversary **can use artifically generated noise** such that the training can be deflected.
We can carry out *supply chain attacks* based on this fact that we can have an attack surface for every task in the machine learning process
### Attacker knowledge
Does the attacker know the details of the classifier?
- **White-box attack**: the attacker would be able to have as mush knowledge as it needs to create the adversarial perturbation needed
- **Black box attack**: requires the attacker to explore the behaviors of the classifier, done by submitting probes
### Attack scopes
- **Targeted attack**: There is a particular class of objects $t$ of interest to misclassify
- **Untargeted**: It's of interest to find perturbations that can fool the model if applied to any input
## Attack vectors
- **Exploitation of empty regions**
- **Label poisoning**
- ...
### Backdoor Attacks
These are the types of attack where the attacker can poison the training set. This can be done by for example, applying a specific transformation or adding some specific pixels so that the NN recognizes it as whatever the adversary decides.
*Stealthiness is key*, given that a user may see the backdoor applied on the set before training
#### Taxonomy:
- **Single image trigger**
- **Static vs adaptive vs randomized pattern**
- **Visible vs invisible trigger**
- **Localized vs diffused trigger**
![[Pasted image 20250516124531.png]]
## Securing deep learning
- **Adversary-aware re-training**: An idea is that given a trained neural network on a set of datapoints, we can retrain it with the points closest to the threshold even closer
- **Outlier Detection**
- **Reverse Engineering the trigger of the backdoor**, possible only when the actual backdoor has been discovered.
- **Saliency map examination**: This is a particularly strong tool to detect backdoors, which consists on visually seeing the triggers for a given image for every node of the network. After analyzing this *pruning* can be applyed to remove the dormant nodes.