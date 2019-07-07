#Have the function ThreeSum(arr) take the array of integers stored in arr, and determine if any three distinct numbers (excluding the first element) in the array can sum up to the first element in the array. For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three sets of triplets that sum to the number 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1]. Your program should return the string true if 3 distinct elements sum to the first element, otherwise your program should return the string false. The input array will always contain at least 4 elements.

def ThreeSum(arr):
    total = arr[0]
    arr = arr[1:]
    for idx in range(len(arr)-2):
        for jdx in range(idx+1,len(arr)-1):
            for kdx in range(jdx+1,len(arr)):
                if arr[idx] + arr[jdx] + arr[kdx] == total:
                    return 'true'
                    
    # code goes here 
    return 'false'
