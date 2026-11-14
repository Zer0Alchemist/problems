# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lst = []

        for n in lists:
            while n:
                lst.append(n.val)
                n = n.next

        lst.sort()
        nodes = ListNode()
        curr = nodes

        for n in lst:
            curr.next = ListNode(n)
            curr = curr.next
    
        return nodes.next
        