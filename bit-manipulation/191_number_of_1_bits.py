class Solution:
    def hammingWeight(self, n: int) -> int:

        # turn integer into string and get the count of 1's in the string

        total = 0
        while n: # could also do while n > 0
            total += n & 1
            n = n >> 1

        return total
        
# Neetcode solution 1:
# class Solution:
#     def hammingWeight(self, n: int) -> int:

#         # turn integer into string and get the count of 1's in the string

#         total = 0
#         while n: # could also do while n > 0
#             total += n % 2
#             n = n >> 1

#         return total
        
# Neetcode solution 2 (gets rid of having to check all middle 0's):
# this works because it adds 1 to the total every time and every action gets rid of the right-most
# "1" bit

# class Solution:
#     def hammingWeight(self, n: int) -> int:
#         res = 0
#         while n:
#             n &= n - 1
#             res += 1
#         return res