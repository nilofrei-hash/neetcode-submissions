# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        Liste = []
        def pfs(root):
            if root is None:
                return 
            Liste.append(root.val)
            pfs(root.left)
            pfs(root.right)
        pfs(root)
        return Liste