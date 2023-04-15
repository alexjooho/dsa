class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers
        # if sum is less than target, move left pointer one
        # if sum is more than target, move right pointer one
        # there will always be a solution, so no need to worry about not finding one

        # once solution is found, return indexes + 1

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1

            elif numbers[l] + numbers[r] > target:
                r -= 1

            else:
                return [l + 1, r + 1]
            
# neetcode solution:
# same but uses a variable to store the current total

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
