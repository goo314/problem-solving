"""LeetCode

Algorithm : 
    Hash
Level :
    Easy
Status :
    Accepted

Mon May 12 23:33:49 KST 2025
"""

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        from itertools import permutations
        for x in permutations(digits, 3):
            if x[0]==0 or x[-1]%2==1:
                continue
            tmp = ''.join(map(str, x))
            ans.append(int(tmp))
        ans = list(set(ans))
        ans.sort()
        return ans
