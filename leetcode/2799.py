"""LeetCode

Algorithm : 
    Sliding Window
Level :
    Medium
Status :
    Accepted

Thu Apr 24 21:55:11 KST 2025
"""

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        cnt = len(set(nums))
        
        ans = 0
        n = len(nums)
        for i in range(n):
            tmp = set()
            for j in range(i, n):
                tmp.add(nums[j])
                if len(tmp) == cnt:
                    ans += n-j
                    break
        
        return ans
