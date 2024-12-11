"""LeetCode

Algorithm : 
    Hash Table
Level :
    Easy
Status :
    Accepted

Thu Dec 12 00:11:52 KST 2024
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []

        n = len(nums)
        if target%2==0 and nums.count(target//2) == 2:
            result = [i for i in range(n) if nums[i] == target//2]
            return result

        d = {}
        
        for i in range(n):
            d[nums[i]] = i
        
        for x in nums:
            y = target - x
            if y in d and y != target//2:
                result = [d[x], d[y]]
        
        """
        n = len(nums)

        d = {}
        for i in range(n):
            d[nums[i]] = i
        
        for i in range(n):
            c = target - nums[i]
            if c in d and d[c] != i:
                result = [i, d[c]]
        """

        return result
        