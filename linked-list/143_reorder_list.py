# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # O(2n) solution with O(n) memory
        # make a list and use two pointers to reorder the list
        # while loop with r - l > 1 since both left and right pointer will move one each time
        # so they get 2 spaces closer each time
        # final if else statement to take into account odd or even number of elements in list
        # make sure that the last element's next value is None

        curr = head

        nodes = []

        while curr:
            nodes.append(curr)
            curr = curr.next
        
        l, r = 0, len(nodes) - 1

        while r - l > 1:
            nodes[l].next = nodes[r]
            nodes[r].next = nodes[l + 1]
            l += 1
            r -= 1

        if r > l:
            nodes[l].next = nodes[r]
            nodes[r].next = None

        else:
            nodes[l].next = None
            
# Neetcode solution with O(n) memory:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # O(2n) solution with O(1) memory
        # use a slow and fast pointer to find middle point of list
        # node after the middle point will represent the latter half of list that needs to be reversed
        # reverse second half of list (while keeping track of last value)
        # set end of first half's next value to none

        slow, fast = head, head.next

        while fast and fast.next:
            # have to do fast and fast.next since we are moving it 2 at a time
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        # this is the first node in the second half of the list
        slow.next = prev = None
        # setting next of last value in first half of list to None so that it is no longer connected
        # also setting previous value to None so the first node in second half will have no value after it
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            # temp is the next value that we need since it'll be changed
            # second.next will be reversed to connect to the previous value
            # the new previous value is the current second
            # and now second will be the next value in the list (aka temp)

        first, second = head, prev
        # final previous value will be the new first node in second half (originally the last node of whole list)

        while second:
            # only need to do while second instead of first as well since second half's length will
            # be = to first half or first half - 1
            first_temp, second_temp = first.next, second.next
            # have to keep track of the next node for first and second half since they both will get changed
            first.next = second
            second.next = first_temp
            # if odd size list, second.next at end will be the last value of first half
            # if even size list, second.next will be None since the last value in first half will have .next of None
            first = first_temp
            second = second_temp