"""LongestPanlindrome

Algorithm : 
    Greedy
Level :
    Medium
Status :
    Failed

Sun Nov 26 14:28:24 PST 2023
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        i, j = 0, len(height)-1

        result = (j-i) * min(height[j], height[i])
        while i < j:
            # It does not find the middle maximum ex. 1*17
            right = (j-(i+1)) * min(height[j], height[i+1])
            left = ((j-1)-i) * min(height[j-1], height[i])

            if result <= max(left, right):
                if max(left, right) == right:
                    i += 1
                    result = right
                else:
                    j -= 1
                    result = left
            else:
                break

        """Answer
        while i < j:
            current = (j-i) * min(height[i], height[j])
            result = max(result, current)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        """
        
        return result
        