class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # graph problem
        # NOTE THAT WE ARE CONSIDERING O'S AS REGIONS
        # so we have to make sure ALL CONNECTING O'S are surrounded for
        # us to turn them into x's

        # TRICK: an O region will not be surrounded if one of the O's are at the edge of the board

        # iterate through the outside of the board, and for every O that is on the outside
        # we will do a dfs of the left, right, up, and down positions
        # and mark them so that we know that the region is not surrounded
            # we can mark them by temporarily changing them to a "T" (doesn't matter what this is)
        # any "O" that wasn't marked means that it is in a region that is surrounded

        # this kind of thinking is called REVERSE THINKING
        # instead of checking for all regions that are surrounded, we find all the regions that
        # are UNSURROUNDED, and then just don't flip those!

        # time complexity: O(2 * m * n) => O(m * n)

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            if (r not in range(rows)
                or c not in range(cols)
                or board[r][c] == 'X'
                or board[r][c] == 'T'):
                return
                # if the cell is not in the board or it is an X or it has already been changed to a T
                # then simply return
                # could also write "not r in range(rows)" for example but this is a stylistic choice

            else:
                board[r][c] = 'T'

                directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

                for row, col in directions:
                    dfs(row, col)
        
        for c in range(cols):
            # iterating over top and bottom edges to check for edge O's
            if board[0][c] == 'O':
                dfs(0, c)
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)

        for r in range(rows):
            # checking left and right edges for O's
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    # change it back to an 'O' if it was marked as a T
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    # if the cell was not marked and it is part of a surrounded region
                    # then change it to an X
                    board[r][c] = 'X'
        
# neetcode solution:
# same solution but with slightly different styling
# also takes up extra work because it goes through entire grid 3 times
# while I go through the edge of grid once and
# through the entire grid once

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O":
                return
            board[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r in [0, ROWS - 1] or c in [0, COLS - 1]):
                    capture(r, c)

        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
