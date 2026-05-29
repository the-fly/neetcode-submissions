class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        previousMin = prices[0]
        for price in prices:
            if price < previousMin:
                previousMin = price
            elif price - previousMin > maxProfit:
                maxProfit = price - previousMin
        return maxProfit

        