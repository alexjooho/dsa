class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # for any given cell, replace the 90 degree cell with it and store the replaced cell
        # then for that value, put it in its 90 degree rotation cell and repeat
        # only have to do this for ((last index #) // 2) rows
        # since that is when we'll have finished going through every cell

        # for each cell, first replace the cell at row = col and col = (-row - 1)
            # this represents the first 90 degree rotation
        # second, replace the cell at row = (-row - 1) and col = (-col - 1)
        # third, replace the cell at row = (-col - 1) and col = (row)
        # finally, replace the cell at row = row and col = col

        # have 4 replacements because there are 4 90 degree changes
        # NOTE: make sure not to include last index of a spiral's row (so decrease right edge by an extra 1)
            # or else the index will be replaced multiple times
        # NOTE: to avoid repeat replacements, we basically have to shift inwards our top, bot, left, and right pointers
            # in this case, only have to do left and right since we handle top with our i (row)
            # and we don't have a bot pointer since we just use -i for it when necessary
            
        # original thought process was to store entire row/column, but that makes the problem very annoying
        # instead, for each cell, simply replace its 4 corresponding 90 degree cells to take care of it at once
        
        # O(n^2) time complexity (since its an n x n matrix, but we technically only visit each cell once)
        # O(1) space complexity since we just have 2 variables
        # could technically only need 1 variable if we save the value of current cell, then go in reverse order
        # e.g. 4th cell to current, 3rd to 4th, 2nd to 3rd, and then finally 1st to 2nd

        length = len(matrix[0])

        for i in range(((length - 1) // 2) + 1):
            for j in range(i, length - i - 1):
                # DON'T INCLUDE LAST INDEX OR ELSE IT WILL REPEAT THE CORNER REPLACEMENTS!
                # the i and the -i will basically make sure the rotating spiral decreases with every row
                    # this brings closer the left and right edges so repeats don't occur
                # the -1 makes sure the last index of the spiral is not included so it doesn't repeat it

                prev = matrix[i][j]
                replaced = matrix[j][-i - 1]
                matrix[j][-i -1] = prev
                prev = replaced
                # this is the first replacement

                replaced = matrix[-i -1][-j - 1]
                matrix[-i -1][-j -1] = prev
                prev = replaced
                # second replacement

                replaced = matrix[-j -1][i]
                matrix[-j -1][i] = prev
                prev = replaced
                # third replacement

                matrix[i][j] = prev
                # fourth and final replacement doesn't need a replaced variable because it's finished
                
# neetcode solution:
# basically same solution, but instead of using the negative values of i and j,
# he keeps a left and right pointer and updates them
# he uses these for top and bottom as well since it is a square
# because he uses pointers, he can use the i in the for loop to add or subtract from top/bot/left/right
# to find each of the 4 90 degree cells.
# this is slightly easier than mine where I had to find the relationship with negative values of each

# he also only uses one variable (topLeft), since he replaces the cells in reverse order as noted in space complexity above

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        while l < r:
            # if n is odd, then it will skip the beneath for loop and exit loop afterwards
            # if n is even, it will do the for loop at the end and then exit
            for i in range(r - l):
                # r - l is so that it only goes through the indexes within the spiral
                # while avoiding the last right index (to avoid repeat of corner replacements)
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l + i]

                # move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1