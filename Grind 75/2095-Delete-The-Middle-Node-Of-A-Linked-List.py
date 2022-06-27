def deleteMiddle(head):
    if not head or not head.next:
        return None
    slow, fast = head, head
    prev = None
    while fast.next and fast.next.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if fast.next:
        prev = slow
        slow = slow.next
    prev.next = slow.next
    slow.next = None
    return head
