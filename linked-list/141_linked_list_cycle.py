# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # create a set for visited nodes
        # traverse the linked list and add nodes as they are visited
        # if the list reaches the end without seeing a duplicate, return False
        # if there is a duplicate, return True

        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
            else:
                seen.add(curr)
            curr = curr.next
        
        return False
        
# neetcode solution: (tortoise and hare)

# class Solution:
#     def hasCycle(self, head: ListNode) -> bool:
#         slow, fast = head, head

#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 return True
#         return False

# this solution is better because it has same time complexity O(n) but memory is only O(1)