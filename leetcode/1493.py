"""LongestPanlindrome

Algorithm : 
    DP
Level :
    Medium
Status :
    Accepted

Sun Dec  3 18:12:44 PST 2023
"""

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0

        arr = []
        
        tmp = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                arr.append(tmp)
                tmp = 0
            else:
                tmp += 1
        arr.append(tmp)
        
        for i in range(1, len(arr)):
            if result < arr[i-1] + arr[i]:
                result = arr[i-1] + arr[i]
        
        if len(arr) == 1:
            result = arr[0] - 1

        return result