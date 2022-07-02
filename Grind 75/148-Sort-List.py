# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMid(self, head):
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        if not right and not left: return left
        if not right: return left
        if not left: return right
        cur, head = None, None
        while left and right:
            if left.val <= right.val:
                if not head:
                    cur, head = left, left
                else:
                    cur.next = left
                    cur = cur.next
                left = left.next
            else:
                if not head:
                    cur, head = right, right
                else:
                    cur.next = right
                    cur = cur.next
                right = right.next
        while left:
            cur.next = left
            cur, left = cur.next, left.next
        while right:
            cur.next = right
            cur, right = cur.next, right.next
        return head
        
        
    def sortList(self, head):
        if not head or not head.next: return head
        mid = self.getMid(head)
        temp = mid.next
        mid.next = None
        left = self.sortList(head)
        right = self.sortList(temp)
        return self.merge(left, right)