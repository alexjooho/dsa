class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1-d DP problem
        # MOST IMPORTANT PART IS TO REALIZE THAT YOU NEED TO GET A TOTAL
        # THAT IS EQUAL TO HALF THE ARRAY'S SUM!!!
        # making a recursive function that either adds current value or doesn't 
        # would result in a O(2^n) time complexity, which is BAD

        # so instead we can keep a cache (set) with all possible targets and add new
        # targets as we iterate through array
        # O(n * sum(nums)/ 2) time and space complexity -> O(n * sum(nums))
        # sum(nums) is since for every possible num up to the sum/2 target, we could have
        # a value in the cache set

        total = sum(nums)

        if total % 2 != 0:
            return False
        
        half = total // 2
        # NOTE: do // so that it stays an int instead of float

        targets = set()
        targets.add(half)

        for num in nums:
            if num in targets:
                # if the number is a valid target to reach half, then return True
                return True
            for target in targets.copy():
                # iterate through possible targets and add new ones which respresent
                # adding this number to the subset (by subtracting from current targets)
                # NOTE: have to do targets.copy() to make a snapshot since otherwise we would be changing
                # the size of original set during an iteration, which leads to error
                if num < target:
                    # only add new target if the current num is smaller than target
                    targets.add(target - num)
            
        return False
        
# neetcode solution
# he goes backwards for some reason

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False
