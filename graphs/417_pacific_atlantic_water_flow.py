# neetcode solution:
# O(m*n) time complexity (does this twice) and same space complexity but x4

# started from outer edge and checked all 4 sides
# if already seen, skip it
# recursive dfs
# trick is to use same parameters for functions, but insert different visited sets so that you can
# use same function for both pacific and atlantic!
# start from outer edge for each respective ocean

# don't need to put in a bunch of logic about whether it is valid before calling the recursive function
# instead, LET THE RECURSIVE FUNCTION DO THE WORK FOR YOU WITH ITS BASE CASE :)

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

# my wrong solution:
# had the right general idea of going from outer to inner but only checked in 2 directions instead of all 4
# my wrong solution wasn't really following the essence of a dfs, and I should've instead starting from 
# a single cell and checked all directions
# NOTE: FOR EACH OUTER CELL CALL THE ENTIRE DFS!
# I tried to make a dfs function for pacific and one for atlantic but neetcode used one dfs for both
# since it checks all directions anyways

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # graph problem
        # recursive dfs starting from outside, and updating each inner cell for if > outer cell and outer cell goes to ocean
        # one dfs for pacific ocean, one dfs for atlantic ocean

        # for pacific ocean: start from top left corner and go right. and then go from one below top left corner and go down
        # check left and upper values

        # for atlantic ocean: start from bot right corner and go left. and then one above bot right corner and go up
        # check right and lower values

        # time complexity: O(m*n*3) = O(m*n) since we loop through grid 3 times
        # space complexity: O(m*n*2) = O(m*n) since we create 2 sets

        # NOTE: this solution doesn't work if a future value turns out to be valid (e.g. for pacific ocean,
        # if a value to the right is valid, this code will not go back to compare with that value)

        pacific = set()
        atlantic = set()

        row, col = len(heights), len(heights[0])

        res = []

        def pacific_dfs(r, c):
            if r >= row or c >= col:
                return
            if r == 0:
                # for first function call
                for i in range(col):
                    pacific.add((r, i))
                for i in range(row):
                    pacific.add((i, c))
                
            else:
                for i in range(c, col):
                    # going towards right
                    if heights[r][i] >= heights[r][i-1] and (r, i-1) in pacific:
                        # comparing to left
                        pacific.add((r, i))
                    elif heights[r][i] >= heights[r-1][i] and (r-1, i) in pacific:
                        # comparing to upper
                        # need to do elif so that it doesn't add it twice
                        pacific.add((r, i))
                for i in range(r, row):
                    # going towards bottom
                    if heights[i][c] >= heights[i][c-1] and (i, c-1) in pacific:
                        pacific.add((i, c))
                    elif heights[i][c] >= heights[i-1][c] and (i-1, c) in pacific:
                        pacific.add((i, c))
            pacific_dfs(r+1, c+1)
            # dfs the next corner

        def atlantic_dfs(r, c):
            if r < 0 or c < 0:
                return
            if r == row - 1:
                # for first function call
                for i in range(col - 1, -1, -1):
                    atlantic.add((r, i))
                for i in range(row - 1, -1, -1):
                    atlantic.add((i, c))
                
            else:
                for i in range(c, -1, -1):
                    # going towards left
                    if heights[r][i] >= heights[r][i+1] and (r, i+1) in atlantic:
                        # comparing to right
                        atlantic.add((r, i))
                    elif heights[r][i] >= heights[r+1][i] and (r+1, i) in atlantic:
                        # comparing to lower
                        atlantic.add((r, i))
                for i in range(r, -1, -1):
                    # going towards top
                    if heights[i][c] >= heights[i][c+1] and (i, c+1) in atlantic:
                        atlantic.add((i, c))
                    elif heights[i][c] >= heights[i+1][c] and (i+1, c) in atlantic:
                        atlantic.add((i, c))
            atlantic_dfs(r-1, c-1)

        pacific_dfs(0, 0)
        atlantic_dfs(row - 1, col - 1)

        for r in range(row):
            for c in range(col):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        print('pacific', pacific, 'atlantic', atlantic)

        return res
    
# bfs solution from leetcode online:
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        rows, cols = len(heights), len(heights[0])
        
        # Create visited matrices for both oceans
        pacific_visited = [[False] * cols for _ in range(rows)]
        atlantic_visited = [[False] * cols for _ in range(rows)]
        
        # Create queue for both oceans
        pacific_queue = deque()
        atlantic_queue = deque()
        
        # Add cells in the first and last rows to their respective queues
        for col in range(cols):
            pacific_queue.append((0, col))
            atlantic_queue.append((rows-1, col))
            pacific_visited[0][col] = True
            atlantic_visited[rows-1][col] = True
        
        # Add cells in the first and last columns to their respective queues
        for row in range(rows):
            pacific_queue.append((row, 0))
            atlantic_queue.append((row, cols-1))
            pacific_visited[row][0] = True
            atlantic_visited[row][cols-1] = True
        
        # Define helper function to check if a cell can flow to an ocean
        def bfs(queue, visited):
            while queue:
                row, col = queue.popleft()
                # Check adjacent cells
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    r, c = row + dr, col + dc
                    # Check if cell is within bounds and hasn't been visited yet
                    if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                        # Check if cell can flow to the ocean
                        if heights[r][c] >= heights[row][col]:
                            visited[r][c] = True
                            queue.append((r, c))
        
        # Run BFS on both oceans starting from the boundary cells
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
        
        # Find the cells that can flow to both oceans
        result = []
        for row in range(rows):
            for col in range(cols):
                if pacific_visited[row][col] and atlantic_visited[row][col]:
                    result.append([row, col])
        
        return result