# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/1399196932

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    result = []
    if root is None:
        return result
    result.extend(self.postorderTraversal(root.left))
    result.extend(self.postorderTraversal(root.right))
    result.append(root.val)
    return result