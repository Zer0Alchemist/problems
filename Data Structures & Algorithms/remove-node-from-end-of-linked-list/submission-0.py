# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []

        while head:
            lst.append(head.val)
            head = head.next


        nodes = ListNode()
        curr = nodes

        for j in range(len(lst)):
            if j == len(lst) - n:
                continue
            curr.next = ListNode(lst[j])
            curr = curr.next

        return nodes.next
        