class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A = sorted(A)
        
        ans = -1
        l, u = 0, len(A) - 1
        
        while l < u:
            s = A[l] + A[u]
            if s < K:
                ans = max(s, ans)
                l = l + 1
            elif s >= K:
                u = u - 1
                
        return ans

A = [254,914,110,900,147,441,209,122,571,942,136,350,160,127,178,839,201,386,462,45,735,467,153,415,875,282,204,534,639,994,284,320,865,468,1,838,275,370,295,574,309,268,415,385,786,62,359,78,854,944]
K = 200

sln = Solution()
print(sln.twoSumLessThanK(A, K))