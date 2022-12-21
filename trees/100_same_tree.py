# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Make a stack for both binary trees
        # Pop node and add children while both stacks are not none
        # Keep checking if the popped nodes are the same
        # Once a stack is empty, compare stacks to make sure both are empty

        # MAKE SURE TO USE .val because tree nodes will not == each other
        # ran into an error because if there wasn't a valid child for one node
        # but there was one for the other, it would still be true if
        # the next node (right) would be the same as the other tree's left

        if not p or not q:
            if p == q:
                return True
            else:
                return False

        if p.val != q.val:
            return False

        p_stack = [p]
        q_stack = [q]

        while p_stack and q_stack:
            p_node = p_stack.pop()
            q_node = q_stack.pop()

            # if p_node.left:
            #     p_stack.append(p_node.left)
            # if p_node.right:
            #     p_stack.append(p_node.right)

            # if q_node.left:
            #     q_stack.append(q_node.left)
            # if q_node.right:
            #     q_stack.append(q_node.right)

            # this caused an error because if test case 2

            if p_node.left and q_node.left:
                if p_node.left.val == q_node.left.val:
                    p_stack.append(p_node.left)
                    q_stack.append(q_node.left)
                else:
                    return False
            elif p_node.left != q_node.left:
                return False

            if p_node.right and q_node.right:
                if p_node.right.val == q_node.right.val:
                    p_stack.append(p_node.right)
                    q_stack.append(q_node.right)
                else:
                    return False
            elif p_node.right != q_node.right:
                return False

        if p_stack == q_stack:
            return True

        return False