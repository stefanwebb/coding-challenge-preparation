# Q1.1

# First solution
def is_unique(s):
    chars = {}
    
    for c in s:
        if c.isalpha():
            chars.setdefault(c, 0)
            chars[c] += 1
    
    return max(chars.values()) == 1

"""
Notes on solution

Rather than keeping counts of each character, can use hash table/bit vector. General message: Think of other relevant data structures!

To solve without additional data structure, can use sorting algorithm.

"""

# Second solution using set (or rather, hash table)
def is_unique2(s):
    chars = set()

    for c in s:
        if c.isalpha():
            if c in chars:
                return False
            chars.add(c)

    return True

# Third solution using sorting
def is_unique3(s):
    chars = list(sorted(s))

    for idx, c in enumerate(chars[:-1]):
        if c == chars[idx+1]:
            return False

    return True

s = "hiptamus"
print(is_unique(s), is_unique2(s), is_unique3(s))