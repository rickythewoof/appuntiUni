# Exam 8 September 2022

## Q1. Collision Resistance

1. A hash function $H$ is *weakly collision resistant* if it's computationally hard to calculate, given a message $m$, another message $m\prime \neq m$ such that $H(m\prime) = H(m)$. A hash function is *strongly collision resistant* if it's computationally hard to find a pair $<m, m\prime>$ such that both have the same hash
2. We can prove this by proving the inverse, since !*strong* -> !weak:
If we found a polynomial-time function $F$ that, given a message $m$ returns another message $m\prime$ s.t. $H(m) = H(m\prime)$, then we would be able to arbitrarily create pairs $<m, F(m)>$, thus breaking strong collision resistance requirements.
3. It's not because it fails on being a  collision resistant function. given the result of this hash function, it's easy to find multiple colliding pairs.

## Q2. RSA

1. RSA is used to encrypt data when there is no agreed-upon session key.
2. RSA uses two pair of public and private keys. The public is the one used to encrypt message and to verify signatures, while the private is used to decrypt and sign messages. The encryption key $e$ is chosen by being relatively prime with the euler's totient function on $N = p*q$, while $d$ is chosen such that $ ed \equiv 1 \bmod (p-1)(q-1)$. It's computationally hard to find $d$ without having both primes $p$ and $q$
3. OS2IP is what creates from an octet stream of bytes to the actual message that has been encrypted.

## Q3. Authentication

1. SPEKE is a password-based authentication mechanism in which there are two users.
Alice (a normal client) and Bob (a server). Alice needs to authenticate herself using a shared secret, all while being sure to not disclose information that could lead to her identity being stolen. Bob and Alice agree upon a secret derived from the password and the prime p used to generate a session key. After that Diffie Hellman is used, with base W and prime p.
2. Authentication is made by sending the credentials using the secured TLS channel on the authentication server. The server checks the credentials, and if they match to a user it generates a session cookie (a sort of ticket granting ticket) valid for the entire duration of the session.

## Q4. Differences between key and password

A password is a type of value created by humans and thought for humans. it's easier to remember and it can be of a fixed lenght. A key is a sequence of bits, it's not encodeable in a string of characters and is bound to a fixed size. A key can be derived from a password by using a KDF.

## Q5. Eavesdropping IPSec packets

An IPSec packet provides security at the network level. Granting that we're using ESP headers we have partial confidentiality over the IP packet. Given how the internet works it would be impossible to interpret an IPSec packet, so informations about the destination IPsec provider will always be visibile, along with informations about the ESP header in itself.

## Q6. Timestamps in cryptographic protocols

Timestamping a message is a great way to add another level of protection against replay and reflection attacks, as those would get invalidated by using information for which too much time has passed. However we need to be sure when and how to use it. Timestamps are very susceptible to desynchronization (which could be accidental or also part of an attack), and in fact X509 Authentication Protocol uses three-way authentication when we can't be sure of the clocks being synchronized.

## Q7. Timestamp Authority

1. A TSA is a certification authority that grants digital signatures of a timestamp. It's useful to legally prove that a document has been created not before that time.
2. A user interested in timestamping its file can send the hash of the file, and the TSA will answer back with the hash, the timestamp and the signature of these two components.

## Q8. Firewalls

1. A personal firewall is a host-based one, it's meant to protect the traffic coming from and going to a single host. A Perimeter firewall is meant to protect an inner LAN from the traffic of an outer portion of LAN/WAN.
2.

```bash
# It makes way more sense to use a blacklisting policy
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD ALLOW

# This makes sure that the only traffic possible is when a packet for the PC is coming from inside the network.
iptables -A INPUT -i eth2 -p tcp -m state --state NEW,ESTABLISHED -j ALLOW
iptables -A OUTPUT -o eth2 -p tcp -m state --state ESTABLISHED -j ALLOW 
```
