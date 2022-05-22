import heapq
def lastStoneWeight(stones):
    for i in range(len(stones)):
        stones[i] = -stones[i]
    heapq.heapify(stones)
    while(len(stones) > 1):
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if first != second:
            new = first - second
            heapq.heappush(stones, new)
    if len(stones) == 1:
        return -stones[0]
    else:
        return 0
            
            
        