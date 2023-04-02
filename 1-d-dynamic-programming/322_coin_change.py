class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create a 1-d array of size equal to amount
        # unbound knapsack type problem
        # sort the coins in descending order by value
        # for each type of coin, if the value of the coin is empty in the index,
        # put 1 for that cell
        # then, for each index, see if the cell of
        # index - value has a coin. if so, you can add 1 to the number of coins
        # in that cell to fill the current index IF AND ONLY IF
        # the total number of coins is now less than what it was before
        # OR IF THE CURRENT INDEX IS EMPTY (0)

        # time complexity: O(N * W), space complexity: O(W)

        # start from biggest coins going to the smallest
        # NOTE: I made the mistake of only going until the last index was filled
        # but we need to go through all coins to see if there is another
        # combination with a smaller number of coins needed!

        # basically want to fill every possible index that can be made with
        # a combination of coins
        # if an index is already filled, only update if the new total of coins
        # will be less

        # edge case of total amount needed being 0:
        if amount == 0:
            return 0

        total = [0] * (amount + 1)

        coins.sort(reverse = True)

        for val in coins:
            # NOTE: probably better to traverse it other way like neetcode did:
            # do each index individually and for each index see if a smaller total coins
            # can be made by looping through coins
            for i in range(1, len(total)):
                if val == i:
                    # for the first multiple of the coin to fill index
                    total [i] = 1

                if (i - val >= 0
                    and total[i - val] > 0
                    and (total[i - val] + 1 < total[i]
                    or total[i] == 0)):
                    # if i - val is a valid index
                    # and if a coin is present in cell of index - value
                    # and if adding a coin to that total will be less
                        # than the current num of coins in the index
                        # OR if the current index is 0
                    # then update the index with lower number of coins
                    total[i] = total[i - val] + 1

        return total[-1] if total[-1] != 0 else -1

# neetcode solution:
# he doesn't sort it, since no matter what we will always look for
# if the total is less or not anyways
# to account for the edge case of amount being 0, he simply made
# it return dp[amount], which is 0 since it doesn't go anywhere in for loop
# he also set every cell to amount + 1 so that it will
# be updated if lower (without having to do my extra OR logic)

# he does it a little differently in that he does one index at a time
# while I tried to use a single coin at a time

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # just to make sure its a valid index
                    dp[a] = min(dp[a], 1 + dp[a - c])
                    # only update if the new num coins is less than current number of coins
        return dp[amount] if dp[amount] != amount + 1 else -1

# recursive solution (much slower and more space complexity)

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # unbound knapsack type problem
        # recursive solution
        # include key and value 0:0 for base case
        # for a given n (target), check every coin if using that coin
        # will lead to a smaller needed number of coins
        # start the needed number of coins at inf so that it can be
        # compared to
        # if the calculation for the target has already been finished,
        # simply return the memoized/cached value

        # FOR RECURSIVE DP, LET THE RECURSION DO THE WORK FOR YOU
        # the recursive function already checks every possible outcome
        # so once it's been checked, we don't need to check it again

        num_coins = {0: 0}

        def dfs(n):
            if n in num_coins:
                return num_coins[n]

            num_coins[n] = float('inf')

            for coin in coins:
                if n - coin >= 0:
                    num_coins[n] = min(num_coins[n], 1 + dfs(n - coin))
                    # if amount - coin is a valid index/number,
                    # for every coin, see if using that coin will get you a
                    # smaller number of coins needed to add up to total

            return num_coins[n]
            # have to return something so that the min() line doesn't
            # give us a NoneType for the recursive call if it never
            # reaches 0

        dfs(amount)

        return num_coins[amount] if num_coins[amount] != float('inf') else -1