# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # go through linked list and see the length
        # then subtract n from length
        # once it reaches the node before the one that needs to be removed, connect it to the value after it
        # edge case of an empty list or a list with its head taken out requires a dummy node
        # O(2n) time complexity O(1) memory

        dummy = ListNode()
        dummy.next = head

        # dummy node in case head is removed

        curr = head
        counter = 0

        while curr:
            counter += 1
            curr = curr.next

        n_delete = counter - n
        counter = 0
        curr = dummy

        while counter < n_delete:
            curr = curr.next
            counter += 1

        curr.next = curr.next.next

        return dummy.next
    
# Neetcode solution using two pointers:

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            # since left is at dummy, right will actually be n + 1 spaces away from the left node at end of loop
            # this loop is just to create a space between the two pointers
            right = right.next
            n -= 1

        while right:
            # this is to get to the end of the loop and to find the left node that is right before
            # the node we want to delete
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next