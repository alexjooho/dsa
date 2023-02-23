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