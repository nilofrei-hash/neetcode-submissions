# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        m = root 
        if m is None:
          return None 
        m.left, m.right = m.right, m.left 
        self.invertTree(m.left)
        self.invertTree(m.right)
        return m
        