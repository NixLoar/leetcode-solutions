# https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/1393760032

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    if val > root.val:
        return self.searchBST(root.right, val)
    elif val < root.val:
        return self.searchBST(root.left, val)
    else:
            return root