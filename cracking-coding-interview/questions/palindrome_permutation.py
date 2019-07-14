def make_counts(s):
    counts = {}
    
    for c in s:
        counts.setdefault(c, 0)
        counts[c] += 1
        
    return counts

# Incorrect answer!
"""def palindrome_permutation(s):
    # Filter non-characters
    s = [c.lower() for c in list(s) if c.isalpha()]
    
    # Count characters
    counts = make_counts(s)
    
    # If even, all counts have to be equal to 2
    if len(s) % 2 == 0:
        return all([v == 2 for v in counts.values()])
    
    # If odd, one 1 and rest 2's
    else:
        cond1 = len([v for v in counts.values() if v == 1]) == 1
        cond2 = len([v for v in counts.values() if v != 1 and v != 2]) == 0
        return cond1 and cond2

s = "Tact Coa"
print(palindrome_permutation(s))"""

"""
Notes on solution

One bug I made during the first solution was confusing "and" and "or"!

Another bug is that the counts have be even, not just 2, for the string to be a palindrome.

"""

# TODO: Have a second go at this problem!