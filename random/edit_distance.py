def OneEditApart(s1, s2):
    # Make sure s1 is smaller string
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    if len(s2) - len(s1) > 1:
        return False

    # Check whether can insert/remove one character anywhere in the word
    idx = jdx = 0
    differs = 0
    while idx < len(s1) and jdx < len(s2):
        if s1[idx] != s2[jdx]:
            differs += 1
            if differs > 1:
                return False

        if s1[idx] == s2[jdx] or len(s1) == len(s2):
            idx += 1
            
        jdx += 1

    return differs == 1 or len(s1) != len(s2)

s1 = 'cat'
s2 = 'cats'
print(OneEditApart(s1, s2))