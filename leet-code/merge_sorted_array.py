class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Work out where to start taking entries from and where to start placing
        jdx = m - 1
        idx = n - 1
        kdx = m + n - 1
        
        while kdx >= 0 and jdx >= 0:
            if idx < 0 or nums1[idx] <= nums2[jdx]:
                nums1[kdx] = nums2[jdx]
                jdx -= 1
            elif nums1[idx] > nums2[jdx]:
                nums1[kdx] = nums1[idx]
                idx -= 1
            kdx -= 1

sln = Solution()
#nums1 = [1,2,3,0,0,0]
#nums2 = [2,5,6]
nums1 = [2,0]
nums2 = [1]
sln.merge(nums1, 1, nums2, 1)
print(nums1)