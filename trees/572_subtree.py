# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        # Traverse through main tree using dfs until a node is found that matches the sub tree's root node
        # If a common node is not found, return false
        # If a common node is found, use recursive helper function to check if they are same tree
        # Continue if subtree not found

        # NOTE: If subRoot is Null, maybe it should always be counted as a subTree

        # if not root or not subRoot:
        #     if root == subRoot:
        #         return True
        #     else: return False
        
        if not subRoot:
            return True
        if not root:
            return False

        main_stack = [root]

        while main_stack:
            current = main_stack.pop()

            if current.val == subRoot.val:
                if self.isSameTree(current, subRoot):
                    return True
            
            if current.left:
                main_stack.append(current.left)
            if current.right:
                main_stack.append(current.right)

        return False


    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if root.val != subRoot.val:
        #     return False
        # this doesn't work because a "None" can't have a .val

        # if root.val == None and subRoot.val == None:
        #     return True
        # this doesn't work because a "None" can't have a .val -> instead you should do this:

        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return self.isSameTree(root.left, subRoot.left) and self.isSameTree(root.right, subRoot.right)
        else:
            return False
            
    # Neetcode recursive solution (using same self.isSameTree function):
    # This solution basically just checks each node with the sameTree function, while the
    # iterative solution just checks nodes if they have the same value
    
    # I think my solution is better (iterative one but it is technically same O)
    
    # class Solution:
    # def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    #     if not t:
    #         return True
    #     if not s:
    #         return False

    #     if self.sameTree(s, t):
    #         return True
    #     return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)