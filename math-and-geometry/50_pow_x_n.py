# neetcode solution
# O(log n) solution
# divide and conquer using recursion to keep dividing exponent by 2
# base case is if n = 0, return 1
# or if x = 0, just return 0 (edge case)
# do problem using absolute value of n, and then if n is negative, get reciprocal of it

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            # base cases

            res = helper(x, n // 2)
            # divide exponent by 2 (if odd we figure it out below)
            res = res * res
            # multiply res of recursive function by itself since that's 
            # equivalent to multiplying exponent by 2
            # could also just not do this line and do x*x in the helper function, which would be like multiplying
            # exponent by 2
            return x * res if n % 2 else res
            # if odd, we multiply by base x again

        res = helper(x, abs(n))
        return res if n >= 0 else 1 / res
        # 1 / res if exponent is negative


# this was my solution but it doesn't pass all test cases since it's not as efficient
# instead, look at neetcode's "divide and conquer" solution

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # start with 1, and multiply by x for each number in range(n)
        # if n is negative, flip it to be 1 / result
        # import math to use 

        result = 1
        negative = False

        if n < 0:
            # if n is negative, make the negative variable true and make n positive
            negative = True
            n *= -1
            # could also do abs()

        for i in range(n):
            # multiply result by x for each number in range(n)
            result *= x

        return 1 / result if negative else result