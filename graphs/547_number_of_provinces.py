class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # union find problem (can also do dfs)
        # for every index, if nodes are connected (== 1) then union them
        # after unioning every node, update the root parents for every node by doing find for every node
        # not all nodes may be updated before this since they might not have been revisited after their parent got a new parent
        # return the length of the set of the parent array since it will get rid of all duplicate parents and give us number of unions

        n = len(isConnected)
        
        parents = [i for i in range(n)]
        rank = [1] * n

        def find(n):
            if parents[n] == n:
                return n
            
            parents[n] = find(parents[n])
            return parents[n]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return

            if rank[p2] > rank[p1]:
                parents[p1] = p2
                rank[p2] += rank[p1]

            else:
                parents[p2] = p1
                rank[p1] += rank[p1]

        for i, row in enumerate(isConnected):
            for j, col in enumerate(row):
                if col == 1 and i != j:
                    # if they are connected and i and j are not same node
                    union(i, j)

        for i in range(n):
            find(i)
            # updates root parents for every node

        return len(set(parents))