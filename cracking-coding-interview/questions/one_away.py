# Q1.5

# Incorrect first solution!
"""def one_away(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    counts = {}
    for c in s1:
        counts.setdefault(c, 0)
        counts[c] += 1
    
    for c in s2:
        counts.setdefault(c, 0)
        counts[c] -= 1
        
    return len([ v for v in counts.values() if v != 0 and v != 1 and v != -1 ]) == 0 and len([ v for v in counts.values() if v == 1 or v == -1 ]) <= 2

print(one_away("pale", "zple"))"""

"""
Notes on solution

Think: what does it mean to be one edit away?

"""

# TODO: Redo with correct solution!