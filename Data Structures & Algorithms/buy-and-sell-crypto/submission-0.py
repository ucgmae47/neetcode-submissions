class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        low = high = prices[0]
        for price in prices:
            if price >= low:
                if price > high:
                    high = price
            else:
                if high - low > profit:
                    profit = high - low
                low = high = price
        if high - low > profit:
            profit = high - low
        return profit