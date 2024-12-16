# https://leetcode.com/problems/balanced-binary-tree/submissions/1399162965

def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True
    if abs(self.calcHeight(root.left) - self.calcHeight(root.right)) > 1:
        return False
    else:
        return self.isBalanced(root.left) and self.isBalanced(root.right)

def calcHeight(self, node):
    if not node:
        return 0
    return 1 + max(self.calcHeight(node.left), self.calcHeight(node.right))