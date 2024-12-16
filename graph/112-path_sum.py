# https://leetcode.com/problems/path-sum/submissions/1457709818

def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    queue = deque([(root, root.val)])

    while queue:
        curr, currSum = queue.popleft()

        if not curr.left and not curr.right and currSum == targetSum:
            return True

        if curr.left:
            queue.append((curr.left, currSum + curr.left.val))
        if curr.right:
            queue.append((curr.right, currSum + curr.right.val))

    return False