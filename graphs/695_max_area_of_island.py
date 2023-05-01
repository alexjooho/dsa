class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # graph problem similar to number of islands
        # use dfs
        # whenever we reach a cell with a 1,
        # we recursively call the cells of all 4 directions
        # and add 1 + left + right + up + down

        # time complexity: O(5 * n * m) => O(n * m)
        # since for each cell, we can possibly visit it 5 times (directly, left, right, up, down)
        
        # O(1) space complexity for my solution

        res = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (not r in range(rows)
                or not c in range(cols)
                or grid[r][c] == 0):
                return 0
                # if out of bounds or the cell is 0, then return 0
            
            # if the cell is valid, we will turn it into a 0 so that it doesn't get counted again
            # and we will get its total by adding up all of its sides + 1
            grid[r][c] = 0

            left, right, up, down = dfs(r, c - 1), dfs(r, c + 1), dfs(r - 1, c), dfs(r + 1, c)

            return 1 + left + right + up + down

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    res = max(res, dfs(row, col))

        return res
    
# neetcode solution:
# same solution using dfs but he uses a seen set so it costs O(m * n) memory instead of O(1) like mine
# the "OR" statements are a little cleaner because it doesn't need to use NOT

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (
                r < 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0
                or (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area
