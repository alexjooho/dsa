"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # recursive dfs for each node
        # keep a seen hashmap to avoid repeats of the same node
        # key of node's value and value of the actual node
        # for each original node and its value, create a new node if it has not already been made
        # and then recursively create and append all its neighbors

        # base case: if node has already been seen, return that node
        # edge case: Node is None -> then return None
        # edge case: Original node has no neighbors -> recursive function handles it since it will not add any neighbors
        
        # O(n) time complexity (n = e + v) and O(n) space complexity for hashmap
        # trick is to use a hashmap with keys of the value, and values of the actual node
        # if a node has already been added to the seen hashmap, simply return that node instead of creating new ones

        if not node:
            return

        seen = {}

        def dfs(original):
            val = original.val
            if val in seen:
                # base case for if this node has already been made
                return seen[val]
                # returning this works since it is the same object and will get updated if it keeps getting updated

            cur = Node(val)
            seen[val] = cur

            for neighbor in original.neighbors:
                cur.neighbors.append(dfs(neighbor))

            return cur

        return dfs(node)
    

# neetcode solution:
# same idea as mine with recursive dfs but instead of using values as keys, it uses the actual original node
# both solutions are good!

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None