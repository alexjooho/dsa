class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search O(log n)
        # keep left and right pointers
        
        # in a rotated sorted array, there will be a pivot point
        # we need to see if we are in the left sorted portion or right sorted portion
            # basically, if left is sorted, then the right side has the pivot point
            # if right is sorted, then the left side has the pivot point
            # and then check the sorted side for if target is within it
        # do this by checking mid value with left or right value (in this solution, left)
        
        # then we can check if the target value will be in the left or right side of middle
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                # have to do <= since the left can equal the middle in a small sized array
                if target > nums[mid] or target < nums[l]:
                    # might be cleaner to write: nums[l] < target < nums[mid] and do r = mid - 1 and change line 30
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    # might be cleaner to write: nums[mid] > target > nums[r] and do l = mid + 1 and change line 37
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
# other solution by finding pivot index and then searching the appropriate part of the array:

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search O(log n)
        # use binary search to search for pivot index (index of highest value basically)
        # keep track of value of first index for reference
        # if middle is smaller than left value, then pivot is on left side, else right side
        # then use binary search to search in correct side of the array

        l, r = 0, len(nums) - 1

        while r - l > 1:
            mid = (r + l) // 2
            if nums[l] > nums[mid]:
                r = mid - 1
            else:
                l = mid
            # since we have r = mid -1 and l = mid, the final array can either be size 2 or 1
        
        pivot = r if nums[r] >= nums[l] else l

        if nums[0] <= target <= nums[pivot]:
            l, r = 0, pivot
        else:
            l, r = pivot + 1, len(nums) - 1
        
        while l <= r:
            mid = (r + l) // 2

            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1