# neetcode solution

class Solution:
    def getSum(self, a: int, b: int) -> int:
        # use XOR ^
        # if there is one 1, then just use that
        # if both have a 1 in that digit spot, then carry it over
        # check using & operator

        # basically have to do a continuous loop until there are no more "carries"
        # do XOR, then also do & and << (left shift) & value to increase its digits place
        # to act as a carry indicator

        # now do XOR and the & again with the 2 binaries
        # keep repeating until no more carries (indicated by an & value that is 0)

        # time complexity: O(1) since we know from the constraints that a and b are within certain numbers
        # XOR and & operations are basically same time complexity as doing a simple + or -

        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:  # -a == b
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        return add(a, b)  # a*b >= 0 or (-a) > b > 0
    
    # NOTE: I didn't really understand the python version of this solution since there is a lot of
    # extra stuff going on that wasn't explained in neetcode's video
    
# neetcode java solution:
# apparently java is much easier for this question because
# python integers are arbitrarily large (they're not 32 bit)

class Solution {

    public int getSum(int a, int b) {
        while (b != 0) {
            int tmp = (a & b) << 1;
            a = (a ^ b);
            b = tmp;
        }
        return a;
    }
}