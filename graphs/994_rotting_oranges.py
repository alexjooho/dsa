# neetcode solution:
# time and space complexity: O(m * n)
# better than my solution because instead of having to iterate through the whole grid
# for each time point, he simply does a bfs starting from each rotten orange
# KEY DIFFERENCE FROM MY SOLUTION: uses rotten oranges as starting point and USES A QUE FOR BFS
# NOTE: MULTI-SOURCE BFS!

# start off by iterating through array and adding each rotten orange into the que
# also take note of how many fresh oranges it starts with

# then, while there are fresh oranges and there are rotten oranges in the que,
# pop however many are in the que currently (which is everything at this time point)
# and update their neighbors if it holds a fresh orange and change it to a rotten orange
# and update the fresh count
# update time after popping everything for the time point

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0

        # iterate through grid and add each rotten orange to the queue and count fresh oranges
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                # by doing this for loop, we are only popping the rotten oranges from this time stamp
                r, c = q.popleft()

                for dr, dc in directions:
                    # for every one of the 4 directions
                    row, col = r + dr, c + dc
                    # if in bounds and nonrotten, make rotten
                    # and add to q
                    if (
                        row in range(len(grid))
                        and col in range(len(grid[0]))
                        and grid[row][col] == 1
                    ):
                        # make it rotten, add it to the que, and decrement fresh oranges
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            time += 1
            # increment time

        return time if fresh == 0 else -1
        # if there are still fresh oranges, then return -1

# my solution:
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # graph problem (kind of like BFS)
        # iterate through grid once to find starting amount of fresh oranges
        # start time at 0
        # while there are still fresh oranges, keep iterating through grid
        # set a variable to the starting fresh oranges of that cycle
        # iterate through grid and for every fresh orange, check its 4 directions
        # for rotten oranges and update it and the # fresh oranges if there is a rotten orange
            # have to update it after iterating through entire grid first since we don't want 
            # them to be rotten and affect oranges it wouldn't have affected in current loop
            # update it after loop by keeping track of cells in a set
            
        # time complexity: O(m * n ^ (m * n))
        # since for each time there are still fresh oranges, we iterate through entire grid

        rows, cols = len(grid), len(grid[0])

        def check_rotten(r, c):
            # helper function to check if a cell holds a rotten orange
            if (r not in range(rows)
                or c not in range(cols)
                or grid[r][c] != 2):
                return

            else:
                return True

        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                # iterate through grid to find starting number of fresh oranges
                if grid[r][c] == 1:
                    fresh += 1

        while fresh > 0:
            rotten = set()
            starting = fresh
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1:
                        if (check_rotten(r + 1, c)
                            or check_rotten(r - 1, c)
                            or check_rotten(r, c + 1)
                            or check_rotten(r, c - 1)):
                            # check if any of the 4 directions holds a rotten orange
                            starting -= 1
                            rotten.add((r, c))
                            # add the cell to rotten set so that we can update it after the iteration

            if starting == fresh:
                # if no oranges turned rotten, that means the number of fresh oranges will never
                # reach 0, and therefore we set time to -1 and return it
                time = -1
                break
            
            fresh = starting
            for row, col in rotten:
                # update oranges that are now rotten
                grid[row][col] = 2
            
            time += 1
            # update time if oranges became rotten

        return time
                