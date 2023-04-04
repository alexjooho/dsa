class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane's algorithm
        # both a dp and greedy algorithm
        # keep track of best max at each index
        # compare curr + val, and val
        # kind of similar to sliding window!

        res = nums[0]
        # can't do 0 for this because array could have negative numbers

        curr_max = float('-inf')
        # could technically also do 0 since this value will always be updated
        # before being compared with res

        for num in nums:
            curr_max = max(curr_max + num, num)

            res = max(res, curr_max)

        return res