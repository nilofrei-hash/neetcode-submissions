# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.Summe = 0
        def dfs(root):
            if root is None:
                return 
            if root.val <= high and root.val >= low:
                self.Summe += root.val 
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return self.Summe 