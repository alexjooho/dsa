from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        # graph multi-source BFS problem
        # we can't simply do a dfs for each empty room since it would have to go through entire grid
        # for each cell, which would be O((m*n)^2) time complexity
        # doing a BFS from each empty room would require repeats of work since we can't confirm distance
        # of cells it passed through. So it would still be O((m*n)^2) time complexity

        # instead, we start off from each gate and move outwards using BFS (queue)
            # MULTI-SOURCE BFS STARTING FROM ALL GATES
        # while the queue isn't empty keep popping from queue
            # note, don't have to do a for loop to pop only the amount currently
            # in queue, since the distance will update automatically by adding 1 to previous cell
            # neetcode solution DOES use the for loop though and simply increments distance
            # through a variable, so either method is viable
        # we check each neighboring direction, and if the direction has an empty room,
        # we update its value with its distance and add it to the queue
            # distance is current distance + 1
            
        # time complexity: O(m * n)

        queue = collections.deque()
        empty = 2147483647

        rows, cols = len(rooms), len(rooms[0])

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            r, c = queue.popleft()
            distance = rooms[r][c]

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r in range(rows)
                    and new_c in range(cols)
                    and rooms[new_r][new_c] == empty):
                    # if the neighboring cell is a valid cell and is an empty room
                    # then update its distance with the current cell's
                    # distance to the gate + 1 and add it to the queue
                    rooms[new_r][new_c] = distance + 1
                    queue.append((new_r, new_c))

                # if the neighbor is not valid, simply don't add it to the queue
                
# neetcode solution:
# worse than mine since it uses more memory for a visited set
# instead, my solution simply doesn't visit cells that it has already visited

# neetcode's solution does a for loop each time for the queue to only pop cells at the current distance
# slightly different from my solution since it uses a distance variable and increments it, while I
# simply added 1 to the room it was being traversed to from
# he also uses a helper function to check each directional neighbor

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = deque()

        def addRooms(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or rooms[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
