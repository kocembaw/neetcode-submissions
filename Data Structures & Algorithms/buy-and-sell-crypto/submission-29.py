class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        max_price = 0
        for price in prices:
            if price > max_price:
                max_price = price
            if price < max_price:
                max_profit = max(max_profit, max_price - price)
        

        return max_profit

