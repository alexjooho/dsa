class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # binary search problem
        # the minimum number of bananas Koko can eat per hour is 1
        # the maximum number of banananas Koko can eat will be the biggest (max) pile
        # in the piles list

        # we have to check each of the values from the min to max to see which one allows
        # Koko to eat all the bananas within the hour time limit while being the slowest speed
            # for each speed, we iterate through piles list to calculate the hours it takes to finish

        # the brute force solution would be to check each speed from min to max
        # this would give us O(max(p) * p) time complexity

        # better solution is to do a binary search
        # O(log max(p) * p) time complexity
        # left and right pointers. if middle time is enough to finish eating in time,
        # then move right pointer to middle - 1, otherwise move left pointer to middle + 1
        # keep track of minimum speed that satisfies conditions

        import math

        l, r = 1, max(piles)
        # left and right pointers at minimum (1) and maximum (max pile size since that's the most Koko can eat)
        # these are the left and right speeds at which Koko is eating bananas

        min_speed = float('inf')
        # technically we could set this to r (max(piles)) instead of infinity since the max speed will definitely
        # be a valid speed

        while l <= r:
            # we do <= so that when they are equal, we still check if it is the minimum speed

            middle = (l + r) // 2
            hours = 0
            # keep track of hours

            for pile in piles:
                hours += math.ceil(pile / middle)
                # do ceiling since we can only get whole hour numbers

            if hours <= h:
                # if the speed was fast enough to eat piles within the hour time limit
                min_speed = min(min_speed, middle)
                r = middle - 1
            else:
                l = middle + 1

        return min_speed
    
# neetcode solution is the exact same solution