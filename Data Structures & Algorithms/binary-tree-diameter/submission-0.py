# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # Oder über nonlocal gelöst
        
        def dfs(node):
            if node is None:
                return 0
            
            # 1. Hole die Höhen der Kinder
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            
            # 2. Aktualisiere den maximalen Diameter (linker Pfad + rechter Pfad)
            self.max_diameter = max(self.max_diameter, left_height + right_height)
            
            # 3. Gebe die Höhe des aktuellen Knotens an den Elternknoten zurück
            return max(left_height, right_height) + 1

        dfs(root)
        return self.max_diameter