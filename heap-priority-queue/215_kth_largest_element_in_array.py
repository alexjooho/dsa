# easy solution would be O(n + klog n), which would be to heapify array
# and then pop k times
# or could just keep min heap with size k, and then return heap[0]

# O(n) solution is actually done with quick select

# NOTE: BOTH OF THESE ARE NEETCODE'S SOLUTIONS

# Solution: Sorting
# NOTE: This is actually not the valid solution, but on leetcode it gives better results
# Time Complexity:
#   - Best Case: O(n)
#   - Average Case: O(n*log(n))
#   - Worst Case:O(n*log(n))
# Extra Space Complexity: O(n)
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


# Solution: QuickSelect
# Time Complexity:
#   - Best Case: O(n)
    # explanation: array we do quick select on goes from n to n/2 to n/4 ... etc
    # since we only do it on one side. n + n/2 + n/4 + ... is equivalent to 2n so O(2n) => O(n)
#   - Average Case: O(n)
#   - Worst Case: O(n^2)
# Extra Space Complexity: O(1)
class Solution2:
    # for a given pivot, we put elements less than it to the left side
    # and elements > than pivot to the right side
    # we do this by having a left pointer and iterating through array
    # if the value is <= pivot, we swap it with the value at the left pointer and +=1 pointer
    # we keep doing this until we finish iterating and then swap pivot with pointer's value
    # this works because if pointer is <= pivot, it will just swap with itself
    # and pointer will be at either the current i position if all values were < pivot or it will
    # be at the first position where value was > pivot!
    
    # we do this recursively but it is O(n) best/average case instead of O(n log n) like 
    # quick sort, since we only worry about one side of the pivot that holds the kth largest
    
    # NOTE: look at neetcode's video for a quick select solution with just one function
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot, fill = nums[right], left
        # we choose right-most value as the pivot since it is simple and we don't have to move it
        # to the end again if we choose right-most value
        # fill is the left pointer

        for i in range(left, right):
            # iterate through entire array excluding right value (the pivot)
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1
                # we update left pointer (fill) so that it will swap with next index now

        nums[fill], nums[right] = nums[right], nums[fill]
        # swap positions of pivot and the pointer (the pointer is the first position with value > pivot)

        return fill
        # we return the index that the pivot is now in, since pivot went to fill's index

    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        # this is the index we are trying to find
        left, right = 0, len(nums) - 1
        # original starting pointers

        while left < right:
            # if left > right, that means we have sorted the entire list
            pivot = self.partition(nums, left, right)
            # keep recursively calling on new left and right pointers

            if pivot < k:
                # we want to search within the values greater than pivot if pivot is < k
                left = pivot + 1
            elif pivot > k:
                # if pivot > k, we want to search within values < pivot
                right = pivot - 1
            else:
                # if pivot == k, that means that pivot is the kth largest value
                break

        return nums[k]