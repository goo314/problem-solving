"""LeetCode

Algorithm : 
    Sliding Window
Level :
    Medium
Status :
    Accepted

Wed Dec 11 23:21:45 KST 2024
"""

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        result = 0

        n = len(nums)
        nums.sort()
        p = n-1
        while p >= 0 and nums[p] - nums[0] > 2*k:
            p -= 1
        
        for i in range(n):
            while p < n and nums[p] - nums[i] <= 2*k:
                p += 1
            result = max(result, p-i)
        
        return result

        """
        nums.sort()
        left = 0
        for num in nums:
            if num - nums[left] > 2*k:
                left += 1
        
        return len(nums) - left
        """