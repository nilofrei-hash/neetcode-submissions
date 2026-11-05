class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None  

# Tree setup
m = Node(20)
m.left = Node(30)
m.right = Node(5)

class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:
        if root is None:
            return 0
        
        # Check if the current node is within the range [low, high]
        current = root.val if low <= root.val <= high else 0
        
        # Recursively check left and right children
        left_sum = self.rangeSumBST(root.left, low, high)
        right_sum = self.rangeSumBST(root.right, low, high)
        
        return current + left_sum + right_sum

s = Solution()
print(s.rangeSumBST(m, 3, 9))