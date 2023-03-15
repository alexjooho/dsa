# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# neetcode solution with O(n^2) time complexity and O(n) space complexity
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # first value or pre order array will be the root node!
        # everything to left of a number in an in order array will be in the left subtree of that node, and
        # everything to right of a number will be in the right subtree of that node

        # however many nodes are still in the left side of the in order array are the number of nodes
        # to the right of the node in the pre order array that are in the left subtree
        # same concept for right side
        # NOTE: THIS PROBLEM IS REALLY GOOD FOR LEARNING TO RECOGNIZING PATTERNS

        # keep updating preorder and inorder arrays 

        # O(n^2) time complexity and O(n^2) memory complexity
        # O(n^2) since for every preorder[0], have to iterate through inorder to find its index

        if not preorder or not inorder:
            # can just do if not inorder since inorder can be depleted before the preorder list
            # e.g. if there are no nodes in left subtree, the preorder will still have values
            return None
        
        root = TreeNode(preorder[0])
        # this is building the root node into a tree node

        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        # note, when slicing an array, python lets you put indexes outside of its index range
        # so even if the array has no index at spot 1, this code will still run
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

# could make a secondary function that does the actual recursion and add parameters of index numbers
# and a hash map of the inorder array's values and index numbers to create a 
# O(n) time and O(n) space complexity solution

# iterative solution with O(n^2) time (but usually O(n)) and O(2n) space:
# building two hashmaps takes O(2N) and for loop takes O(n^2) time complexity in worst case
# two hash maps cost O(2n) space complexity
# NOTE: THIS SOLUTION IS PROBABLY NOT WORTH DOING SINCE ITS MUCH MORE CODE AND HARDER THAN RECURSIVE


# approach: start with root node and for each subsequent node in the preorder traversal,
# use inorder traversal to test if it is a left node or a right node. Then use inorder
# traversal to find the parent node to attach the node to

# basically, for each preorder value (other than root), use the node in the index of the node - 1 (call this next)
# if current node has a lower index than next, then it is a left child of the first node that has been seen
# as you are going to the right in the inorder list
# if current node has a higher index than next, then it is a right child of the first node that has been seen
# as you are going to the left in the inorder list
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        total = len(preorder)
        root = TreeNode(preorder[0])
        prev = root
        node = None
        seen = {preorder[0]: root}
        indexDict = {val:i for i, val in enumerate(inorder)}
        for i in range(1,total):
            node = TreeNode(preorder[i])
            endVal, nextval = preorder[i], preorder[i -1]
            iindex, nindex = indexDict[endVal], indexDict[nextval]
            if nindex > iindex:
                for g in range(iindex, total):
                    if inorder[g] in seen:
                        prev = seen[inorder[g]]
                        break
                prev.left = node
            if iindex > nindex:
                for g in range(iindex,-1,-1):

                    if inorder[g] in seen:
                        prev = seen[inorder[g]]
                        break
                prev.right = node
            seen[endVal] = node
        return root