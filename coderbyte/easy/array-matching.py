"""
Have the function ArrayMatching(strArr) read the array of strings stored in strArr which will contain only two elements, both of which will represent an array of positive integers. For example: if strArr is ["[1, 2, 5, 6]", "[5, 2, 8, 11]"], then both elements in the input represent two integer arrays, and your goal for this challenge is to add the elements in corresponding locations from both arrays. For the example input, your program should do the following additions: [(1 + 5), (2 + 2), (5 + 8), (6 + 11)] which then equals [6, 4, 13, 17]. Your program should finally return this resulting array in a string format with each element separated by a hyphen: 6-4-13-17. 

If the two arrays do not have the same amount of elements, then simply append the remaining elements onto the new array (example shown below). Both arrays will be in the format: [e1, e2, e3, ...] where at least one element will exist in each array.
"""

def readArray(s):
    return [int(x) for x in s.replace('[','').replace(']','').split(',')]

def ArrayMatching(strArr):
    arr1, arr2 = [readArray(s) for s in strArr]
    
    if len(arr1) < len(arr2):
        arr1 += [0] * (len(arr2) - len(arr1))
    elif len(arr1) > len(arr2):
        arr2 += [0] * (len(arr1) - len(arr2))
    
    sums = [str(x+y) for x,y in zip(arr1, arr2)]
    
    # code goes here 
    return '-'.join(sums)