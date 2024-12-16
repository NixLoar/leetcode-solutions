# https://leetcode.com/problems/reverse-linked-list/submissions/1374657277

def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    nodePrev, nodeNext = None, None
    node = head
    while node is not None:
        nodeNext = node.next
        node.next = nodePrev
        nodePrev = node
        node = nodeNext
    return nodePrev