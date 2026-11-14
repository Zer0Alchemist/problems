# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []

        while head:
            lst.append(head.val)
            head = head.next

        lst = lst[::-1]
        node = ListNode()
        curr = node
        for n in lst:
            curr.next = ListNode(n)
            curr = curr.next

        return node.next
        