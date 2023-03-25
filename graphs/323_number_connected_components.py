class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # use union find to optimize time complexity to O(e * α(n)) with path compression and ranking
        # make a parent array and rank array
        # make a find function and union function
        # find function will look for the root parent of the node and also implement path compression so that it doesn't re-check same nodes
        # union function will call find function for both nodes in an edge and put the smaller union
        # into the bigger union and return 1 (return 0 if both have same parents since this means they're in same union cycle)
        # for every edge, the number of connected components will decrease by 1 if a union was made
        
        par = [i for i in range(n)]
        # parent array
        rank = [1] * n
        # rank array so that smaller union will join bigger one
        
        def find(n1):
            if n1 == par[n1]:
                # if the node is its own parent, return node
                return n1
            
            par[n1] = find[par[n1]]
            # path compression to compress route to parent so it doesn't have to re-check it
            return par[n1]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                # check rank and update rank
                par[p1] = p2
                rank[p2] += rank[p1]
            
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
                
            return 1
        
        unions = n
        
        for n1, n2 in edges:
            unions -= union(n1, n2)
            # unions starts at number of nodes, and every time a union is made/added to, subtract by 1
        
        return unions
    
# neetcode solution 2 using a class for union find and hashmap instead of array:
# this solution basically doesn't use the ranking but uses path compression
# this saves space but uses up more time when doing find
# instead of subtracting 1 from total unions each time a union is made/added to, it simply
# makes a set of all the parents (since duplicate parents can't be added to set) and checks the length of it
# this works because it calls find parent on every single node again to make sure it is fully updated
# otherwise, some nodes might not have parents that are fully updated to the root parent and instead
# just the parent above it
# NOTE: this solution isn't as time efficient and is probably harder to come up with in an interview

class UnionFind:
    def __init__(self):
        self.f = {}

    def findParent(self, x):
        y = self.f.get(x, x)
        if x != y:
            y = self.f[x] = self.findParent(y)
        return y

    def union(self, x, y):
        self.f[self.findParent(x)] = self.findParent(y)


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind()
        for a, b in edges:
            dsu.union(a, b)
        return len(set(dsu.findParent(x) for x in range(n)))