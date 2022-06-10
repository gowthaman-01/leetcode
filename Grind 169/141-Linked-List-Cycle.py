def hasCycle(head) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
