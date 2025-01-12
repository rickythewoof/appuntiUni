# Exam 19 January 2024

## Q1. Hashing

| Question | Answer |
| --------------------- | :---: |
| Strong resistance -> Weak resistance | **Y** |
| Weak resistance -> Strong resistance | **N** |
| unkeyed more secure than keyed | **N** |
| F1(F2(x)) has more collisions than inverse (*) | **N** |
| Is H(x) = $x^2$ cryptographic? ? | **N** |

## Q2. Digital signatures

1. RSA Digital signature would have the following steps:

    - hash PDF document and sign the document with your private key following PKCS directives
    - Include certificate in the signature
    - use PaDes or Cades for attaching signature in the pdf document itself, or create an envelope for adding the signature and certificate
2. ElGamal vs DSS

    | Properties | ElGamal | DSS |
    | --------------------- | :---: | :---: |
    | Uses cryptographic hash function | **Y** | **Y** |
    | Is ISO and FIPS standardized | **N** | **Y** |
    | Includes standards on the hashing process | **N** | **Y** |

## Q3. Symmetric encryption

1. because going from A to 2A with the same key is linearly computational efficient. Bruteforcing a key has the same computational cost.
2. It's bad because this breaks perfect cypher theorem. If the stream is reused, $Pr(P | C) \neq Pr(P)$.
3. The commands encrypts the file *file.txt* given on the input, using AES and with a 128-bit key, using CBC mode of operation. It asks for a passphrase on the *stdin*, then prints the key and IV used on *stdout*. The file gets encrypted using the printed information and saved as a file called *file.txt.enc*
4. It doesn't make sense to use a cryptographic hashing function as a method of encryption, for two main reasons:

    - It's a One-way function, so it's computationally impossible to get back the file from the hash by itself.
    - Its vulnerable to forgery attacks.

## Q4. iptables

1.

    ```bash
    iptables -P [FORWARD/INPUT/OUTPUT] [ALLOW/DROP]
    ```

2. the following command is an iptables rules in which a rule gets inserted on top of the INPUT chain. It matches with the packets coming from a service (that have ports 0:1023) and that they're going to a user process (the others). The rule is applied if it matches the port directive and if it's for the loopback interface. If it matches it drops the packet.
3.

    ```bash
    iptables -I INPUT -i eht0 -s 192.168.7.2/24 -p tcp -m state --state NEW -j DROP
    iptables -I OUTPUT -o eth0 -d 192.168.7.2/24 -p tcp -m state --state NEW -j DROP
    ```

## Q5. Authentication

1. A replay attack involves an attacker intercepting and reusing a previously transmitted message to deceive a system. Examples include:
An attacker intercepts a user's authentication token (e.g., a cookie or session ID) and reuses it to gain unauthorized access. An attacker intercepts an encrypted authentication request and replays it later to gain access. 
2. Using nonces and timestamp. Too lazy to write here, in case please send PR.
3. They are precomputed tables containing the hash values of a large set of possible plaintext inputs (e.g., passwords). They are dangerous because they allow attackers to reverse-engineer hashed passwords quickly by comparing stored hashes to precomputed values, bypassing the need for brute force.
4. It occurs when an attacker gains access to a database of hashed passwords and systematically compares each hash against a dictionary of possible plaintext passwords (e.g., common passwords). This attack does not require direct interaction with the system, making it fast and difficult to detect.

## Q6. Short questions

1. We can use the property of the Euler's quotient function. Given prime p = 7, $\phi(7) = 6$.

    $2^{100} \bmod 7 = 2 ^{6*16}*2^4 \bmod 7 = 2^4 \bmod 7 = 2$.

2. TLS operates at transport level, IPsec at network level. IPsec can encrypt both the payload and the headers of the packets, while tls can encrypt only the payload. Both provides authentication and confidentiality. TLS is used to secure internet comunications. while IPsec is used to secure VPN and host to host transmissions.
3. A perfect cipher is one that, given a ciphertext generated through the cipher function, doesn't show information about the plaintext used to generate a ciphertext. Mathematically speaking, given P and C, $Pr(P) = Pr(P | C)$.
