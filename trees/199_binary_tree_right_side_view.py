# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # breadth first search where we always add the right side first
        # check if the right and left nodes are not None
        # for every new level, we add the first node we see to the result array
        # this will sometimes be the left node if there was no right node
        # we always add right first, and then add left

        # use a deque to pop from the left side
        # time and space complexity: O(n)
        
        # you could technically do this with dfs by just going to right side first and 
        # appending to result every time you reach a new level for the first time
        # but bfs is probably a better solution

        from collections import deque

        queue = deque()
        # edge case of empty tree
        if root:
            queue.append(root)
        res = []

        while queue:
            for i in range(len(queue)):
                # we traverse this whole level
                node = queue.popleft()
                if i == 0:
                    # for the first value we see in this level (which will be the right-most node)
                    res.append(node.val)
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
        
        return res
    
# neetcode solution:
# basically same solution as mine
# except he appends the left side first and then the right side for each node
# and appends the last node of the level (which is the right most node) into the result
    # he keeps updating rightside so that at the end of the for i in range loop
    # the rightside will be the last node
# same concept, just different order since I appended the right side first
# he also appends node.left and node.right even if they are None values
# and he checks for that in the loop

# code is technically a little faster than mine since it doesn't have a lot of "if" statements
# and it doesn't have to check what i == for every single i. it just appends last valid node

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
