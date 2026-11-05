# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def merge(a, b):
          if a is None:
            return b
          if b is None:
            return a
          node = TreeNode(a.val + b.val)      # 1. Knoten zuerst (Preorder)
          node.left = merge(a.left, b.left)
          node.right = merge(a.right, b.right)
          return node
        return merge(root1, root2)

        