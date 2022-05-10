# Challenge Name: diffie-hellman

## Question

![[CTF2022/picoCTF2022/Cryptography/diffie-hellman/Question.png]]

In this challenge, we're provided a message and two hints to decrypt it. 
`H98A9W_H6UM8W_6A_9_D6C_5ZCI9C8I_JBACIFAI`

```
Hints 1: Diffie-Hellman key exchange is a well known algorithm for generating keys, try looking up how the secret key is generated
According to the challenge title given, we can know that this challenge is related to the diffie-hellman. 

Hints 2: For your Caesar shift amount, try forwards and backwards.
```


## Solution
To solve this question, you have to know the formula and concept of the diffie-hellman. Diffie-hellman is a method of key exchange to let people exchange the cryptographic key over a public channel. Then, the key can be used with symmetric key algorithms to transmit information in a protected manner. In this challenge, we need to find out the secret key of Alice and Bob with the details provided. 

Check out more about Diffie-Hellman - https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

The challenge description have provide the following details:

p = 13
g = 5
Alice (a) = 7
Bob (b) = 3


According to the link above, we can know that 
p = public (prime) modulus
g = public (prime) base
a = Alice's private key (only visible for Alice)
b = Bob's private key (only visible for Bob)
A = Alice public key
B = Bob public key

First, we need to find out the A and B public key with the formula: 
A = g^a mod p
A = 5^7 mod 13
A = 8

B = g^b mod p
B = 5^3 mod 13
B = 8


After that, by using the private key provided and the public key calculated, we can find the secret key of Alice and Bob using the same formula.

sa = B^a mod p
sa = 8^7 mod 13
sa = 5

sb = A^b mod p
sb = B^7 mod 13
sb = 5

That's how I found out the secret key of Alice and Bob, which is 5. 

To solve this challenge, we got the second hints, which is use the Caesar Cipher shift backwardly. For example, H backward 5 times is C, 9 backward 5 times is 4, and so on. 

In this case we use the sequence of the Caesar Cipher: 
ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Finally, you'll got the message:
C4354R_C1PH3R_15_4_817_0U7D473D_E657DA5D

## Flag
That's the flag !
`
picoCTF{C4354R_C1PH3R_15_4_817_0U7D473D_E657DA5D}
`



