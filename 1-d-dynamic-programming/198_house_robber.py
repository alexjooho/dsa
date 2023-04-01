class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming problem because each problem relies on another subproblem
        # basically, there are two choices: rob = max(arr[0] + rob[2:n], rob[1:n])
        # rob first house and then get the max you can rob from 3rd house onwards
        # or skip first house, and get max you can rob from 2nd house onwards
        # second part of both choices is the subproblem

        # fibonacci sequence problem because every new value depends on the last 2 values
        # n1 and n2 will be arr[0] and arr[1], respectively
        # for every value afterwards, if current value + n1 is > n2, then new n2 becomes val + n1
        # otherwise, n2 will just be the same
        # n1 always gets changed to the previous n2

        # we are basically just always checking whether robbing the current house will give us
        # a greater value than if we didn't rob it.
        
        # time complexity: O(n), space complexity: O(1)
        
        n = len(nums)

        if n <= 2:
            # edge case where list is 2 or less numbers
            return max(nums)

        n1, n2 = nums[0], nums[1]
        if n2 < n1:
            # edge case where second house is less value than first house
            # this could cause a problem if we want to skip next 2 houses after first house
            # e.g. [2, 1, 1, 2] would give us 3 instead of 4 if we don't do this
            # we do this in our for loop but it doesn't do it for first 2 houses
            # so we have to do it manually here
            n2 = n1

        for i in range(2, n):
            temp = n2
            if nums[i] + n1 > n2:
                n2 = nums[i] + n1
            n1 = temp

        return n2
    
# neetcode solution:
# he simply puts n1 and n2 as 0 so that he can start from the beginning of the array
# without having to worry about edge cases like my solution

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2