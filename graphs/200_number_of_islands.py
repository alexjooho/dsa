# my bfs solution
# NOTE: CAN TURN THIS INTO ITERATIVE DFS BY SIMPLY POPPING FROM RIGHT SIDE INSTEAD OF LEFT!
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate through grid
        # if a "1" is found and it has not been seen before, start making an island off of adjacent land and increment island count
        # go left, right, up, and down, and if that index has an island, add it to que and to the seen set
        # NOTE: can just change "1"'s to "2"'s to save space, and make it O(1) space complexity instead of O(m*n)
        # use BFS with deque (need to make a helper function for this)
        
        # O(n*m) time complexity, O(1) space complexity

        if not grid:
            return 0

        total = 0
        row, col = len(grid), len(grid[0])

        def bfs(m, n):
            # this bfs will start with a "1" index and then add its left, right, up, and down indexes if they also = "1"
            # if those indexes are "1", it will change them to "2" since they are now a part of the island
            # it will then change the current index to a "2"
            island = deque()
            island.append((m, n))
            grid[m][n] = "2"
            # this is so that we won't visit this index again

            while island:
                r, c = island.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # down, up, right, left
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r in range(row) and 
                        new_c in range(col) and 
                        grid[new_r][new_c] == "1"):

                        grid[new_r][new_c] = "2"
                        island.append((new_r, new_c))
            
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    bfs(r, c)
                    total += 1
        
        return total
    
# neetcode bfs solution (can turn into iterative dfs by simply popping from right):
# same exact concept except he uses a seen set which causes it to be O(n*m) instead of O(1) space complexity like mine

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited=set()
        islands=0

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
           
            while q:
                row,col = q.popleft()
                directions= [[1,0],[-1,0],[0,1],[0,-1]]
               
                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r ,c) not in visited:
                       
                        q.append((r , c ))
                        visited.add((r, c ))

        for r in range(rows):
            for c in range(cols):
               
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands +=1 

        return islands
    
# neetcode recursive dfs solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands