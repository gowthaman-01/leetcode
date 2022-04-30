import heapq
def topKFrequent(nums, k):
    hm = {}
    for num in nums:
        hm[num] = hm.get(num, 0) + 1
    li = []
    for num in hm.keys():
        li.append((-1 * hm[num], num))
    heapq.heapify(li)
    output = []
    for i in range(k):
        output.append(heapq.heappop(li)[1])
    return output
        
        