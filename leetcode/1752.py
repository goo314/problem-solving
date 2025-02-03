"""LeetCode

Algorithm : 
    Array
Level :
    Easy
Status :
    Accepted

Mon Feb  3 22:16:36 KST 2025
"""

class Solution:
    def check(self, nums: List[int]) -> bool:
        result = False

        n = len(nums)
        for i in range(n):
            tmp = nums[i:] + nums[:i]
            if tmp == sorted(tmp):
                result = True
                break
        
        return result
    
    """Better Answer
        result = False
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                count += 1
            if count > 1:
                return result
        
        result = True
        return result
    """