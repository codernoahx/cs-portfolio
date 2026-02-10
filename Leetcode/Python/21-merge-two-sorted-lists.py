from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # dummy node to return list head and node to traverse the linked list
        node = dummy = ListNode()
        # Iterate until one of the list pointer becomes None
        while list1 and list2:
            # When we begin, the dummy node pointer points to None, and in the first iteration we make it point to
            # list1 or list2 head's node. If either the if or the else statement executes, then the
            # node will point to the list 1 or list 2 current node (head if it it's first iteration
            # or in case no element from the other list was inserted and list pointer is still pointing to head).
            # And we also update the list pointer to point to the next node in the list.
            # if list1 val is smaller than list 2 val
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            # Else if list 2 val is smaller
            else:
                node.next = list2
                list2 = list2.next
            # Doesn't matter which statement executes we assign the node pointer to point to the node it is pointing towards
            # Updating the node pointer, so that we can change which node will the next node point too based on the conditionals
            node = node.next
        # if there're any elements left in list 1 or list 2, make the node point to the rest of the list as it's already sorted
        # If anyone of the value is None/False/Empty, only the True/Non-empty value will be assigned. If both aren't
        # False/None/Empty, then the first value in the comparison from left to right will be assigned (list1).
        node.next = list1 or list2

        # return the node that dummy is pointing too
        return dummy.next
