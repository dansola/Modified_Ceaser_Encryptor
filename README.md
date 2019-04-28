# Modified Ceaser Encryptor GUI
Modified ceaser encryption software allowing for easy decryption.

# Overview
The action of a Caesar cipher is to replace each plaintext letter with a different one a fixed number of places down the alphabet. The cipher illustrated here uses a left shift of three, so that (for example) each occurrence of E in the plaintext becomes B in the ciphertext.

![alt text](https://github.com/dansola/Modified_Ceaser_Encryptor/blob/master/Images/Caesar_cipher.png)

Traditionally, to decrypt a Ceaser cipher, one would need to produce various decryptions based on the number of shifts and select which one seems most reasonable.  To make the decryption process easier, this modified Ceaser encryptor outputs the number of shifts after each encrypted character.  This way, a decryption algorithm can easily decrypt an encrypted password.  In this software all uppercase and lowercase letters can be used along with all numbers and the following special characters: 

~\`!@#$%^&*()+=_-{}[]\|:;’?/<>,.

To increase the difficulty of a human realizing the pattern of this modified Ceaser algorithm, the letters, numbers and special characters were all shuffled.

# GUI Examples

Valid Encryption/Decryption:
![alt text](https://github.com/dansola/Modified_Ceaser_Encryptor/blob/master/Images/Encryption_Example.png)

Invalid Encryption/Decryption:
![alt text](https://github.com/dansola/Modified_Ceaser_Encryptor/blob/master/Images/Invalid_Example.png)

As seen in the image above, a user is not allowed to encrypt a password containing spaces or other invalid characters.  Similarly, the user is not able to decrypt an invalid encryption.  The encryption is considered invalid of it contains invalid characters, or if a number does not follow a character.
