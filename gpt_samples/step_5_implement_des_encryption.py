from step_4_feistel_rounds import feistel, permute, xor
from step_1_Implement_DES_Functions import IP, FP

# Step 5: Implement DES Encryption
#
# Now that we have Feistel rounds, let's apply 16 rounds of processing.

def des_encrypt_block(plaintext, subkeys):
    # Initial Permutation
    permuted_text = permute(plaintext, IP)

    # Split into left and right halves
    left, right = permuted_text[:32], permuted_text[32:]

    # 16 Rounds of Feistel function
    for i in range(16):
        temp_right = right[:]
        right = xor(left, feistel(right, subkeys[i]))  # Apply Feistel function
        left = temp_right  # Swap left and right

    # Final Permutation
    final_block = permute(left + right, FP)
    return final_block
