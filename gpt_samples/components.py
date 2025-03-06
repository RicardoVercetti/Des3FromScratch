import step_1_Implement_DES_Functions as des_fn

# Function to convert a hexadecimal key to a binary list
def hex_to_bin(hex_key, size):
    bin_val = bin(int(hex_key, 16))[2:].zfill(size)
    return [int(bit) for bit in bin_val]


# ----------------- -----------------      notes       ----------------- -----------------

# int(str, int)             → Could have a binary string or a hex string in place of 'str'
# eg:
#   int("101", 2)           → '2' for binary to int conversion
#   int("1A3", 16)          → '16' for hex to int conversion

# bin(int)                  → Integer to binary conversion

# string.zfill()            → pad a string with leading zeros until it reaches the specified length


# ----------------- ----------------- working section ----------------- -----------------
print("Runs...")
# print(des_fn.hex_to_bin("112233445566", 64))

# print(int("str", 2))
# print(int("101", 2))  # Output: 5 (binary 101 → decimal 5)
# print(int("AB", 16))   # Output: 10 (hexadecimal A → decimal 10)


# print(bin(171)[2:].zfill(10))
# print(bin(171)[2:])
print(bin(171))
# print(bin("171"))