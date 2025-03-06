# Step 4: Implementing Feistel Rounds
#
# In the Feistel structure, each round consists of:
#
#     Expanding the right half (32 bits → 48 bits) using an expansion permutation.
#     XORing the expanded right half with a subkey.
#     Substituting the result using S-boxes (shrinking it back to 32 bits).
#     Applying a permutation (P-box) to the output.
#     XORing the result with the left half.
#
# Tables Needed for Feistel Rounds
#
#     Expansion (E) Table (Expands 32 bits → 48 bits)
#     S-boxes (8 substitution boxes that reduce 48 bits → 32 bits)
#     Permutation (P) Table (Rearranges 32-bit output)


# -------------- -------------- scraps -------------- --------------
# 1. Expansion (E) Table
#
# The right half is expanded from 32 bits to 48 bits.
# Expansion Table (E)

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

def expand(block, table):
    return [block[x-1] for x in table]


# -------------- --------------  2. XOR Operation -------------- --------------
#
# We XOR the expanded right half with the subkey.

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

# -------------- -------------- 3. S-Boxes (Substitution) -------------- --------------
#
# The 48-bit input is divided into 8 chunks (6 bits each) and passed through 8 S-boxes, which output 4 bits each, reducing the size back to 32 bits.
#
# Each S-box takes:
#
#     First & last bit → Row number
#     Middle 4 bits → Column number
#     It then replaces the value based on a predefined table.
#
# S-Box Tables

S_BOXES = [
    # S1
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 9, 3, 15, 6, 2],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 7, 5, 0, 14, 9, 12, 6]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 8, 15, 14, 9, 3, 0, 11, 1, 2, 12, 4, 10, 5, 6],
     [7, 11, 0, 13, 14, 1, 10, 3, 9, 5, 15, 12, 2, 8, 4, 6],
     [9, 5, 11, 0, 14, 2, 3, 12, 8, 13, 7, 4, 15, 10, 1, 6]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 15, 10, 1, 3, 6, 7, 9, 14, 2, 12, 0, 5, 11, 4],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 9, 0, 14, 2],
     [11, 1, 10, 13, 4, 7, 9, 5, 8, 15, 12, 14, 2, 0, 6, 3]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 15, 10, 3, 9, 8, 6, 0],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 14, 0],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 9, 10, 4, 5, 3, 0]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 1, 13, 0, 11, 3, 7, 4, 10, 2, 8, 12, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 8, 0, 6, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 15, 2, 8, 6],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 13, 0, 15, 10, 3, 5, 8, 6]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 9, 0, 14, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 13, 0, 15, 10, 3, 5, 8, 6],
     [13, 0, 15, 10, 2, 8, 7, 5, 9, 4, 11, 1, 12, 14, 3, 6]]
]


# -------------- -------------- S-Box Substitution Function -------------- --------------
def sbox_substitution(block):
    output = []
    for i in range(8):
        chunk = block[i * 6:(i + 1) * 6]
        row = (chunk[0] << 1) | chunk[5]  # First and last bit for row
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]  # Middle 4 bits for column
        sbox_value = S_BOXES[i][row][col]
        output.extend(format(sbox_value, '04b'))  # Convert to 4-bit binary
    return [int(bit) for bit in output]

# -------------- -------------- 4. Permutation (P) -------------- --------------
#
# After substitution, the output goes through a permutation (P-table).

# Permutation (P) Table
P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

def permute(block, table):
    return [block[x-1] for x in table]


# 5. Full Feistel Function
#
# Now, let's put everything together into a single Feistel function.

def feistel(right_half, subkey):
    expanded = expand(right_half, E)
    xored = xor(expanded, subkey)
    substituted = sbox_substitution(xored)
    permuted = permute(substituted, P)
    return permuted
