class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        d = ListNode()
        r = d

        total = c = 0

        while l1 or l2 or c:
            total = c

            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            num = total % 10
            c = total // 10
            d.next = ListNode(num)
            d = d.next
        
        return r.next