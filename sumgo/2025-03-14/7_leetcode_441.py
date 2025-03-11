class Solution:
    def arrangeCoins(self, n: int) -> int:

        i = 1
        
        while True:
            if i > n:
                return i-1
            n -= i
            i += 1