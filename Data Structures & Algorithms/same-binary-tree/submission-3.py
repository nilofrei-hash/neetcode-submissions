# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            # Both nodes are empty, so this part matches
            if p is None and q is None:
                return True

            # Exactly one node is empty, so the trees differ
            if p is None or q is None:
                return False

            # Values differ, so the trees differ
            if p.val != q.val:
                return False

            # Both current nodes match; compare their children
            return dfs(p.left, q.left) and dfs(p.right, q.right)

        return dfs(p, q)
        