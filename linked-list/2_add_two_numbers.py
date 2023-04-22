# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# neetcode solution since my solution is too brute force:
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # add digits starting from the start (since this will be the one's place for both numbers)
        # create a node for the resulting sum
        # if the sum for that digits place is 10 or greater, we have to carry over the 1 to next digits place

        # edge case: different length linked lists -> keep adding until both are exhausted
        # edge case: both linked lists finished but there is a 1 to carry over -> remember this and add another node
        # to the sum linked list

        # time complexity: O(n + m)
        # space complexity: O(1) if we exclude the result linked list

        # NOTE: THIS IS JUST TRADITIONAL ADDITION!

        dummy = ListNode()
        # we use a dummy node to avoid edge cases of inserting into a linked list with None values
        # technically not necessary since problem says that the linked lists will not be empty
        # but it still saves code and makes writing code easier
        cur = dummy

        carry = 0
        # keep track of carry digit!
        while l1 or l2 or carry:
            # keep iterating until both lists finished
            # put "or carry" for edge case 2... if both lists finished but a carry needs to be added
            # the values will be 0 + 0 + 1 and we need to add that to new linked list
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            # for both of these, only get the val if the list still isn't finished

            val = v1 + v2 + carry
            # have to include the carry to new digit value
            carry = val // 10
            # clever way of checking if val >= 10 since this will always give us 0 or 1

            val = val % 10
            # clever way of only getting singles digit
            # if val is < 10, then it will just give us the number
            # if val is >= 10, then it will give us remainder after dividing by 10

            cur.next = ListNode(val)

            # update pointers:
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # traverse through each linked list and create an array of string digits
        # after traversing, reverse the array and then join the string and turn it into an integer
        # add the two numbers and then create the sum linked list in reverse order

        num_1, num_2 = [], []

        cur_1, cur_2 = l1, l2

        while cur_1:
            num_1.append(str(cur_1.val))
            cur_1 = cur_1.next

        while cur_2:
            num_2.append(str(cur_2.val))
            cur_2 = cur_2.next

        num_1.reverse()
        num_2.reverse()

        sum_lists = str((int(''.join(num_1)) + int(''.join(num_2))))

        dummy = ListNode()
        cur = dummy

        for i in range(len(sum_lists) - 1, -1, -1):
            cur.next = ListNode(int(sum_lists[i]))
            cur = cur.next

        return dummy.next