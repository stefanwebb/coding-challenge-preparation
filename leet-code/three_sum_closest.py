# A N^2*ln(N) solution
"""
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        
        # For each x...
        last_x = None
        for idx, x in enumerate(nums):
            if x == last_x:
                continue
                
            # And each y...
            last_y = None
            for jdx, y in enumerate(nums[(idx+1):-1]):
                if y == last_y:
                    continue
                    
                #if x + y - target >
                    
                # Use binary search to find the best z
                lower = idx+jdx+2
                upper = len(nums)-1
                
                while lower <= upper:
                    median = (lower + upper)//2
                    proposal = x+y+nums[median]
                    
                    if abs(proposal - target) < abs(ans - target):
                        ans = proposal
                        
                    if proposal - target > 0:
                        upper = median - 1
                    
                    elif proposal - target < 0:
                        lower = median + 1
                    
                    else:
                        break

        return ans
"""

# NOTE: This doesn't work!
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]
        
        # O(N^2): Calculate sum of all pairs and maximum minimum index
        pairs = {}
        for idx, x in enumerate(nums[:-1]):
            for jdx, y in enumerate(nums[(idx+1):]):
                pairs[x+y] = (idx,idx+jdx+1)

        print(pairs[-174])
                
        # Convert pairs to sorted list
        pairs = list(pairs.items())
        pairs.sort(key=lambda x: x[0])
                
        # O(N*lg(N)): Search for lowest ans
        # For each x...
        for idx, x in enumerate(nums[:-2]):
            lower = 0
            upper = len(pairs)-1
            
            # ...do binary search over sum of all pairs
            """for y_plus_z, jdx in pairs:
                proposal = x + y_plus_z
                if abs(proposal - target) < abs(ans - target) and jdx > idx:
                    ans = proposal"""

            while lower <= upper:
                median = (lower+upper)//2
                proposal = x + pairs[median][0]
                jdx = pairs[median][1][0]
                indices = pairs[median][1]

                if proposal == -274:
                    print('Got here!')
                
                if abs(proposal - target) < abs(ans - target) and jdx > idx:
                    ans = proposal
                    
                if proposal - target > 0:
                    upper = median - 1
                elif proposal - target < 0:
                    lower = median + 1
                #else:
                #    break

        return ans

#nums = [-55,-24,-18,-11,-7,-3,4,5,6,9,11,23,33]
nums = [87,6,-100,-19,10,-8,-58,56,14,-1,-42,-45,-17,10,20,-4,13,-17,0,11,-44,65,74,-48,30,-91,13,-53,76,-69,-19,-69,16,78,-56,27,41,67,-79,-2,30,-13,-60,39,95,64,-12,45,-52,45,-44,73,97,100,-19,-16,-26,58,-61,53,70,1,-83,11,-35,-7,61,30,17,98,29,52,75,-73,-73,-23,-75,91,3,-57,91,50,42,74,-7,62,17,-91,55,94,-21,-36,73,19,-61,-82,73,1,-10,-40,11,54,-81,20,40,-29,96,89,57,10,-16,-34,-56,69,76,49,76,82,80,58,-47,12,17,77,-75,-24,11,-45,60,65,55,-89,49,-19,4]
target = -275

sln = Solution()
print(sln.threeSumClosest(nums, target))