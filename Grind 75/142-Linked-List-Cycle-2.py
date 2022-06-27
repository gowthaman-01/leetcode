def detectCycle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    if fast == None or fast.next == None:
        return None
    slow = head
    while(fast != slow):
        fast = fast.next
        slow = slow.next
    return fast
