class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do a binary search of the rows
        # then do a binary search within the row

        row = None

        t, b = 0, len(matrix) - 1

        while t < b:
            middle = (t + b) // 2

            if matrix[middle][0] <= target <= matrix[middle][-1]:
                row = middle
                break

            if target > matrix[middle][-1]:
                # if target is greater than the last value in the middle row,
                # then the top row pointer goes to row after middle row
                t = middle + 1
            
            else:
                # otherwise, bottom row pointer goes to middle row
                b = middle
        
        row = t if not row else row
        # the above while loop will always go until the row is found or if t == b and that is the row
        # if the row has not been found, it will be the t or b pointer (either works)
            # NOTE: this row might not even include the actual value within its ranges though
        # if the row HAS been found, simply keep it

        l, r = 0, len(matrix[0]) - 1

        while l < r:
            middle = (l + r) // 2

            if target == matrix[row][middle]:
                return True
            
            if target > matrix[row][middle]:
                l = middle + 1
            
            else:
                r = middle - 1
        
        return target == matrix[row][l]
        # the above while loop will either find the value of have left and right pointers equal to each other
        # if the left/right pointer is the target, return true. otherwise, return false
        
        
# neetcode solution:
# basically same solution except he just broke the loop once the target was within
# bounds of the "middle" row, and simply set the row value to the "middle" row after the loop

# he also does a fail fast check after the row finding while loop to see if the valid row was
# not found. (if not top <= bot: return False)

# he uses <= instead of < so that he can simply return true or false after the loop

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
