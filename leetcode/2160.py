"""LeetCode

Algorithm : 
    Greedy
Level :
    Easy
Status :
    Accepted

Sun Nov 26 14:54:56 PST 2023
"""

class Solution:
    def minimumSum(self, num: int) -> int:
        result = 0
        nums = sorted(list(str(num)))

        new1 = nums[0] + nums[2]
        new2 = nums[1] + nums[3]

        result = int(new1) + int(new2)

        return result
        