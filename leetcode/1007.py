"""LongestPanlindrome

Algorithm : 
    Greedy
Level :
    Medium
Status :
    Accepted

Sun Nov 26 15:27:35 PST 2023
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        result = 0

        nums = [0]*7
        for t in tops:
            nums[t] += 1
        for b in bottoms:
            nums[b] += 1
        
        x = max(nums)
        length = len(tops)
        
        if x < length:
            return -1
        
        val = nums.index(x)

        numt, numb = 0, 0
        for i in range(length):
            if val != tops[i] and val != bottoms[i]:
                return -1
            if val == tops[i] and val == bottoms[i]:
                continue
            elif val == tops[i]:
                numt += 1
            elif val == bottoms[i]:
                numb += 1
        
        result = min(numt, numb)
        
        return result