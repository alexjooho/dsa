class Solution:
    def trap(self, height: List[int]) -> int:
        # for every position, calculate the amount of water it can hold
        # by first looking at the min height between the max left and max right pillars
        # then we subtract the current position's height from it and that'll give us the current
        # position's amount of water

        # min(L, R) - height[i]
        # if it's 0 or negative, don't add it to the total

        # Time complexity: O(n), space complexity: O(1)

        # original solution (O(n) space): iterate through array twice and create an array
        # for max left and max right. iterate once for max left, iterate once for max right
        # then for third iteration, just calculate the amount of water in each position

        # for O(1) memory solution: use two pointers
        # left pointer at beginning, right pointer at max
        # move the pointer that has a lower max value
        # with this solution, we're technically not finding both the max left and max right values
        # but instead we're only getting the smaller of the two, since we only care about the min of the two
        # calculate current position's value of whichever pointer got moved last

        # NOTE: first and last index can't contain any water, that's why it's ok for us to do the
        # calculation before we go to the next index during the while loop

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            # don't need to worry about doing an extra addition where l = r since at that point,
            # they will both be at the index of the highest height, and so the addition will be 0
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
                # don't need to check if the calculation is negative since leftmax was updated before doing calculation
                # if we updated leftmax after doing calculation, then we would have to check for negative
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
