# Exam 3 February 2023

## Q1. Authenticity vs Authentication

Authenticity refers to the branch of connecting an object to the rightful owner. An object is "authentic" if the creator of the object is the one which is assumed to be.
Authentication refers to the branch of checking the validity of the identity presented by a user, o a computer.
Authentication contains authenticity, since we want to check if the object creator is the rightful owner, so if the identity provided is authentic.

## Q2. Symmetric Encryption vs Decryption

1. OFB, or Output Feedback, is a way of encrypting a file that contains more than one block. Decryption works pretty much the same. Both times is important to use the same Encryption algorithm. It can be used with any block encryption algorithm, and it's based, on these steps
    - a random Initialization Vector is chosen, and is encrypted by the algorithm an the private key. The output now does two things:
        - Gets inserted as the input of the next step
        - gets XOR-red with the plaintex block $M_1$ to create the first Cypher blcok $C_1$
    - Algorithm continues until the last block is encrypted.
2. Randomization helps lots in the algorithm, since it adds entropy to the system. A stolen preprocessed sequence of encrypted IV could be used to decrypt a cyphertext, even without know knowing the key, and this breaks the usefulness of a good encryption algorithm.
3. KDF, or Key Derivation Function, is a class of functions that aims to create a key from a passphrase, a password or whatever variable-lenght set of characters. This helps humans on various parts of Security, since it helps them with a way easier to remember set of characters without needing to remember a 128, 256 or whatever lenghy key.
4. we can divide the command in two different parts:

    ```bash
    echo "SilverSurfer" -n
    ```

    this commands prints on *stdout* the string provided in the parameters. The *-n* removes the newline.

    ```bash
    openssl enc -aes-128-cbc -p -out out.enc
    ```

    this part gets data that he got from *stdin* (piped from previous stdout *echo* command) and encrypts with AES, with a 128-bit key, and with a Cypher Block Chain mode of operation. The key will get derived (with KDF) from the user's passphrase, and will output the encrypted cyphertext on the output's file *out.enc*, and on stdout it'll print the key and IV used.
5. On CBC mode of operation this would corrupt the plaintext relative to the modified ciphertext block, and the plaintext after this.
6. A flipped bit on the plaintext is just another plaintext.

## Q3. Digital Certificates

1. Certificate Revocation Lists are a document, released from Certification Authorities (CA) that contains a list of Certificates Serial Numbers that have been invalidated before their expiration date. They are released usually every two weeks, and this means that before knowing a user certificate is invalidated it could pass lots of time. Ai Spik Inglisc porcodio. Online Certificate Status Protocol is a way to check the validation status of a certificate in real-time by probing the CAs website.
2. OCSP Stapling is a way to not generate incessant traffic on CAs servers. When surfing the web, certificates are checked often, even multiple times for every website, and this would basically create a Denial Of Service. For this, the OCSP status is signed and appended on the certificate itself, for which has a limited lifetime.
3. Although the webpage is not digitally signed, the actual certificate downloaded from it is. Also, if the document would be hosted on an HTTPS website, we'd need to check for that certificate validity.

## Q4. Digital Signatures

1. Usually companies that require these kinds of double signatures on a document don't mind about the difference, even tho there is one: in the first case both sign the document, while in the second case Bob signs both the document along with the fact that Alice signed it, which is different from signing the document by itself.
2. If verification fails on a document then we can't be sure of multiple points:
    - **Integrity**: The file could have been compromised by a malicious third party or by a corruption;
    - **Authenticity**: The file has not been signed by the user which is the owner of the signature, the certificate used for signing violates policies, or that it has been invalidated.
3. First, how did Alice gain access to a certificate of her identity without knowing her public key (which is also contained in the certificate itself)? Also, to sign a document we need a private key, for one would need to know the public key (since it directly derives the private key).

## Q5. Firewalls

1. Blacklisting is basically blocking everything, while the rules allows specific traffic, that matches at least one rule, to pass through. Whitelisting is basically the inverse of this: allowing everything while blocking specific rule-defined traffic.
2. We'll write a set of iptables commands to do what's requested:

    ```bash
    # Blocks all inbound and outbound traffic to/from the firewall
    iptables -P INPUT DROP
    iptables -P OUTPUT DROP

    # We will assume that eth0 is the network card that connects LAN, and eth1 connects to the WAN
    iptables -P FORWARD ACCEPT
    iptables -A FORWARD -i eth1 -o eth0 -p tcp -m state --state NEW -j DROP 
    ```
