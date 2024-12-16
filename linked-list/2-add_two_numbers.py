# https://leetcode.com/problems/add-two-numbers/submissions/1374671276

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        i = 0
        while l1 is not None:
            num1 += l1.val*10**i
            l1 = l1.next
            i+=1	
            
        num2 = 0
        i = 0
        while l2 is not None:
            num2 += l2.val*10**i
            l2 = l2.next
            i+=1	

        total = num1 + num2
        if total == 0:
            return ListNode(0)

        head, curr = None, None
        while total > 0:
            digit = total%10
            if head is None:
                head = ListNode(digit)
                curr = head
            else:
                curr.next = ListNode(digit)
                curr = curr.next
            total = total // 10

        return head