class Solution:
    def jump(self, nums: List[int]) -> int:
        # greedy problem where we kind of utilize two pointers/sliding window
        # for each jump, we update left and right pointers to include the next pointer after
        # the previous max jump (left), and the max jump (right)

        # we iterate through this "jump window" to see what is the next greatest jump to update 
        # the new window and increment our jump counter
        
        # basically doing a BFS of each possible jump distance to see which one will give us the next 
        # greatest jump distance each time

        # could do DP, but that would be O(n^2) instead of O(n)

        jumps = 0

        l, r = 0, 0
        # left and right pointers start at 0 because we haven't checked how far it can jump yet

        while r < len(nums) - 1:
            # once the right pointer reaches the last index, we stop

            max_right = r + 1
            # the max right will at the least be 1 more than the right most index in the current window

            for i in range(l, r + 1):
                if i + nums[i] > max_right:
                    # if the current index value + the index is greater than max right, update it
                    max_right = i + nums[i]

            l, r = r + 1, max_right
            # update the left and right pointers
            # the left pointer will now start at the next index that hasn't been checked
                # aka the index after the previous right pointer
            # the right pointer will be at the max right index from checking all the indexes between l and r

            jumps += 1
            # increment jumps by one
        
        return jumps
    
# neetcode solution:

class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < (len(nums) - 1):
            maxJump = 0
            # instead of max = r + 1, he just did 0 since it will automatically get updated anyways
            for i in range(l, r + 1):
                maxJump = max(maxJump, i + nums[i])
            l = r + 1
            r = maxJump
            res += 1
        return res
