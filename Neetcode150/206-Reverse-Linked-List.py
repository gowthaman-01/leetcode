def reverseList(head):
    current = head 
    prev = None
    while current:
        temp = current.next
        current.next = prev 
        prev = current
        current = temp
    return prev