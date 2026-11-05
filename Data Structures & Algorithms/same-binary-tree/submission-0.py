class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        liste1 = []
        liste2 = []
        
        def dfs(node, liste):
            if node is None:
                liste.append(None) # Wichtig: Leere Knoten mitschreiben!
                return
            
            dfs(node.left, liste)
            dfs(node.right, liste) 
            liste.append(node.val)
            
        # Beide Bäume durchlaufen und in ihre jeweiligen Listen schreiben
        dfs(p, liste1)
        dfs(q, liste2)
        
        # Am Ende vergleichen, ob beide Listen identisch sind
        return liste1 == liste2