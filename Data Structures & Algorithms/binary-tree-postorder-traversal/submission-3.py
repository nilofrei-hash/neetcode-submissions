# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        Liste = []
        def psf(root):
          if root is None:
            return 
          psf(root.left)
          psf(root.right)
          Liste.append(root.val)
        psf(root)
        return Liste 