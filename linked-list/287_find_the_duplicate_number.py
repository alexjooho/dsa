class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # linked list cycle problem (even though its in an array)
        # use Floyd's tortoise and hare
        # for every value, point it's "next" value to the index of # value
        # look for where the cycle begins (index that is pointed to twice)
        # cycle can never begin at index 0 since numbers are from 1 -> n, that's why we start at 0

        # use fast and slow pointer to find first index where the pointers meet
        # then leave the slow pointer where it is and we are now done with the fast pointer
        # put ANOTHER slow pointer at the starting index, and then keep incrementing both old and new
        # slow pointers by 1 until they intersect.
        # where they intersect will be where the cycle starts, and that index # will be the repeated number

        # NOTE: THIS IS NOT INTUITIVE! BASICALLY: the distance from fast and slow pointer intersection to the
        # cycle start is the SAME DISTANCE from beginning point to cycle start
        # that's why when the new and old slow pointers intersect, that will be the cycle start

        # Logic (look at video for visual representation)
        # let p be the distance from start to beginning of cycle
        # let c be the distance of cycle
        # let x be distance of intersection point to the beginning of cycle
        # c - x will be the distance from beginning of cycle to the intersection point since it doesn't complete cycle
        # fast pointer will get to the cycle first and will do an extra loop compared to slow pointer!
        # fast pointer's distance will be P + 2C - X   (since it does the cycle and then gets to intersection point c - x)
        # slow pointer's distance will be P + C - X (since it stops immediately at intersection point)
        # 2 * slow = fast  (since fast pointer is twice as fast) -> 2P + 2C - 2X = P + 2C - X => P = X
        # this is the proof for why the intersection point will have same distance to cycle as from start to cycle!!

        # technically instead of 2C, it could be NC if the p portion is really long and fast needs to loop multiple times
        # but math will still work!
        
        # Joma Tech explanation/proof (want to prove that x % (mod) L = z)
        # x = distance from beginning to beginning of cycle
        # y = distance from beginning of cycle to meeting point
        # z = distance from meeting point (M) to beginning/end of cycle
        # L = loop length
        # turtle distance = x + y, hare distance = 2(x + y)
        # 2(x + y) = M + k*l  (where k is any number between 1 and infinity for the # of loops)
        # x = k * l - y
        # x mod L = (k * l - y) mod L
        # x % L = L - y = z
        # this means that the distance from beginning to beginning of cycle and z to beginning of cycle is the same

        slow, fast = 0, 0
        while True:
            # do while True to basically just keep going until they intersect
            slow = nums[slow]
            fast = nums[nums[fast]]
            # fast does next.next
            # always will be in bounds since the numbers can only point to possible indexes
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
            
# interesting solution found on leetcode that technically doesn't change the array
# but it changes it and turns it back to its original state
# probably isn't technically allowed

# checks for a seen number by turning numbers negative

def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            if nums[ abs(num) ] < 0:
                ans = abs(num)
                break
            nums[ abs(num) ] = -nums[ abs(num) ]
        # restore nums
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        return ans

# another interesting solution that does not satisfy constraints but shows an interesting intuitive pattern:

# use array as a "hashmap." recursively put each number into its respective index until
# the respective index already has the correct number, meaning that that number is the duplicate
# can do this iteratively as well

# Interesting solution #3:
# use binary search after sorting the array
# for every index, the number of indexes before it and including it
# should be <= to the value of the number in the index

# can do an iterative search from 0 to n, but we can also do binary search and check from middle