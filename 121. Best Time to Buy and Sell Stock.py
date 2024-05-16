class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dif = [0,0]

        for i in range (1, len(prices)):
            if prices[i] - prices[i-1] + dif[1] >= 0:
                dif[1] = prices[i] - prices[i-1] + dif[1]
                dif[0] = max(dif[0], dif[1])
            else:
                dif[1] = 0

        return dif[0]        
