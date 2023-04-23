# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # basically think of every single node as a "root" with the diameter being
        # the maximum height of the left side + the maximum height of the right side
        # we recursively call each node, and for each node we calculate its height and diameter

        # the height of a "None" tree is 0
        # otherwise, we calculate the node's height with 1 + max(left, right)
        # we also use left + right to calculate the diameter at the current tree

        # we don't need a hashmap/set to keep track of visited nodes since we are going bottom up
        # and will not repeat nodes!
        
        # time complexity: O(n), space complexity: O(1)

        res = [0]
        # global result variable
        # we use an array instead of a typical variable/number since it is easy to use globally

        def dfs(root):
            if not root:
                # if the node is "None", then its height is -1 since it wouldn't actually connect
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            res[0] = max(res[0], left + right)
            # diameter is left + right heights

            return 1 + max(left, right)
            # we return the max height of this node so that the node that called this node
            # will be able to calculate its own diameter

        dfs(root)
        return res[0]
    
# above is neetcode's solution except I didn't do 2 + left + right for diameter
# I simply did left + right, and for nodes that are "None", I set them to 0 instead of -1

# previous solution that worked but is inefficient since I have to loop twice:

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # basically think of every single node as a "root" with the diameter being
        # the maximum length of the left side + the maximum length of the right side
        # to get the maximum length, we basically need to do a dfs of each node to get its height
        # so that when we are looking for each node's diameter, we can just add the max depth of the left node
        # and the right node

        # keep hashmap for max depths for each node

        # time complexity: O(2n) == O(n)
            # we are visiting each node twice. once to find each node's max depth and once for diameter
        # space complexity: O(n)

        res = float('-inf')

        seen_depth = {None: 0}

        def max_depth(node):
            # recursive function for finding max depth of every node
            if not node:
                return 0
            if node in seen_depth:
                return seen_depth[node]
            
            cur_max = 1 + max(max_depth(node.left), max_depth(node.right))
            seen_depth[node] = cur_max

            return cur_max

        max_depth(root)

        def max_diameter(node):
            if not node:
                return
            
            diameter = seen_depth[node.left] + seen_depth[node.right]
            nonlocal res
            res = max(res, diameter)

            max_diameter(node.left)
            max_diameter(node.right)

        max_diameter(root)

        return res