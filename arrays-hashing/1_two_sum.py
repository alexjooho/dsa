class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # make a dictionary that has keys of values needed to reach the sum, and the index of the original number
        # if a number is in the dictionary, return the index of other number and current number in a list
        # if a number is not in the dictionary, add a key that is the number needed to reach the sum with current number,
        # with a value of the current number's index

        sum_hash = {}

        for i in range(len(nums)):
            if nums[i] in sum_hash:
                return [sum_hash[nums[i]], i]
            else:
                sum_hash[target-nums[i]] = i


# neetcode solution:
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}  # val -> index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i

# this solution uses enumerate, and also just puts in the current number into dictionary instead of
# calculating the difference beforehand