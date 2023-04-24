# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # for each node, recursively call the left and right nodes and get their max heights
        # make sure that left and right are not more than 1 apart in terms of height
        # return max height of current node by doing 1 + max(left, right)

        # since we can't check if a result is False while comparing it to a 0
        # we can't let the base case be to return 0
        # instead we will check if node.left and node.right are None and not call the function
        # if that's the case

        # edge case of empty tree
        if not root:
            return True

        def max_height(node):
            left, right = 0, 0
            if node.left:
                left = max_height(node.left)
                if not left:
                    return False
            if node.right:
                right = max_height(node.right)
                if not right:
                    return False

            if abs(right - left) > 1:
                return False

            return 1 + max(left, right)

        return True if max_height(root) else False
        # if the tree never has an invalid subtree, then the recursive call of the root
        # will return a number, which is Truthy
    
# neetcode solution:
# instead of having to do recursive calls in a roundabout way by checking if node.left and node.right
# aren't "None", he keeps the typical base case, but for every function he returns the height
# and whether its valid or not by doing [valid, height]
# this way, he can simply check the validity through the array and also the height

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                # a "None" tree is always valid by itself
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # if left or right are false or if the tree itself is not valid, then balanced = False
            return [balanced, 1 + max(left[1], right[1])]
            # he also returns the height in the second position of the array

        return dfs(root)[0]
