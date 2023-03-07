class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers
        # calculate area with (i2 - i1) * min(height[i1], height[i2])
        # if left pointer is smaller, move it, otherwise move right pointer (move either if they are equal)
        # smaller height is always the limiter in this problem

        max_water = 0

        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_water = max(area, max_water)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_water