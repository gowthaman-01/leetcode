def removeNthFromEnd(head, n):
    slow_index, fast_index, slow, fast, store = 0, 0, head, head, {}
    store[0] = head        
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        slow_index += 1
        fast_index += 2
        store[slow_index] = slow
        store[fast_index] = fast
    if fast.next:
        fast_index += 1
        store[fast_index] = fast.next
    n_index = fast_index - n + 1 
    if n_index == 0:
        return head.next
    if n_index in store:
        delete = store[n_index]
        if n_index - 1 in store:
            prev = store[n_index - 1]
        elif n_index - 2 in store:
            prev = store[n_index - 2].next
        else:
            prev = None
    else:
        prev = store[n_index - 1]
        delete = prev.next
    after = delete.next
    prev.next = after
    return head