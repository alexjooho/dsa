class Solution:
    def reverseBits(self, n: int) -> int:
        # start with a total of 0 that will be added upon for each bit
        # start from the end bit of the integer and add that place's value to the total
        # to get the place value of the bit, keep a counter that starts at 2^31
        # shift the binary to the right and keep doing this until the binary = 0

        total = 0
        counter = 2**31

        while n:
            if n & 1:
                total += counter
            counter = counter // 2
            # make sure to use "//" instead of "/" because "/" turns the integer into a float
            # since it doesn't round down, and the questions asks for an integer answer
            n = n >> 1

        return total
        

# neetcode solution:
# this is a more "bit-like" solution
# it basically does the same thing but adds the values by shifting to the left an i
# number of times to get the place value of that bit

# class Solution:
#     def reverseBits(self, n: int) -> int:
#         res = 0
#         for i in range(32):
#             bit = (n >> i) & 1
#             res += (bit << (31 - i))
#         return res

# another youtube solution (basically same concept but it's a little simplified):
# this solution keeps adding 1 or 0 to the result and then shifts to the left to increase
# the place value each time another value is to be added

    # res = 0

    # for i in range(32):
        
    #     res = res << 1
    #     bit = n%2
    #     res += bit
    #     n = n >> 1

    # return res