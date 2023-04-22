"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # recursive solution
        # for each node from the original list, create a copy node
        # do the same for the next node and the random node for each node
        # keep a seen hashmap with the original node as the key and the new copy node
            # as the value
        # the original node will not be mutated, so it can be used as a key
        
        # O(n) time complexity and O(n) space complexity

        seen = {}

        def dfs(original):
            if not original:
                # if the node is actually a null value, return None
                # also takes care of edge case where head is None
                return None

            if original in seen:
                # if the node has already been done, simply return it
                return seen[original]
            
            new_node = Node(original.val)
            seen[original] = new_node
            # add original node as key to seen hashmap and the new node as the value
            # so that we don't repeat it

            new_node.next = dfs(original.next)
            new_node.random = dfs(original.random)

            return new_node
            # have to return the new_node so that it gets connected to previous node

        new_head = dfs(head)

        return new_head
    
# neetcode iterative solution:
# instead of doing a recursive function, he simply does 2 passes through the original linked list
# first pass will create all the new nodes, and store them in a dictionary
# with the key being the original node, and the value being the new node

# second pass will connect all the next and random nodes
# O(n) time and space complexity

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Node") -> "Node":
        oldToCopy = {None: None}
        # have to put None: None so that if a next node is None, then it will also return None

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]
        # this takes care of the edge case where the head is None because it will also stil return None