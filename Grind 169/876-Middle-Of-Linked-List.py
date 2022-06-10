def middleNode(head):
    slow, fast = head, head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next
    if fast.next:
        return slow.next
    else:
        return slow
