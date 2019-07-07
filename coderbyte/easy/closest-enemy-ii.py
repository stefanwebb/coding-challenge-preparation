"""
Have the function ClosestEnemyII(strArr) read the matrix of numbers stored in strArr which will be a 2D matrix that contains only the integers 1, 0, or 2. Then from the position in the matrix where a 1 is, return the number of spaces either left, right, down, or up you must move to reach an enemy which is represented by a 2. You are able to wrap around one side of the matrix to the other as well. For example: if strArr is ["0000", "1000", "0002", "0002"] then this looks like the following: 

0 0 0 0
1 0 0 0
0 0 0 2
0 0 0 2 

For this input your program should return 2 because the closest enemy (2) is 2 spaces away from the 1 by moving left to wrap to the other side and then moving down once. The array will contain any number of 0's and 2's, but only a single 1. It may not contain any 2's at all as well, where in that case your program should return a 0. 
"""

def findOne(arr):
    for idx, row in enumerate(arr):
        for jdx, col in enumerate(row):
            if arr[idx][jdx] == '1':
                return (idx, jdx)
                
def findTwos(arr):
    locs = []
    for idx, row in enumerate(arr):
        for jdx, col in enumerate(row):
            if arr[idx][jdx] == '2':
                locs.append((idx, jdx))
    return locs

def ClosestEnemyII(strArr):
    rows = len(strArr)
    cols = len(strArr[0])

    # Find where 1 is
    oneLoc = findOne(strArr)
    twoLocs = findTwos(strArr)
    
    if len(twoLocs) == 0:
        return 0
    
    minDiff = 100
    for loc in twoLocs:
        xMin = min(abs(loc[0]-oneLoc[0]), rows-abs(loc[0]-oneLoc[0]))
        yMin = min(abs(loc[1]-oneLoc[1]), cols-abs(loc[1]-oneLoc[1]))
        thisDiff = xMin + yMin
        if thisDiff < minDiff:
            minDiff = thisDiff

    # code goes here 
    return minDiff

x = ["01000", "00020", "00000", "00002", "02002"]
print(ClosestEnemyII(x))