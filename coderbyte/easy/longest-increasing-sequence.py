# Have the function LongestIncreasingSequence(arr) take the array of positive integers stored in arr and return the length of the longest increasing subsequence (LIS). A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order. The sequence does not need to be contiguous or unique, and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6]. For this input, your program should return 3 because that is the length of the longest increasing subsequence. 

# NOTE: I found this problem particular hard! Didn't get the dynamic programming solution straight away

def LongestIncreasingSequence(arr):
    def helper(start, arr):
        #if len(arr) == 0:
        #    return 0
        candidates = [helper(arr[idx], arr[(idx+1):])+1 for idx in range(len(arr)) if arr[idx]>start]
        if candidates == []:
            return 0
        else:
            return max(candidates)

    # code goes here 
    return helper(0, arr)
    
# keep this function call here  
x = [10, 12, 4, 6, 100, 2, 56, 34, 79]
#x = [4, 3, 5, 1, 6]
print(LongestIncreasingSequence(x))