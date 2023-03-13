class Solution:
    def countBits(self, n: int) -> List[int]:
        # create an empty array
        # for each number up to n, turn number into binary and get rid of starting "0b"
        # count the number of 1's in that number in a while loop
        # and then append to the array
        # this is bad because it's O(n^2)

        ans = []

        for i in range(n + 1):
            binary = bin(i)[2:]
            binary_list = [*binary]
            counter = 0

            while binary_list:
                counter += int(binary_list.pop()) % 2

            ans.append(counter)

        return ans
        
# Neetcode solution:
# This solution is O(n) because it doesn't repeat any steps
# Doesn't even need to be turned into a bit (so it's more so a dynamic programming problem/solution)
# starts by making a list with that size so that the list doesn't ever have to grow if it starts with
# less allocated space than expected

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

# other solution from youtube comment (better solution)
# this solution takes advantage of the fact that doing // 2 will basically get rid of the
# last bit, since it divides by 2 and rounds down (same as shifting to right)
# so if you do this, you can just check the last bit of the current number and add that to the
# number of bits that the number half of it had

# for every odd number, it will add the last 1 bit, and for every even number it will be same as half the number

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)
        return ans