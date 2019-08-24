# N^3 solution times out
"""class Solution:
    def threeSum(self, nums):
        ans = set()
        
        #duplets = {}
        
        for idx, x in enumerate(nums):
            for jdx, y in enumerate(nums[(idx+1):]):
                for kdx, z in enumerate(nums[(idx+jdx+2):]):
                    if x + y + z == 0:
                        this = [x,y,z]
                        this.sort()
                        ans.add((this[0], this[1], this[2]))
                        
        return [list(this) for this in list(ans)]

nums = [-1,0,1,2,-1,-4]"""

# N^2 solution
"""class Solution:
    def threeSum(self, nums):
        ans = set()
        duplets = {}
        
        # Remove duplicates
        #nums = list(set(nums))
        
        counts = {}
        for x in nums:
            counts.setdefault(x, 0)
            counts[x] = counts[x] + 1
            
        nums = []
        for k,v in counts.items():
            v = max(v, 3)
            nums.extend([k]*v)
        
        for idx, x in enumerate(nums):
            for jdx, y in enumerate(nums[(idx+1):]):
                duplets.setdefault(x+y,[])
                duplets[x+y].append((idx,jdx+idx+1,y))

        for kdx, z in enumerate(nums):
            if -z in duplets:
                indices = duplets[-z]
                for idx,jdx,y in indices:
                    if kdx != idx and kdx != jdx:
                        this = [z,y,-z-y]
                        this.sort()
                        ans.add((this[0], this[1], this[2]))
                        
        return [list(this) for this in list(ans)]"""

# This is a super fast N^2 solution!
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        # Insert numbers in hash table
        indices = {}
        for idx, x in enumerate(nums):
            indices.setdefault(x, [])
            indices[x].append(idx)

        # Loop through numbers
        last_x = None
        for idx, x in enumerate(nums):
            if x > 0:
                break

            # Skip duplicates
            if x == last_x:
                continue

            last_y = None
            
            # Find if there are two numbers that sum to -x
            for jdx, y in enumerate(nums[(idx+1):]):
                if y == last_y:
                    continue

                z = -x-y
                if z in indices:
                    for kdx in indices[z]:
                        if kdx > jdx+idx+1:
                            result.append([x, y, z])
                            break

                last_y = y

            last_x = x
 
        return result

#nums = [0,0]
nums = [0,0,0,0]
#nums = [-1,0,1,2,-1,-4]

# NOTE: Lists are not hashable, whereas tuplets are!
# Hence the hack above

sln = Solution()
print(sln.threeSum(nums))