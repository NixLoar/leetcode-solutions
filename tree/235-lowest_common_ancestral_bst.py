# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/1401075946

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return
    if p.val > q.val:
        p, q = q, p
    return self.findLCA(root, p, q)
    
def findLCA(self, node, p, q):
    if node.val == p.val or node.val == q.val:
        return node
    elif node.val < q.val and node.val > p.val:
        return node
    elif node.val < q.val and node.val < p.val:
        return self.findLCA(node.right, p, q)
    else:
        return self.findLCA(node.left, p, q)