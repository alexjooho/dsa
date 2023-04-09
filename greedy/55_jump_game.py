# greedy solution from neetcode:
# O(n) time complexity!

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # start from end of the list and make that your "goal"
        # go backwards from that point and update goal every time an
        # index has a value that can jump to current goal
        # if the goal ends up being at the start, then return true

        # since we are checking each index to see if it can reach the goal
        # it is greedy (we are trying to find local optimal solution each time)

        goal = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                # update goalpost if current index can reach goal
                goal = i

        return True if goal == 0 else False
    
# can also start from the beginning:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = 0
        # starting from beginning

        for i in range(len(nums)):
            if i > goal:
                # if i is past the current goal, then it can't go further and it fails
                return False

            goal = max(goal, nums[i] + i)
            # have to do max to see if the goal post has now moved up

        return True
        # if we finish the loop, that means that goal >= i where i is the last index


# first brute force recursive solution:
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # recursively go through each index
        # for each value, start with highest jump and go down to 1
        # recursively call dfs for each jump at new index
        # if an index can not lead to the last index, change its value to 0
        # base case: if value == 0, return False
            # if idx out of range, return False
            # if idx is last index, return True
        
        # time complexity: O(n^2) because for every index, could possibly have to check
        # every other index

        n = len(nums)

        def dfs(idx):
            if idx == n - 1:
                return True

            if idx >= n:
                return False

            if nums[idx] == 0:
                return False

            for i in range(nums[idx], 0, -1):
                # going backwards from longest jump
                if dfs(idx + i):
                    return True
                
            nums[idx] = 0
            # if this index can not lead to the final index, set it to 0 to cache that its a fail

            return False

        return dfs(0)