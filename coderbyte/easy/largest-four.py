# Have the function LargestFour(arr) take the array of integers stored in arr, and find the four largest elements and return their sum. For example: if arr is [4, 5, -2, 3, 1, 2, 6, 6] then the four largest elements in this array are 6, 6, 4, and 5 and the total sum of these numbers is 21, so your program should return 21. If there are less than four numbers in the array your program should return the sum of all the numbers in the array. 

import heapq

def LargestFour(arr):
    if len(arr) < 4:
        return sum(arr)
        
    heap = arr[:4]
    heapq.heapify(heap)
    
    for x in arr[4:]:
        heapq.heappushpop(heap, x)
    
    # code goes here 
    return sum(heap)