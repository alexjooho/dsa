# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse bst in order recursively to create a list of values in ascending order
        # NOTE: in order traversal is "traverse left, myself, traverse right"
        # then return the k - 1 index of the list to get the kth smallest value
        # O(n) time and space complexity

        res = []

        def in_order_traversal(root):
            if root:
                in_order_traversal(root.left)
                res.append(root.val)
                in_order_traversal(root.right)
            
        in_order_traversal(root)

        return res[k-1]
    
# neetcode iterative solution using stack O(n) time and O(1) space complexity:
# note that this solution is less code because it just checks if current is valid
# and adds it to stack if it is
# it doesn't keep curr as the popped value, instead it sets it to the right value
# so that it doesn't redo the loop

# stack starts off empty because nodes are added to stack as they are traversed
# also because curr is a variable that is kept track of outside of while loop as well

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right
            
# my iterative solution:
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # traverse bst in order iteratively to create a list of values in ascending order
        # O(n) time and O(1) space complexity
        # keep track of numbers popped until it equals k, then we will return that value
        # keep a stack and keep adding onto it as long as the current node has a left value.. keep updating current node
        # after there are no more left values, pop the last value of the stack
        # if it has a right node, add it to the stack and make that the current node
        # if it doesn't, keep popping nodes and updating current node until one has a right node, and then make that the current
        # node and add it to the stack
        
        # for each node it will check if there is a left node, otherwise the last node will be popped and be the current node

        popped = 0
        
        curr = root
        node_stack = [root]

        while node_stack:
            if curr.left:
                node_stack.append(curr.left)
                curr = curr.left
            else:
                popped += 1
                curr = node_stack.pop()
                if popped == k:
                    return curr.val
                while not curr.right:
                    popped += 1
                    curr = node_stack.pop()
                    if popped == k:
                        return curr.val
                node_stack.append(curr.right)
                curr = curr.right