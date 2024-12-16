# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/submissions/1393748592

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

def maxDepth(self, root: 'Node') -> int:
    if not root:
        return 0
    depth = 0
    for child in root.children:
        depth = max(depth, self.maxDepth(child))
    return depth+1