class Solution:
    def isHappy(self, n: int) -> bool:
        # turn number into string so that we can choose each integer
        # turn each string integer into an int and square it
        # add the sum of the squares
        # NOTE: the sum of squares of a number will ALWAYS eventually lead to a loop
            # will loop to either a 1 or a 4
        # if it loops to repeat a number that is not 1, then return false
            # keep track of this with a seen set
        # if it reaches 1, then return true

        seen = set([n])

        while True:
            # doesn't matter what we put here since the loop will end with the logic inside
            num_string = str(n)
            total = 0

            for num in num_string:
                int_num = int(num)
                total += int_num * int_num
                # can just do ** 2

            if total == 1:
                return True
            if total in seen:
                return False
            seen.add(total)
            n = total

# neetcode solution:
# a little cleaner because he doesn't turn the number into a string
# instead he uses a helper function and uses modulo
# then he uses // to remove the singles digit
# in this case he uses the turtle and hare to allow him to use less memory

class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
