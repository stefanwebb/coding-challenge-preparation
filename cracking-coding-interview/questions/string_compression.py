# Q1.6

def string_compression(s):
    counts = [[s[0], 1]]
    for idx, c in enumerate(s[1:]):
        if c == s[idx]:
            counts[-1][1] += 1
        else:
            counts.append([c, 1])
            
    compressed = ''.join([k+str(v) for k,v in counts])
    return compressed if len(compressed) < len(s) else s

s = "aabcccccaaa"
print(string_compression(s))

