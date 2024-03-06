class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit=0
        buy=float('inf')
        sell=0

        for i in prices:

            if i<buy:
                buy=i
                sell=0

            if i>sell:
                sell=i

            profit=max(profit, sell-buy)


        return profit
        