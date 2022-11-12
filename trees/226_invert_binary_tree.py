# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # create a stack of descendant tree nodes
        # pop a tree node, and for every tree node: 
        # switch the left and right descendant if they are present, and then add them to the stack
        # keep doing this until the stack is empty, and then return the root node
        
        # make sure that the root node is not a "None"

        if not root:
            return root
        
        node_stack = [root]

        while node_stack:
            current = node_stack.pop()
            if current.left:
                node_stack.append(current.left)
            if current.right:
                node_stack.append(current.right)
            
            current.left, current.right = current.right, current.left
        
        return root
        
# this is the iterative solution that I used, but there is a recursive solution that neetcode showed
# either way, this problem always should use DFS because it needs to invert all the descendants
# it technically doesn't matter whether an iterative or recursive solution is used, because both
# time and space complexity are the same

# class Solution:
#     def invertTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return None

#         # swap the children
#         tmp = root.left
#         root.left = root.right
#         root.right = tmp

#         self.invertTree(root.left)
#         self.invertTree(root.right)
#         return root

# cool, shorter solution:

    # if root:
	#     root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
	#     return root
    
# this works because the first recursive solution basically does an extra step of calling the function
# after left and right are switched even though each recursive function returns the node anyways
# so instead of doing the extra step, it just calls the function while switching