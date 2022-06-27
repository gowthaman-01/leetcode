def isPalindrome(head):
    if not head.next:
        return True
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        
    start = slow.next

    # Reverse second half of linked list 
    
    prev = None
    while start:
        temp = start.next
        start.next = prev
        prev = start
        start = temp
    
    begin, end = head, prev
    while begin and end:
        if begin.val != end.val:
            return False
        begin = begin.next
        end = end.next

    return True