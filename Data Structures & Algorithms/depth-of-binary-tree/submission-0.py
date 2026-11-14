# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxlen(node):
            if not node:
                return 0
            
            return 1 + max(maxlen(node.left), maxlen(node.right))
        
        return maxlen(root)
