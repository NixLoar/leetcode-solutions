# https://leetcode.com/problems/swap-nodes-in-pairs/submissions/1374705967

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    prev, node = dummy, head
    while node and node.next is not None:
        next_pair = node.next.next
        second_node = node.next

        second_node.next = node
        node.next = next_pair
        prev.next = second_node

        prev = node
        node = next_pair
        
    return dummy.next