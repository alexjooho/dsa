class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # keep left, right, top, and bottom pointers
        # if left > right or top > bot, then stop iterating
        # otherwise, keep going in a spiral motion, stopping after every direction meets a pointer
        # keep incrementing/decrementing pointers

        # NOTE: need to do an if statement to break at any given point since its not a square matrix
        # and since it could technically spiral and repeat cells (e.g. example 2 it went from 6 -> 7 and then repeated 6)
        
        # could use a helper function to make it less lines of code, but it makes it more confusing imo

        l, t = 0, 0
        r, b = len(matrix[0]) - 1, len(matrix) - 1

        res = []

        while l <= r and t <= b:
            # have to do <= instead of < since = means its still valid

            for i in range(l, r + 1):
                # left to right
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break
            # could technically do this break and the (if l > r) break after the top to bot on right side
            # since we are going from top to bot next so if t > b, then the for loop won't even happen
            # top incremented by 1 (goes down a row) since we finished top row

            for i in range(t, b + 1):
                # top to bot on right side
                res.append(matrix[i][r])
            r -= 1
            if l > r:
                break
            # right decremented by 1

            for i in range(r, l - 1, -1):
                # right to left on bot side
                res.append(matrix[b][i])
            b -= 1
            if t > b:
                break
            # actually don't need the break here since we are looping in range b -> t next so
            # if t > b, then the for loop below won't even occur
            # bot decremented by 1

            for i in range(b, t - 1, -1):
                # bot to top on left side
                res.append(matrix[i][l])
            l += 1
            # left incremented by 1
            # don't need another break if statement here since the while loop will do it automatically

        return res
    
# neetcode solution:
# implements the notes I have above about the breaks only being needed at certain points
# basically same code and concept

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        while left < right and top < bottom:
            # get every i in the top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            # get every i in the right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            # get every i in the bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            # get every i in the left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res