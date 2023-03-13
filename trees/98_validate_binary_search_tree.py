# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # traverse through the list using DFS
        # for each node, keep track of what it needs to be greater than
        # and what it needs to be less than
        # for a node to the right, update new value it needs to be greater than
        # for a node to the left, update new value it needs to be less than
        # O(n) time complexity and O(n) space complexity
        # NOTE: remember that every child node to right side must be greater than the furthest ancestor and less than furthest
        # ancestory for left side
        # NOTE: THIS IS THE ITERATIVE DFS SOLUTION

        node_stack = [[root, float('-inf'), float('inf')]]
        # each item added to stack will be an array with 3 items:
        # the node, the value it has to be greater than, and the value it has to be less than

        while node_stack:
            curr = node_stack.pop()

            if curr[0].val <= curr[1] or curr[0].val >= curr[2]:
                # NOTE: HAVE TO DO <= AND >= SINCE A BINARY SEARCH TREE CAN NOT HAVE DUPLICATE VALUES
                return False
            if curr[0].left:
                node_stack.append([curr[0].left, curr[1], curr[0].val])
            if curr[0].right:
                node_stack.append([curr[0].right, curr[0].val, curr[2]])
        
        return True
    
# Recursive solution:

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # recursive solution
        # for each node, keep track of what it needs to be greater than and less than
        # call the recursive function each time
        # base case is if the node is None, then return true

        # O(n) time complexity and O(n) memory complexity since each node requires a function added onto call stack

        def valid(node, left, right):
            if not node:
                return True
            if node.val <= left or node.val >= right:
                # could also do: if not (node.val < right and node.val > left)
                return False
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float('-inf'), float('inf'))
    
# extra in order traversal solution (O(2n) time complexity)
# basically traverses left, then current node, then right recursively
# an in-order traversal of a binary search tree will create a list with values in ascending order!
# this is because every value to the left will be less than the value to the right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        self.inorder_traversal(root, res)
        return self.is_sorted(res)
    
    def inorder_traversal(self, root, res):
        if root:
            # if the node is null, it will not append it to the list
            self.inorder_traversal(root.left, res)
            res.append(root.val)
            self.inorder_traversal(root.right, res)
            
    def is_sorted(self, arr):
        if not arr:
            return False
        for i in range(1, len(arr)):
            if arr[i] <= arr[i-1]:
                return False
        return True