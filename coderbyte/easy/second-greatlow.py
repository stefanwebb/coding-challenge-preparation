# Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, respectively, separated by a space. For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98. The array will not be empty and will contain at least 2 numbers. It can get tricky if there's just two numbers! 

# O(n*log(n)) solution
def SecondGreatLow(arr):
    # Sort and remove duplicates
    sortedArr = list(sorted(set(arr)))
    
    if len(sortedArr) == 1:
        return '{} {}'.format(sortedArr[0], sortedArr[0])
    
    else:
        return '{} {}'.format(sortedArr[1], sortedArr[len(sortedArr)-2])

# TODO: O(log(n)) solution!

# keep this function call here  
print(SecondGreatLow(raw_input()))