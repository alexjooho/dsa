class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # use a hash set to keep track of numbers that have been seen
        # iterate through list to add each seen number to set
        # then iterate through range to check each value
        # this will be O(2n) time complexity and O(n) space complexity

        seen = set()
        n = len(nums)

        for i in range(n):
            seen.add(nums[i])

        for i in range(n + 1):
            if not i in seen:
                return i

        # could also make a set by doing set(list(range(0, len(nums)))) and then remove values until only one is left
        # remove last value with set.pop()
        
# neetcode solution:
# this makes the solution O(1) space complexity
# res += i - nums[i] is done instead of summing both the list and the range from 0 to n
# because it is O(n) instead of O(2n) time complexity

# Subtracting the sum of the list from the sum of all numbers in the range will give the missing number but will be O(2n) (unless you use n(n+1)/2 formula)
# instead, can just subtract differences from the result that starts at the highest value and then return result

# res = len(nums) to start because in the for loop, it never reaches an i of len(nums) so it
# needs to be accounted for before the loop

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)

#         for i in range(len(nums)):
#             res += i - nums[i]
#         return res

# bit manipulation solution with XOR:
# important to note that order does not matter for XOR (has both associative and communicative properties)
# and XOR of the same 2 numbers will always cancel out to 0

# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         res = len(nums)
#         for i in range(len(nums)):
#             res ^= i ^ nums[i]
#         return res