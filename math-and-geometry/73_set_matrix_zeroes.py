class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # iterate through matrix
        # to find all 0's
        # keep track of which rows and columns should be changed to 0 by using sets
        # afterwards, update them to 0's by iterating through sets

        # original idea was to update row/col as each 0 was found, but that could result in O((m * n) ^ (m * n))
        # while this solution is simply O(3 (m * n)) time complexity which is O(m * n)
        # could optimize solution by simply iterating only one extra time (so 2 times total) and if the cell
        # is within a row or col in rows or cols sets, then change to 0
        
        # O(m + n) space complexity

        rows = set()
        cols = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for row in rows:
            for i in range(len(matrix[0])):
                matrix[row][i] = 0

        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0
                
# neetcode solution:
# his solution is O(1) space complexity instead of O(m + n)

# basically he just changes the 0th index of a row/col to 0 if it needs to be changed to all 0's
# this works because we are iterating through the matrix from the top left
# so changing the top-most index of a column or left-most index of a row will not lead to
# repeats where we look at a 0 multiple times

# one extra thing we need is a variable for the 0th row, since changing [0][0] would indicate
# that both the row and column need to be changed
# since we can't let them overlap, we use [0][0] to signify column and have a separate variable
# for row zero. this is the only variable we need since others wont overlap

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        # O(1)
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        # determine which rows/cols need to be zero
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    # indicating that column needs to be all 0's
                    if r > 0:
                        matrix[r][0] = 0
                        # indicating that row needs to be all 0's
                    else:
                        rowZero = True
                        # if it was in the 0th row, then use rowZero variable

        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    # using row/col indicators to update cell
                    matrix[r][c] = 0

        if matrix[0][0] == 0:
            # have to do this separately for row/col of 0th row
            for r in range(ROWS):
                matrix[r][0] = 0

        if rowZero:
            for c in range(COLS):
                matrix[0][c] = 0