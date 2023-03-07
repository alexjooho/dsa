class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # O(nlogn) + O(n^2) -> O(n^2) time complexity
        # O(n) space complexity for result
        # sort list
        # iterate through list
        # for each index, use two pointers to find a sum that equals 0 if possible
        # this will eliminate any duplicates since the first number will always be from a different index

        # edge cases: careful for duplicate numbers during iteration of loop, and while moving pointers

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # Skip positive integers
            if a > 0:
                break

            if i > 0 and a == nums[i - 1]:
                continue
                # this is to skip numbers that we've seen already

            l, r = i + 1, len(nums) - 1
            # we don't need to do a len(nums - 2) in the for loop above because if it gets past that index
            # l will be > r so it will skip this entirely
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # technically don't even need the r -= 1 since if left side changes, the right side will
                    # automatically move to the left due to the code above
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res