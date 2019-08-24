def binsearch(arr, x, lower, upper):
    while lower <= upper:
        median = (lower+upper)//2
        
        if arr[median] < x:
            lower = median+1
        elif arr[median] > x:
            upper = median-1
        else:
            return median
        
    return upper


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Make num2 the bigger one always
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        lower2 = 0
        upper2 = len(nums2) - 1
        median2 = (lower2 + upper2)//2
        
        # Calculate number of elements less than median by performing binary search
        # in nums1
        lower1 = 0
        upper1 = len(nums1) - 1
        median1 = binsearch(nums1, nums2[median2], lower1, upper1)

        # Number of elements less than or equal to nums2[median]
        count = median2 + median1 + 1
        
        print('{} elements less than {}'.format(count, nums2[median2]))

sln = Solution()

nums1 = [1, 2]
nums2 = [3, 4]

sln.findMedianSortedArrays(nums1, nums2)