# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        prev, cur, l = None, head, 0
        while cur:
            l += 1
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        # Length of list
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        k = k % l
        if k == 0: return head
        
        # Reversing entire list
        head1 = self.reverse(head)
        cur = head1
        for i in range(k - 1):
            cur = cur.next
        head2 = cur.next
        cur.next = None
        
        # Reversing first k nodes
        res = self.reverse(head1)
        
        # Reversing nodes after
        sec = self.reverse(head2)
        head1.next = sec
        
        return res
        
            
        