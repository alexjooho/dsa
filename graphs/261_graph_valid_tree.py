from typing import (
    List,
)

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # O(N + E) time complexity and O(3n) space complexity

        # a graph is a valid tree basically if there are no cycles
        # DFS for each node to check that there is no cycle
        # keep a hash set for visited nodes so that they are not re-checked
        # keep a hash set for cycle so that if there is a repeated node, it is not a valid tree

        # since edges are undirected, make a dictionary that has key of node
        # and value being a set of nodes its connected to
        # whenever a node checks a connected node, remove that edge from both sets

        # edge case: a node is not connected to anything (this is not a valid tree since it's not connected to the tree)
        # edge case: 1 or 0 nodes
        
        # NOTE: ALL NODES MUST BE CONNECTED, SO WE COULD'VE SIMPLY DONE DFS ONCE AND CHECKED VISITED AND USED JUST ONE SET

        if n <= 1:
            return True
        
        visited = set()
        cycle = set()

        neighbors = {i : set() for i in range(n)}

        for n1, n2 in edges:
            neighbors[n1].add(n2)
            neighbors[n2].add(n1)

        def dfs(node):
            if node in visited:
                return True
            if node in cycle:
                return False

            cycle.add(node)

            for neighbor in neighbors[node]:
                neighbors[neighbor].remove(node)
                # need this line so that we don't go back to the same parent node (since edges are undirected)
                # could also use another variable in dfs function called prev to make sure we don't go back to prev node (default value = -1)
                if dfs(neighbor) == False:
                    return False
            
            cycle.remove(node)
            visited.add(node)

            return True
        
        for val in neighbors.values():
            # this is for the edge case where a node is not connected to the tree
            # instead of having to do this, neetcode's solution simply checks visited set's length to = n
            # this is possible since he doesn't start a dfs for every node in range(n), he simply does it from 0 once
            if not val:
                return False

        for node in range(n):
            if dfs(node) == False:
                return False

        return True
    

# neetcode solutions:

# Problem is free on Lintcode
class Solution:
    # create an adjacency list and a visited set
    # only need to do dfs on 0 since we know 0 will be present, and if this doesn't connect
    # to all the nodes, then it's not a tree
    
    # do dfs on 0, and make sure there are no cycles and that all nodes have been visited
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if not n:
            return True
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)
            for j in adj[i]:
                if j == prev:
                    continue
                if not dfs(j, i):
                    return False
            return True

        return dfs(0, -1) and n == len(visit)
    
    
    
    # alternative solution via DSU O(ElogV) time complexity and 
    # save some space as we don't recreate graph\tree into adjacency list prior dfs and loop over the edge list directly
    
    # union find solution where each node is made to be connected to a singular parent/root node
    # decrements n by 1 to make sure every node is connected and detects cycle if parent of two nodes in edge are the same!
    class Solution:
        """
        @param n: An integer
        @param edges: a list of undirected edges
        @return: true if it's a valid tree, or false
        """
    def __find(self, n: int) -> int:
        while n != self.parents.get(n, n):
            n = self.parents.get(n, n)
        return n

    def __connect(self, n: int, m: int) -> None:
        pn = self.__find(n)
        pm = self.__find(m)
        if pn == pm:
            return
        if self.heights.get(pn, 1) > self.heights.get(pm, 1):
            self.parents[pn] = pm
        else:
            self.parents[pm] = pn
            self.heights[pm] = self.heights.get(pn, 1) + 1
        self.components -= 1

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        # init here as not sure that ctor will be re-invoked in different tests
        self.parents = {}
        self.heights = {}
        self.components = n

        for e1, e2 in edges:
            if self.__find(e1) == self.__find(e2):  # 'redundant' edge
                # instead of doing this (since it also does find twice in connect)
                # you could simply check if every connect function call is truthy to make sure there is no cycle
                return False
            self.__connect(e1, e2)

        return self.components == 1  # forest contains one tree