class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # create sets to keep track of numbers for each row, col, 3x3 box
        # time complexity will be O(9^2) and space complexity will be O(9^2)
        # iterate over entire board once

        # for boxes, label their sets by their position row-wise and column-wise
        # e.g. top left box is (0, 1)
        # for any given cell, // 3 both the row and column to get which box it is in

        # keep a dictionary that holds all the hash sets we need
        # use collections.defaultdict(set) to make it easy for us since
        # defaultdict lets us add to/check a key that hasn't been made yet

        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r //3, c //3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True