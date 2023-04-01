class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programing problem: fibonacci sequence
        # basically check whether getting the current house is better value than skipping it
        # if curr + n1 > n2, then n2 = curr + n1
        # n1 will always equal prev n2
        
        # check whether the max of [0:-1] is greater than max of [1:]
        # NOTE: the trick to this question is basically recognizing that
        # we need to see whether the subarray including first element without last element
        # or subarray including last element without first element
        # yields a greater max value

        # this question is same as house robber except we need to exclude either first or last element

        # NOTE: my original idea was to keep track of whether the first element was being used or not
        # BUT THIS LEADS TO TOO MANY EDGE CASES!
        # by simply excluding the first element or the last element, we ensure that they are never both used!!!
        
        # time complexity: O(2n), space complexity: O(1)

        if len(nums) <= 2:
            # edge case for if the list has 2 or less indexes
            return max(nums)
        
        def rob_1(nums):
            # basically using house robber 1 as a helper function
            rob1, rob2 = 0, 0

            # [rob1, rob2, n, n+1, ...]
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2

        return max(rob_1(nums[0:-1]), rob_1(nums[1:]))
    
    # list of edge cases for my original idea of keeping track of whether first element was used:
    # only 3 elements, only 4 elements, first and second elements being the same, etc
    # FIRST IDEA WAS BAD!
    
# neetcode solution:
# same exact concept

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        # the nums[0] is for the edge case for if the list has 2 or less indexes

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2