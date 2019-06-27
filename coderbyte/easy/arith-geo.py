#Have the function ArithGeo(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern or return "Geometric" if it follows a geometric pattern. If the sequence doesn't follow either pattern return -1. An arithmetic sequence is one where the difference between each of the numbers is consistent, where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2, 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements. 

def ArithGeo(arr): 
    # Need a minimal number of elements
    if len(arr) < 3:
        return -1
        
    # Hypothesized difference or ratio
    diff = arr[1] - arr[0]
    ratio = float(arr[1])/arr[0]
    
    for idx in range(2, len(arr)):
        if (arr[idx] - arr[idx-1]) != diff:
            break
        elif idx == len(arr) - 1:
            return 'Arithmetic'
            
    for idx in range(2, len(arr)):
        if float(arr[idx])/arr[idx-1] != ratio:
            break
        elif idx == len(arr) - 1:
            return 'Geometric'
            
    return -1

# keep this function call here  
print(ArithGeo(raw_input()))