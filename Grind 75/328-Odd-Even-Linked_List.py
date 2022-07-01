class Solution:
    def oddEvenList(self, head):
        if not head: return head
        odd, even, new, start = head, head.next, head, head.next
        while odd and even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
                even.next = odd.next
                even = even.next
            else: break
        odd.next = start
        return new
    
