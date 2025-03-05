# Understanding 3DES
# 3DES uses three 56-bit keys (168-bit in total).
# It applies the DES algorithm three times:
#     Encryption: Ciphertext = DES_Encrypt(DES_Decrypt(DES_Encrypt(Plaintext, K1), K2), K3)
#     Decryption: Plaintext = DES_Decrypt(DES_Encrypt(DES_Decrypt(Ciphertext, K3), K2), K1)

# Step 2: Implementing DES
# Since 3DES is based on DES, we need to first build a basic DES encryption function.
# 1. DES Key Schedule (Generating Subkeys)
# DES uses a 64-bit key, but only 56 bits are used. The key is permuted and split into left and right halves. We then generate 16 round keys.
# 2. Initial and Final Permutations
# The plaintext undergoes an initial permutation (IP) before processing and a final permutation (FP) at the end.
# 3. Feistel Network (16 Rounds of Processing)
# Each round consists of:
#     Expanding the right half from 32 bits → 48 bits.
#     XORing it with the round key.
#     Substituting through S-boxes (Shrinks 48-bit back to 32-bit).
#     A permutation and merging with the left half.
# 4. Reverse Steps for Decryption
# Decryption is the same as encryption but with reversed subkey order.

# Step 3: Implementing 3DES
#
#     Encrypt the plaintext using DES with key K1.
#     Decrypt the result using DES with key K2.
#     Encrypt again using DES with key K3.












print("This runs too...")