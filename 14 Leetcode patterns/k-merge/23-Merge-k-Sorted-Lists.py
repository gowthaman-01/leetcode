import heapq
def mergeKLists(lists): 
    if not lists: 
        return None
    first, nodes = [], {}
    for i in range(len(lists)):
        if lists[i]:
            nodes[i] = lists[i]
            first.append((lists[i].val, i))
    heapq.heapify(first)
    prev, head = None, None
    while len(first):
        min_element = heapq.heappop(first)
        min_index = min_element[1]
        min_node = nodes[min_index]
        if not prev:
            prev = min_node
            head = prev
        else:
            prev.next = min_node
            prev = min_node
        if min_node.next:
            heapq.heappush(first, (min_node.next.val, min_index))
            nodes[min_index] = min_node.next
    return head
        