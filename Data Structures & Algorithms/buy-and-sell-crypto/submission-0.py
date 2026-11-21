class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum = 0
        for i in range(1, len(prices)):
            for m in range(i, len(prices)):
              summe = prices[m] - prices[i - 1] 
              if summe > max_sum:
                max_sum = summe 
        return max_sum 


        