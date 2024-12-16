# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/1407569532

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    kth_node = 0
    list_size = 1
    curr = head
    while curr:
        if list_size == k:
            kth_node = curr
        list_size += 1
        curr = curr.next 
    
    curr = head
    curr_position = 1
    while curr:
        if curr_position == list_size - k:
            curr.val, kth_node.val = kth_node.val, curr.val
        curr_position += 1
        curr = curr.next
    
    return head