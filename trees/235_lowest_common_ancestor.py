# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Neetcode solution:
# Better because it takes advantage of the fact that its a BINARY SEARCH TREE!!!

class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        # O(log n) time complexity since it doesn't look at all nodes, and always splits in half
        # O(1) memory complexity since it doesn't require any data structures!
        # check if current node is < both values or > both values
        # if node < both values, go to right side, if node > both values, go to left side
        # else, return node since that is either in between both nodes or is one of them and has
        # the other as a desendant!
        
        cur = root
        while cur:
            # cur will never be None but this is just a way to keep traversing through tree
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur

# My solution:
# my solution is bad because it is just seeing the binary search tree as a regular tree
# and going through all its values
# instead I should've taken advantage of the fact that its a bst and traversed it accordingly!

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # do a DFS until both p and q are found
        # keep track of all nodes seen in an array so that the previous nodes can be compared
        # turn one of the arrays of nodes into a set and iterate backwards in the other one until a node is found
        # in the set
        # O(n) to dfs tree, another O(n) to turn a list into set, and final O(n) to find LCA
        # so it is O(3n) time complexity
        # ~ O(5n) memory complexity (~2n for tree since there are copies, n for p, n for q, n for set)

        # allows a node to be a descendant of itself

        p_list = []
        q_list = []

        node_stack = [[root, []]]

        while not p_list or not q_list:
            curr = node_stack.pop()

            if curr[0]:
                # curr[1].append(curr[0].val)
                # NOTE: HAVE TO PUT ACTUAL NODE IN HERE, NOT VAL
                curr[1].append(curr[0])
                if curr[0] == p:
                    # can compare actual node instead of their specific values since p and q are actually the same node
                    # from this tree
                    p_list = curr[1].copy()
                    # have to do .copy since if its the same array, it will have added values of future nodes
                elif curr[0] == q:
                    q_list = curr[1].copy()
                node_stack.append([curr[0].left, curr[1].copy()])
                # have to do .copy since if its the same array, it will have added values of future nodes
                # just need .copy for left side since right side is going down dfs same path
                node_stack.append([curr[0].right, curr[1]])

        q_set = set(q_list)

        for i in range(len(p_list) - 1, -1, -1):
            if p_list[i] in q_set:
                return p_list[i]