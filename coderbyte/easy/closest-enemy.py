# Have the function ClosestEnemy(arr) take the array of numbers stored in arr and from the position in the array where a 1 is, return the number of spaces either left or right you must move to reach an enemy which is represented by a 2. For example: if arr is [0, 0, 1, 0, 0, 2, 0, 2] then your program should return 3 because the closest enemy (2) is 3 spaces away from the 1. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0. 

def ClosestEnemy(arr):
    whereOne = arr.index(1)
    
    right = whereOne+1
    left = whereOne-1
    
    while True:
        if right < len(arr) and arr[right] == 2:
            whereTwo = right
            break
        elif left >= 0 and arr[left] == 2:
            whereTwo = left
            break
        right += 1
        left -= 1
        
        if right >= len(arr) and left < 0:
            return 0

    # code goes here 
    return abs(whereTwo-whereOne)

print(ClosestEnemy([1, 0, 0, 0, 2, 2, 2]))