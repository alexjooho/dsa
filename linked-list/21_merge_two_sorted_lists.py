# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

# previous solution that didn't work:
# it didn't work because list1.val would throw an attribute error in edge cases where there was an empty list given
# above solution is better anyways because it uses less extra variables (just reassigns list1 and list2)
# IT IS VERY IMPORTANT TO USE A DUMMY NODE SO THAT YOU CAN EASILY DEAL WITH EDGE CASES LIKE AN EMPTY LIST!!!

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         # keep a temporary current node for each list
#         # keep a temporary current node for the merged list
#         # create a variable for the head, which is the lesser of the two heads
#         # keep comparing the current nodes of both lists and adding that to the next node of the current merged list node
#         # stop once one of the lists reaches a node without a next node, and then add the rest of the list with a next node onto 
#         # the current merged list node

#         head, curr1, curr2 = None, list1, list2
#         if list1.val <= list2.val:
#             head = list1
#             curr1 = list1.next
#         else:
#             head = list2
#             curr2 = list2.next
        
#         curr_merged = head

#         while curr1 and curr2:
#             if curr1.val <= curr2.val:
#                 curr_merged.next = curr1
#                 curr_merged = curr1
#                 curr1 = curr1.next
#             else:
#                 curr_merged.next = curr2
#                 curr_merged = curr2
#                 curr2 = curr2.next
        
#         if not curr1:
#             curr_merged.next = curr2
#         else:
#             curr_merged.next = curr1
        
#         return head