class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dynamic programming with Kadane's algorithm
        # have to keep track of current max and current min
        # update current max/min with product including current value
        # OR current value could also become new min/max if bigger/smaller

        # O(n) time complexity, O(1) space complexity
        # dp because we are solving subproblem of best solution
        # for subarrays ending at EACH individual index
        # the normal dp solution would use two arrays (one for max_product and one for min_product)
        # but this is also a greedy algorithm that uses the best option at each point
        # and therefore we just use 2 variables and lower the space complexity

        # somewhat similar to a sliding window!

        res = float('-inf')
        # could just use nums[0]

        curr_min = 1
        curr_max = 1
        # have to use 1 so when it multiplies, it will be updated

        for num in nums:
        # for every value, we update curr_min/curr_max FIRST
        # BEFORE possibly updating res
            temp = curr_max
            # need a temp for updating curr_min if curr_max was updated

            curr_max = max(num * curr_max, num * curr_min, num)
            # the new max can be obtained from current val, val * curr_max,
            # or val * curr_min if val is negative

            curr_min = min(num * temp, num * curr_min, num)

            res = max(res, curr_max)
            # keep checking if new curr_max is > res

        return res