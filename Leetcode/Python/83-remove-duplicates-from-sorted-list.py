from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        # while the cur pointer doesn't become None
        while cur:
            # While the cur.next isn't None and the cur next node value is same as cur node value
            while cur.next and cur.next.val == cur.val:
                # Change cur next pointer to point to the node which cur next node pointer points too.
                cur.next = cur.next.next
            # Update the cur pointer, so that we can look for more duplicates from where the cur next node value isn't duplicate or
            # it became None
            cur = cur.next
        return head


def main():
    val = 0
    head = node = ListNode(val)
    for i in range(10):
        if i % 2 == 0:
            val += 1
        node.next = ListNode(val)
        node = node.next
    node = head
    print("Before:", end=" ")
    while node:
        print(node.val, end=" ")
        node = node.next

    Solution().deleteDuplicates(head)
    node = head
    print("\nAfter: ", end=" ")
    while node:
        print(node.val, end=" ")
        node = node.next
    print()



if __name__ == "__main__":
    main()
