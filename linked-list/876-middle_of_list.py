# https://leetcode.com/problems/middle-of-the-linked-list/submissions/1365165938

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    i = 0
    while node is not None:
        i += 1
        node = node.next
    mid = i // 2
    node = head
    for i in range(mid):
        node = node.next
    return node