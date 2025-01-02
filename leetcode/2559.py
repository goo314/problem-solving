"""LeetCode

Algorithm : 
    Prefix Sum
Level :
    Medium
Status :
    Accepted

Thu Jan  2 23:40:49 KST 2025
"""

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def isVowelString(word) -> bool:
            vowels = ["a", "e", "i", "o", "u"]
            start, end = word[0], word[-1]
            if start in vowels and end in vowels:
                return True
            return False
        
        result = []
        n = len(words)
        dp = [0] * (n+1)
        
        for i in range(n):
            word = words[i]
            dp[i+1] = dp[i]
            if isVowelString(word):
                dp[i+1] += 1

        for (i, j) in queries:
            ans = dp[j+1] - dp[i]
            result.append(ans)

        return result