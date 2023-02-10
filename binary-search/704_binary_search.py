class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # simple binary search question
        # divide list in half (since it's ordered) and search in
        # lower half if the number is lower than the middle number, or upper half otherwise
        # use a lower and upper pointer, and update lower or upper depending on if number is greater
        #   less than or greater than midway point (don't just use the average index since you already checked it
        #   use the average index + or - 1)
        # keep going until the number is found or the list is exhausted
        
        # could brute force by making a copy of half the needed list every time, but that would take up too much space

        # CAREFUL FOR EDGE CASES (e.g. target is lower than lowest value)

        # instead of doing while lower != upper, you should do while upper - lower > 1 to avoid edge cases with a list of 2

        lower = 0
        upper = len(nums) - 1

        while upper - lower > 1:  # can just do while lower <= upper
            middle = math.floor((lower + upper) / 2)  # can just do // to equal math.floor

            if target == nums[middle]:
                return middle

            if target > nums[middle]:
                lower = middle + 1
            
            if target < nums[middle]:
                upper = middle - 1

        if target == nums[lower]:
            return lower
        elif target == nums[upper]:
            return upper
        else:
            return -1
            
    
    # neetcode solution:
    
    # this solution is better because it doesn't require the extra lines of code from line 32-35
    # this is because the while loop keeps going until lower and upper equal each other, and then stops
    
    # class Solution:
    # def search(self, nums: List[int], target: int) -> int:
    #     l, r = 0, len(nums) - 1

    #     while l <= r:
    #         m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow   # this is if the numbers are REALLY big
    #         if nums[m] > target:
    #             r = m - 1
    #         elif nums[m] < target:
    #             l = m + 1
    #         else:
    #             return m
    #     return -1