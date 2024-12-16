# https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/1480298401

def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    if root is None:
        return result
    result.extend(self.inorderTraversal(root.left))
    result.append(root.val)
    result.extend(self.inorderTraversal(root.right))
    return result