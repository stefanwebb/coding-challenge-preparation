# Have the function ArrayAdditionI(arr) take the array of numbers stored in arr and return the string true if any combination of numbers in the array (excluding the largest number) can be added up to equal the largest number in the array, otherwise return the string false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not contain all the same elements, and may contain negative numbers.

def ArrayAdditionI(arr):
    # Find the largest element and remove
    maxElem = max(arr)
    arr = [e for e in arr if e != maxElem]

    # Call helper method
    def recurseAdd(currentSum, currentArr, maxElem):
        for i in range(len(currentArr)):
            thisSum = currentSum + currentArr[i]
            if thisSum == maxElem:
                return True

            elif i != len(currentArr)-1:
                if recurseAdd(thisSum, currentArr[(i+1):], maxElem) == True:
                    return True
                
        # code goes here 
        return False
    
    if recurseAdd(0, arr, maxElem):
        return "true"
    else:
        return "false"
    
# keep this function call here
x = [5,7,12,1,2]
print(ArrayAdditionI(x))