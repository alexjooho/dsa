class Solution:
    # O(n^2) solution that uses two arrays for dp and keep track of how many
    # number to the right (or left if you go other direction) are greater/lower
    # we then revisit that index and if it has values greater or lower than it
    # and it is also the same comparison (greater or lower) than the current
    # value its being compared to, then that means that it is part of a 3 pair
    # and you add its # of up/down depending on comparison to the total

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)

        up = [0] * n
        down = [0] * n

        teams = 0

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]
                else:
                    down[i] += 1
                    teams += down[j]

        # other direction:
        # NOTE: need to have the two loops direction compare in a way that
        # the same index is visited again to check that it is part of a 3 pair

        # for j in range(n):
        #     for i in range(j):
        #         if rating[i] < rating[j]:
        #             up[j] += 1
        #             teams += up[i]
        #         else:
        #             down[j] += 1
        #             teams += down[i]

        return teams

# Version B:  O(n^2) solution with (primitive) nested loops for building our 4 counting variables.
# uses left and right pointer to find values left and right of each point (going inwards to outwards)
# since we need to consider every combination of A > B > C and A < B < C:
# we do left_lower * right_higher (since this will be A < B < C)
# and we do left_higher * right_lower (A > B > C)

# we multiply these and then add them together since its a combination of all possibilities

class Solution:
    def numTeams(self, A):
        L = len(A)
        result = 0
        for j in range(1,L-1):
            x, lo_L, lo_R, hi_L, hi_R = A[j], 0, 0, 0, 0
            for i in range(j):
                if A[i]<x:
                    lo_L += 1
                else:
                    hi_L += 1
            for k in range(j+1,L):
                if A[k]<x:
                    lo_R += 1
                else:
                    hi_R += 1
            result += lo_L*hi_R + hi_L*lo_R
        return result

# Version A:  [Top Speed] O(n log n) solution using SortedLists to calculate our 4 counting variables in Log(n) time.
# uses SortedList to keep track of left side and right side of array
# keeps left and right sides sorted and removes each value before calculating
# and then adds it to left once done

# uses sl.bisect_left(x) to find how many numbers are to the left of it
# and subtracts that from length of the sl to get the # of higher numbers

from sortedcontainers import SortedList
class Solution:
    def count_low_high(self,sl,x):
        lo =           sl.bisect_left(x)
        hi = len(sl) - lo
        return lo, hi

    def numTeams(self, A):
        result = 0
        left   = SortedList()
        right  = SortedList(A)
        for x in A:
            right.remove(x)
            lo_L, hi_L  =  self.count_low_high(left ,x)
            lo_R, hi_R  =  self.count_low_high(right,x)
            result     +=  lo_L*hi_R + hi_L*lo_R
            left .add(x)
        return result