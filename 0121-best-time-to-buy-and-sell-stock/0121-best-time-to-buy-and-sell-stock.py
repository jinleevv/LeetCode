class Solution:
        # Double For Loop O(n^2)
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         profit = prices[j] - prices[i]
        #         if profit > maxProfit:
        #             maxProfit = profit
    def maxProfit(self, prices: List[int]) -> int:
        # My Approach
        
        # maxProfit = 0
        # highNum = (prices[0], -1)
        # lowNum = (prices[0], -1)

        # for i in range(1, len(prices)):
        #     if prices[i] - lowNum[0] > maxProfit:
        #         if i > lowNum[1]:
        #             maxProfit = prices[i] - lowNum[0]
        #         if prices[i] > highNum[0] or highNum[1] == -1:
        #             highNum = (prices[i], i)
       
        #     elif highNum[0] - prices[i] > maxProfit:
        #         if i < highNum[1]:
        #             maxProfit = highNum[0] - prices[i]
        #             lowNum = (prices[i], i)
        #         if prices[i] < lowNum[0] or lowNum[1] == -1:
        #             lowNum = (prices[i], i)

        # return maxProfit

        # Solution Approach
        minPrice = float('inf')
        maxProfit = 0

        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        
        return maxProfit
        