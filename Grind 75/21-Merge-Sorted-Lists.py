def mergeTwoLists(list1, list2):
    if not list1 and not list2:
        return None
    elif not list1:
        return list2
    elif not list2:
        return list1
    
    current, head, l1, l2 = None, None, list1, list2
    
    while l1 and l2:
        if l1.val <= l2.val:
            if not head:
                head = l1
                current = head
            else:
                current.next = l1
                current = current.next
            l1 = l1.next
        else:
            if not head:
                head = l2
                current = head
            else:
                current.next = l2
                current = current.next
            l2 = l2.next
    if l1:  
        while l1:
            current.next = l1
            current = current.next
            l1 = l1.next
    elif l2:
        while l2:
            current.next = l2
            current = current.next
            l2 = l2.next
    
    return head
    