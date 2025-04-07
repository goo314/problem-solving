class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans = []

        n = len(prices)
        for i in range(n):
            p = prices[i]
            for j in range(i+1, n):
                if prices[j] <= prices[i]:
                    p -= prices[j]
                    break
            ans.append(p)
        
        return ans
