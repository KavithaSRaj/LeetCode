    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        while( i < len(prices) and j < len(prices) and j > i):
            if prices[j] - prices[i] > 0:
                print(profit)
                profit = max(profit, prices[j] - prices[i])
                j += 1
            else:
                i += 1
            if i == j:
                j += 1
        return profit
    def maxProfit(self, prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0
    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
            
    return max_profit