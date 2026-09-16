class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
             
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit
                
        return max_profit
    
prices = [9,7,4,2,3,1,6,10]

solution = Solution()
result = solution.maxProfit(prices)

print("Maximum profit: ", result)