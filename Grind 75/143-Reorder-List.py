# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return head
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        if fast.next:
            slow = slow.next
        # Reverse List
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        left, right = head, prev
        while left and right:
            leftNext, rightNext = left.next, right.next
            if left == right:
                left.next = None
                return
            left.next = right
            if rightNext == None:
                right.next = None
                return 
            right.next = leftNext
            left, right = leftNext, rightNext
        