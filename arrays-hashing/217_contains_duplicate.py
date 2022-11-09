class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False
        
# Other solution:
# return len(nums) != len(set(nums))

# this solution takes longer run time though 