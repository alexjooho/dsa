# neetcode solution
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # nums can contain duplicate numbers
        # to avoid duplicate subsets: for each index, we need to decide whether we add the index's NUMBER
        # or do not add any more of that NUMBER
        # then we go to the next index if we decided to add number, or the next index that isn't the same number
        # if we decided not to add that number
        # since our nums list is not guaranteed to be sorted, we need to sort it ourselves
        
        # idea behind this is that we never want to have to go repeat a path with a subset that has the
        # same amount of a certain number!
        # e.g. if we have 1, 2 and 1, 2, 2. we never want the 1, 2 subset to add another 2 to have the same
        # number of 2's

        # time complexity: O(n*2^n) because there could be 2^n subsets (since for each number we can either add or not add)
        # and each one can be up to size n
        # it's not O(n^2 * 2^n) since although we have a while loop within the iteration, it skips
        # any indexes that are the same number, so we don't actually revisit those indexes in that
        # decision tree

        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                # append a deep copy of array instead of the actual array
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            subset.pop()
            # make sure to pop afterwards so it is not included in future calls

            # All subsets that don't include nums[i]
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                # since we don't want to include this number anymore in this recursive call,
                # we keep iterating through list until the number at the index is different!
                i += 1
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res