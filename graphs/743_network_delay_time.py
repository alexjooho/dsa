class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra's algorithm
        # O((E + V) log V) -> O(E log V) assuming that E > V

        # set for visited nodes
        # hashmap for node's edges with their respective weights/times
        # heap for finding minimum cumulative distance node

        # start at source node
        # add the node to min heap with its distance 
        # (if we needed final distance for every node, would update distance in a separate hashmap)
        # pop from heap and if the node hasn't been visited yet, do the same for this node

        # keep track of time while iterating to know what the final time will be
        # the last minHeap call of a node that hasn't been visited will have the minimum total time since it is limiting factor

        # in this question, we don't need to have a hashmap for each node's final calculated distance
        # since all we care about is the total time, but other questions might require it
        # make sure that every node has been visited!

        edges = collections.defaultdict(list)
        # using defaultdict with a list parameter so that we can append 
        # to a key that is empty and it will always be an empty list to start

        for u, v, w in times:
            # updating hashmap with every node's edges and their weights
            edges[u].append((v, w))

        minHeap = [(0, k)]
        # initializing minheap with starting weight 0 and the first node being k
        # NOTE: heap sorts the same way .sort sorts, it will look at the first element of tuple, list, etc
        # and check next value if first element is a tie

        visit = set()
        t = 0

        while minHeap and len(visit) < n:
            # the len(visit) < n is so that we don't keep iterating after already seeing all the nodes
            # not necessary, but it optimizes the solution to get rid of excess work
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue

            visit.add(n1)
            t = w1
            # keep updating weight

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    # this is just a slight optimization to not redo nodes
                    heapq.heappush(minHeap, (w1 + w2, n2))
                    # the distance for the node added will be the current distance + the distance to that node

        return t if len(visit) == n else -1
        # have to check that every node was visited