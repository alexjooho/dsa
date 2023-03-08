class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # have to consider whole array at start since rotation could be anywhere
        # looking for index where its value is less than index - 1's value
        # compare middle index value to left and right most index values
        # if both are less, use the right side of array since that means the turning point is on right side
        # if both are more, use left side of array since that means the turning point is on the left side
        # if left is less than right, then left is the minimum value
        
        # O(log n)

        l, r = 0, len(nums) - 1

        while (r - l) > 1:
            mid = (r + l) // 2
            
            if nums[l] < nums[mid] and nums[r] < nums[mid]:
                l = mid
            elif nums[l] > nums[mid] and nums[r] > nums[mid]:
                r = mid
            elif nums[l] < nums[r]:
                return nums[l]

        return min(nums[l], nums[r])

# Neetcode solution:

# his solution basically keeps track of the min number seen and keeps updating it
# only compares to the right side of the list each time to see whether to halve to left or right
# also doesn't include the middle number since it always goes + 1 or - 1 of it
# at the end, he checks if the final array (of size 1) has the minimum value

# NOTE: IF THE RIGHT VALUE IS LOWER THAN MIDDLE, THEN NOTHING ON THE LEFT CAN BE LOWEST VALUE
# SINCE WE ALREADY PASSED ROTATION POINT AND NUMBERS WILL KEEP GOING UP

# if he compared to the left side, he would always have to check that the list is not in order

class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0 ,len(nums) - 1 
        curr_min = float("inf")
        
        while start  <  end :
            mid = (start + end ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return min(curr_min,nums[start])