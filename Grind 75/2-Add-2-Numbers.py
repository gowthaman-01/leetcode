# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        carry, cur, head = 0, None, None
        while l1 and l2:
            val = l1.val + l2.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            new = ListNode(val)
            if cur == None:
                head = new
                cur = new
            else:
                cur.next = new
                cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            val = l1.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            new = ListNode(val)
            cur.next = new
            cur = cur.next
            l1 = l1.next
        while l2:
            val = l2.val + carry
            if val >= 10:
                carry = 1
                val = val % 10
            else:
                carry = 0
            new = ListNode(val)
            cur.next = new
            cur = cur.next
            l2 = l2.next
        if carry == 1:
            cur.next = ListNode(1)
        return head