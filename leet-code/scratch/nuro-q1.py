import math

def preprocess(arr):
    preprocessed = {}
    for power in range(0, math.floor(math.log2(len(arr)))+1):
        for idx, x in enumerate(arr):
            length = len(arr[idx:])
            if length < 2**power:
                continue
        
            if power == 0:
                preprocessed[(idx, power)] = x
            else:
                preprocessed[(idx, power)] = min(preprocessed[(idx, (power-1))], preprocessed[(idx+2**(power-1), (power-1))])
            
    return preprocessed

def minimum_range(a, b, preprocessed):
    length = math.floor(math.log2(b-a+1))
    return min(preprocessed[a, length], preprocessed[b + 1 - 2**length, length])

arr = [5, 2, 7, 3, 1]
p = preprocess(arr)

print(minimum_range(0,4, p))