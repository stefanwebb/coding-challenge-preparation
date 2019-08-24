""" Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Naive solution of iterating through all combinations
        for idx, x in enumerate(nums):
            for jdx, y in enumerate(nums[(idx+1):]):
                if x + y == target:
                    return [idx, jdx+idx+1]"""

def binsearch(arr, x):
    lower = 0
    upper = len(arr)-1
    
    while lower <= upper:
        median = (lower+upper)//2
        
        if arr[median] < x:
            lower = median+1
        elif arr[median] > x:
            upper = median-1
        else:
            return median
        
    return None

# O(n*log(n)) solution
"""class Solution:
    def twoSum(self, nums, target):
        nums_idx = [(x, idx) for idx, x in enumerate(nums)]
        nums_idx.sort(key=lambda x: x[0])

        nums = [x for x,_ in nums_idx]
        indices = [idx for _,idx in nums_idx]
        
        # Binary search
        for idx, x in enumerate(nums):
            y = target-x
            if y < x:
                continue

            jdx = binsearch(nums[(idx+1):], y)
            
            if jdx is not None:
                return [indices[idx], indices[jdx+idx+1]]"""

# O(n) solution
class Solution:
    def twoSum(self, nums, target):
        diffs = {target-x:idx for idx,x in enumerate(nums)}
        
        for jdx,y in enumerate(nums):
            if y in diffs:
                idx = diffs[y]
                if jdx != idx:
                    return [jdx,idx]

class Solution:
    def twoSum(self, nums, target):
        checks = {}
        for idx, x in enumerate(nums):
            checks[x] = idx
            
        for idx, x in enumerate(nums):
            if target - x in checks:
                jdx = checks[target - x]
                if jdx != idx:
                    return [idx, jdx]

#nums = [2,7,11,15]
#target = 9

#nums = [3,3]
#target = 6

nums = [3,2,4]
target = 6

sln = Solution()
print(sln.twoSum(nums, target))