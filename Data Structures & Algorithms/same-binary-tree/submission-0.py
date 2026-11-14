# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        pqueue = deque([p])
        qqueue = deque([q])

        while pqueue and qqueue:
            pnode = pqueue.popleft()
            qnode = qqueue.popleft()

            if pnode is None and qnode is None:
                continue
            if pnode is None or qnode is None or pnode.val != qnode.val:
                return False

            pqueue.append(pnode.left)
            pqueue.append(pnode.right)
            qqueue.append(qnode.left)
            qqueue.append(qnode.right)
        
        return True