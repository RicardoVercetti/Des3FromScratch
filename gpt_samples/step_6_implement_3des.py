from step_1_Implement_DES_Functions import generate_subkeys, hex_to_bin
from step_5_implement_des_encryption import des_encrypt_block


# Step 6: Implement 3DES
#
# Now that we have DES, we can implement 3DES:
#
#     Encrypt with K1
#     Decrypt with K2
#     Encrypt with K3


def triple_des_encrypt(plaintext, key1, key2, key3):
    subkeys1 = generate_subkeys(key1)
    subkeys2 = generate_subkeys(key2)
    subkeys3 = generate_subkeys(key3)

    # Encrypt → Decrypt → Encrypt
    step1 = des_encrypt_block(plaintext, subkeys1)  # Encrypt with K1
    step2 = des_encrypt_block(step1, subkeys2[::-1])  # Decrypt with K2
    step3 = des_encrypt_block(step2, subkeys3)  # Encrypt with K3

    return step3


def main():
    import datetime
    time_start = datetime.datetime.now()
    print("start time →", time_start)
    plaintext = hex_to_bin("0123456789ABCDEF", 64)  # Convert plaintext to binary
    key1 = hex_to_bin("133457799BBCDFF1", 64)
    key2 = hex_to_bin("1122334455667788", 64)
    key3 = hex_to_bin("AABB09182736CCDD", 64)

    ciphertext = triple_des_encrypt(plaintext, key1, key2, key3)
    ciphertext_bin_str = "".join(map(str, ciphertext))
    print("Ciphertext (Binary):", ciphertext_bin_str)

    ciphertext_hex = hex(int(ciphertext_bin_str, 2))[2:]  # Removing the '0x' prefix
    print(f"Ciphertext (Hexadecimal): {ciphertext_hex}")
    time_finish = datetime.datetime.now()
    print("finish time →", time_finish)


if __name__ == "__main__":
    main()