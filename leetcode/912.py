"""LongestPanlindrome

Algorithm : 
    Counting Sort
Level :
    Medium
Status :
    Accepted

Tue Nov 28 23:29:23 PST 2023
"""

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        result = []

        count = [0] * (10**5+1)
        for x in nums:
            count[x+5*10**4] += 1
        
        for i in range(len(count)):
            while count[i] > 0:
                result.append(i-5*10**4)
                count[i] -= 1

        return result