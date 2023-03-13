# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # use BFS to get every node in a level of the tree
        # do this using a deque (from collections import deque) and popping from left the number of times that
        # the current level's length is
        # start with an empty list, and for every level, add all the nodes into a list and append to the total list

        # O(n) time and memory complexity

        q = deque()
        node_values = []

        if root:
            # don't want to start a loop if root is null
            q.append(root)

        while q:
            curr_level = []
            for i in range(len(q)):
                curr = q.popleft()
                # have to do popleft() so that it pops from the front
                curr_level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            node_values.append(curr_level)
        
        return node_values