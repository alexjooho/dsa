class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # brute force would be 2^n since for every number
        # we have to decide whether we put it in the subsequence or not
        # yes/no decision, n times
        # naive idea was that just a nested for loop would give us answer, but
        # it doesn't because just because a number is bigger than previous
        # doesn't mean that its in the ideal longest solution

        # we should use dp to get O(n^2)
        # can use recursion dfs with cache or use bottom up DP ->

        # work from the end and then work backwards
        # for every value, we check the max of current total or 1 + total
        # for each index after it that has a higher number

        # basically checking local max length of subsequence for each index
        # until we finally get to the beginning of the list
        # and then finding the largest length in totals list

        # NOTE: unlike 2-d subsequence array dp problems (ones with letters that look for same letter),
        # we just keep local max instead of shifting the max over to other indexes

        total = [1] * len(nums)
        # every index has a minimum max sequence of 1 (itself)

        for i in range(len(nums) - 1, -1, -1):
            # for every single index
            for j in range(i + 1, len(nums)):
                # for every index after the index that has a calculated
                # local max already
                if nums[i] < nums[j]:
                    # to make sure that nums[j] is even valid (greater)
                    total[i] = max(total[i], total[j] + 1)
                    # if adding 1 to the already calculated index
                    # is greater than current index's value,
                    # then update it

        return max(total)

# dp starting from beginning:
def lengthOfLIS(self, nums: List[int]) -> int:
	total_number = len(nums)
	dp = [0 for _ in range(total_number)]
	for i in range(1, total_number):
		for j in range(i):
			if nums[j] < nums[i]:
				dp[i] = max(dp[i], dp[j] + 1)
	return max(dp) + 1

# binary search O(n logn) solution:
# https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
# I didn't spend time to learn this solution (patience sort)

def lengthOfLIS(self, nums: List[int]) -> int:
	tails = [0] * len(nums)
	result = 0
	for num in nums:
		left_index, right_index = 0, result
		while left_index != right_index:
			middle_index = left_index + (right_index - left_index) // 2
			if tails[middle_index] < num:
				left_index = middle_index + 1
			else:
				right_index = middle_index
		result = max(result, left_index + 1)
		tails[left_index] = num
	return result

# recursive solution:
# basically a dfs that has to be done starting from every index
# and if an index has already been dfs'd through, it will return its value
# for dp problems, recursive solutions typically have much worse
# time and space complexity

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # recursive solution

        total = [-1] * len(nums)
        # start off with -1 so we know if it's been visited

        def dfs(prev, ind):
            if total[ind] != -1:
                return total[ind]
                # for if this index has already been calculated

            res = 1
            curr = nums[ind]

            for i in range(ind + 1, len(nums)):
                if nums[i] > curr:
                    res = max(res, 1 + dfs(curr, i))

            total[ind] = res
            return res

        # return dfs(float('-inf'), 0)
        # can't do this because the 0th index might not be part
        # of longest subsequence

        # dfs(float('-inf'), 0)
        # CAN'T JUST DO DFS OF 0TH INDEX since it might not reach all indexes
        # and other indexes might be starting point

        for i in range(len(nums)):
            dfs(float('-inf'), i)

        return max(total)