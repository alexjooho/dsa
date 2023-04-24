# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # recursive dfs
        # keep track of the largest visited node for each recursive call
        # for each node, return 0/1 + recursive left + recursive right
            # this will be the total good nodes at the given node
        
        # if current node is >= largest visited node in path, add 1 to count and
            # call left and right nodes with new largest value
        # else, just call left and right nodes with same largest value and don't add to count
            # recursively call left and right and return 1/0 + the left and right values
            # since that will let us get the total at the root node (going bottom up)

        def dfs(node, largest):
            if not node:
                return 0

            if node.val >= largest:
                return 1 + dfs(node.left, node.val) + dfs(node.right, node.val)

            else:
                return dfs(node.left, largest) + dfs(node.right, largest)

        return dfs(root, float('-inf'))
        # can just do root.val for the second value since that is the current largest technically
    
# neetcode solution:
# same concept of going bottom up recursively and tallying the good nodes
# he calculates if node.val > max first and also updates max before calling left and right
# he adds the left and right to the result and returns result

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            if not node:
                return 0

            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
            return res

        return dfs(root, root.val)