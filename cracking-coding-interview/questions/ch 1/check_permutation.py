# Q1.2

def check_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    chars1 = {}
    chars2 = {}
    
    for c1, c2 in zip(s1, s2):
        chars1.setdefault(c1, 0)
        chars2.setdefault(c2, 0)
        chars1[c1] += 1
        chars2[c2] += 1
        
    return chars1 == chars2

s1 = "abc"
s2 = "cba"

print(check_permutation(s1, s2))

"""
Notes on solution

Really have my brain switched on when I'm coding! And check that there aren't any stupid bugs before hitting Run!

A second solution sorts both strings and compares whether they are equal.

A modification of my solution would be to only count one string in the first loop, then have a second loop and decrement the counts. If any go negative, return False.

"""