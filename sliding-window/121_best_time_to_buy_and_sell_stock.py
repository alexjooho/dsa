class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # global max profit variable
        # updating current profit variable that will update global max profit if it is > global
        # have a current min buy that updates as lower buys are found
        # return global max profit after looping once

        max_profit = 0
        min_buy = float('inf')

        for price in prices:
            if price < min_buy:
                min_buy = price

            curr_profit = price - min_buy

            if curr_profit > max_profit:
                max_profit = curr_profit

        return max_profit

# could've used indexes to make it a "two pointers" or "sliding window" type of question, but this question
# only asked for max profit instead of when to buy, so I didn't use it

# neetcode solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        l = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]:
                l = r
            res = max(res, prices[r] - prices[l])
        return res