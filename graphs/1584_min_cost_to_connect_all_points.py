class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # O(n^2 + (E + V)logV) = O(n^2) Time complexity
        # Neetcode put n^2 * logv since max edges is nodes^2 but that portion can 
        # be simplified to O((E + V)logV) which is overpowered by n^2
        # O(n^2) is from creating adjacency list
        # Prim's algorithm (very similar to dijkstra's algorithm)

        # create edges list (adjacency list)
        # minheap (frontier - every possible node that could be added - like bfs) to keep track of closest node
            # every addition to minheap needs the cost and the node to be connected
            # since question doesn't ask for path and only wants total distance, we don't even need to know prev node
        # hashset for visited nodes to avoid cycles
        # to create all nodes connect without a cycle, will need n-1 edges

        n = len(points)

        adj = { i: [] for i in range(n)}
        # even though the points aren't given a node value, for each one were just giving a number
        # each value list will be a list of [cost, node] arrays inside the list

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
                # have to append to both nodes since it is undirected
                # this is how we create the adjacency list

        # Prim's algorithm portion:
        res = 0
        visit = set()
        min_heap = [[0, 0]] # [cost, point]... the heap will sort based on first value

        while len(visit) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visit:
                # have to check if the node has already been checked
                continue

            res += cost
            visit.add(i)

            for neighbor_cost, neighbor in adj[i]:
                if neighbor not in visit:
                    heapq.heappush(min_heap, [neighbor_cost, neighbor])

        return res