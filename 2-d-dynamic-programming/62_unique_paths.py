class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dynamic programming problem
        # robot can only move right or down, so:
        # every cell in first row is 1
        # every cell in first column is 1

        # time complexity O(n * m), space complexity O(n * m)
        # could reduce space complexity by simply using a 2 or even 1 row array

        # NOTE: I originaly filled each of these cells with their respective index
        # but it's not about how many steps it takes, its about how many unique
        # paths there are. And there's only ONE way to get to any of these cells:
        # directly right or directly down nonstop

        # for every given cell in second and higher rows, there are
        # (left cell) + (right cell) ways of getting to the cell

        # create a 2-d array of size m x n and fill it in until the last cell

        grid = [[0] * n for row in range(m)]
        # NOTE: [[0] * n] * m WILL NOT WORK, it will make each row
        # the same instance

        # fill out left most column and top most row with 1
        for i in range(n):
            grid[0][i] = 1

        for i in range(m):
            grid[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
                # current cell's value is value of top + left

        return grid[m - 1][n - 1]

# neetcode solution:
# not as intuitive imo because it goes backwards and keeps making newRow
# this solution uses 2 1-row arrays (basically using a 2-row array total)
# so it saves space complexity

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m - 1):
            # skipping bottom row
            newRow = [1] * n
            # newRow will be the row above the old row
            for j in range(n - 2, -1, -1):
                # starting at second to last position (column)
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # time: O(n * m) space: O(n)