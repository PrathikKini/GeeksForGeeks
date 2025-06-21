class Solution:
    def maximumProfit(self, prices):
        # code here
        minprice = prices[0]
        maxProfit = 0
        
        for sell in prices:
            maxProfit = max(maxProfit, sell - minprice)
            minprice = min(minprice,sell)
        return maxProfit