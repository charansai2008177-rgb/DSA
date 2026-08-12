class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        if not prices:
            return 0
        mins = prices[0]
        profit = 0
        for x in range(1,len(prices)):
            profit = max(profit,prices[x]-mins)
            mins = min(mins,prices[x])
        
        return profit
        

        