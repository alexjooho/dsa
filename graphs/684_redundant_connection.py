class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find to put each node under a parent/leader and return
        # the edge that contains two nodes with the same union
        # use union find since we are given edges and want to find a cycle
        # looking for edge that causes a redundant connection that is not needed to get to parent node

        # simply doing dfs won't work since we might be able to find a cycle, but we have to make an
        # adjacency list and have to return the exact edge that caused the cycle
            # which would result in a O(n^2) solution

        # time complexity: O(e * alpha(n)) => O(e)
        # since we used both ranking and path compression
        # alpha(n) is ackermann n and that becomes close to a constant

        ranks = collections.defaultdict(int)
        # we want the base rank for each parent to be 0
        # keep track of ranks so we add each union to the bigger rank

        parents = {}

        def find(node):
            # helper function to find parent
            if node not in parents:
                # if a parent hasn't been made for this node, set the parent to itself
                parents[node] = node

            if parents[node] == node:
                # base case so that if the parent of the node is itself, it will return itself
                return node

            parents[node] = find(parents[node])
            # recursive call to do path compression
            return parents[node]

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # find the parents

            if p1 == p2:
                # if the parents are the same, that means there is a cycle
                return True

            r1, r2 = ranks[p1], ranks[p2]
            # find their parents' rankings

            if r2 > r1:
                # if the rank of parent 2 is > parent 1
                # then update the parent of p1 to be p2 instead of itself
                # and then update the rank
                parents[p1] = p2
                ranks[p2] += 1
                # NOTE: have to increase rank by rank of other parent since we are adding all of its
                # children nodes
                # previously, I just did rank += 1 which is wrong!

            else:
                # opposite of above
                parents[p2] = p1
                ranks[p1] += 1

        for n1, n2 in edges:
            # for each edge, union the two nodes
            # and if there is a cycle, set result to the 
            if union(n1, n2):
                return [n1, n2]
                # we can return the first cycle edge since that will be the one last seen in the list
                # since there is only one additional edge
                
# neetcode solution:
# same solution but with slightly different styling by using arrays instead of hashmaps for ranks/parents
# instead of using a hashmap for the parents and rankings, he simply used arrays
# he does this since we know that there is one extra edge, and the number of nodes goes in order
# he adds an extra index to account for the 0th index not being used

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                # this path compression only compresses by one level of depth each time
                # mine is better since it compresses all the way to the top parent by using recursion
                par[p] = par[par[p]]
                p = par[p]
            return p

        # return False if already unioned
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
