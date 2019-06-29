# Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)). The array will not be empty, will only contain positive integers, and will not contain more than one mode. 

def mean(arr):
    return sum(arr)/len(arr)

# NOTE: The median is not the mode!    
def median(arr):
    sortedArr = list(sorted(arr))
    if len(arr) % 2 == 1:
        return sortedArr[len(arr)//2]
    else:
        return float(sortedArr[len(arr)//2] + sortedArr[len(arr)//2-2])/2
        
def mode(arr):
    counts = {}
    for x in arr:
        # TODO: Better way to do this?
        counts.setdefault(x, 0)
        counts[x] += 1
    
    maxKey, maxValue = 0, 0
    for k,v in counts.items():
        if v > maxValue:
            maxKey, maxValue = k, v
            
    return maxKey

def MeanMode(arr):
    if mean(arr) == mode(arr):
        return 1
    else:
        return 0

    # code goes here 
    return arr