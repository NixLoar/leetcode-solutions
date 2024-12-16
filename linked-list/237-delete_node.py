# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/1377074362

def deleteNode(self, node):
    node.val = node.next.val
    node.next = node.next.next