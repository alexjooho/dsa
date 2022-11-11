# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # keep a current next variable to keep track of which node is next
        # make each node's next node be the one before it
        # stop when it reaches a node with no next node

        curr_before = None
        curr_node = head

        while curr_node:
            next_node = curr_node.next
            curr_node.next = curr_before
            curr_before = curr_node
            curr_node = next_node

        return curr_before

# there is also a recursive solution (from neetcode):

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         # recursive: T O(n), M O(n)

#         if not head:
#             return None

#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newHead

# this solution basically just keeps track of the newHead to make sure that
# it returns the new head (which was previously at the end)
# this solution also keep setting the next of each head it's currently at
# to be None so that the previous head will end up with a next of None

# THE MAIN IMPORTANT LINE IS THE head.next.next = head
# and the fact that this happens after the recursion