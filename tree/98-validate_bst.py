# https://leetcode.com/problems/validate-binary-search-tree/submissions/1399191685

def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.checkBST(root, float('-inf'), float('inf'))

def checkBST(self, node, min_val, max_val):
    if not node:
        return True
    if node.val >= max_val or node.val <= min_val:
        return False
    return self.checkBST(node.left, min_val, node.val) and self.checkBST(node.right, node.val, max_val)    