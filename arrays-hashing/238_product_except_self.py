class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # iterate over the list 2 times
        # once for a "prefix" loop and once for a "postfix" loop
        # create an output list with n indexes that all equal 1 to start
        # while iterating for the prefix loop, keep track of current product and insert into output
        # list at index + 1
        # while iterating for the postfix loop, iterate backwards and insert into output at index - 1

        # basically keep track of total product at each index except that index's element
        # by multiplying all previous elements by all elements after it

        output = [1] * len(nums)

        prefix, postfix = 1, 1
        
        for i in range(len(nums) - 1):
            prefix *= nums[i]

            output[i + 1] *= prefix

        for i in range (len(nums) -1, 0, -1):
            postfix *= nums[i]

            output[i - 1] *= postfix

        return output
    
    # this is O(n) time complexity (technically 2n) and O(1) space complexity
    
# Neetcode solution:
# basically same solution except he just set res[i] to current prefix/postfix and then kept going

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1):
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res