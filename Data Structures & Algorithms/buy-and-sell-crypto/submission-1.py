class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = float('inf')
        for i in range(len(prices)):
            if prices[i]<buy:
                buy = prices[i]
            else:
                max_profit = max(max_profit,prices[i]-buy)
        return max_profit
















        # max_profit = 0
        # least = float('inf')
        # for i in range(len(prices)):
        #     if prices[i]<least:
        #         least = prices[i]
        #     else:
        #         if prices[i]-least>max_profit:
        #             max_profit = prices[i]-least
        # return max_profit


        