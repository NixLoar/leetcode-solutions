# https://leetcode.com/problems/insert-into-a-binary-search-tree/submissions/1393771639

def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        root = TreeNode(val)

    elif val < root.val:
        if not root.left:
            root.left = TreeNode(val)
        else:
            self.insertIntoBST(root.left, val)
    else:
        if not root.right:
            root.right = TreeNode(val)
        else:
            self.insertIntoBST(root.right, val)
    return root