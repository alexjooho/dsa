class Solution:
    def numDecodings(self, s: str) -> int:
        # two possibilities, take the first possible decoding and
        # add the maximum decodings of the rest of the code
        # or take the second possible coding and add the max of rest
        # e.g. for 11106: 1 + max of 1106 OR 11 + max of 106
        # then for the remaining code, do the same thing

        # dynamic programming problem
        # careful to not include "0" in front of a number or as a number!
        # fibonacci sequence where the next maximum number depends
        # on the last 2 numbers
        # dp[i] = dp[i + 1] + dp[i + 2]

        # start from the end so that we don't have to look ahead for 0's
        # if the number is a 0, set current n2 to 0 (since you can't use this)
        # for each number, it is the combination of using (possibly) the
        # max codes for the prev 2 numbers (in this case, the right-side)
        # n1 represents if you use the right char as part of a 2-digit code
            # n1 can only be used if current number with right number is valid!!
        # n2 represents if you use the current char as part of a 1-digit code

        # edge case for if number starts with a 0 or if it has a second
        # char of 0 but a first char > 2
        # careful for invalid numbers aka > 26

        # this was my previous way of handling edge cases (but not needed now)
        # if s[0] == 0:
        #     return 0
        # if s[1] == 0 and s[0] > 2:
        #     return 0

        n1, n2 = 0, 1

        for i in range(len(s) - 1, -1, -1):
            temp = n2
            if s[i] == "0":
                # if current number is 0, it can't be a start of valid code
                # make sure to put "0" instead of 0, since its a string
                n2 = 0
            elif int(s[i:i+2]) <= 26:
                # max number of codes is n2 + n1 only if number of
                # curr and next char is valid (since n1 represents
                # the usage of next char as 2-digit char)
                # otherwise, n2 stays the same since there's the same
                # number of possible codes
                n2 += n1
            n1 = temp

        return n2

# neetcode recursive cache solution:
# this solution goes top-down/top-bottom
# it recursively calls the next number and also adds the next next numbers's call
# if a 2-digit number is valid
# has a base case of returning cached value or returning 0 if number is 0
# since a code can't start with 0

class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}
        # base case to return 1 if at last char

        def dfs(i):
            if i in dp:
                return dp[i]
                # technically fails for input of "0"
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            # doing recursion on next digit
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
            # doing recursion on 2nd next digit, since its taking into account the
            # next digit as part of current 2-digit char
            # if so, add that recursive option to res
                res += dfs(i + 2)
            dp[i] = res
            return res

        return dfs(0)

# neetcode dynamic programming solution:
# same general concept, starts from bottom to top
# using a whole dictionary, but not necessary

# Dynamic Programming
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]