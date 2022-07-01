from collections import deque
import heapq
class Solution:
    def findClosestElements(self, arr, k, x):
        res, less, more = deque([]), [], []
        for num in arr:
            if num == x:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
            elif num < x:
                less.append(-num)
            else:
                more.append(num)
        heapq.heapify(less)
        heapq.heapify(more)
        while k > 0:
            if less and more:
                l, m = -less[0], more[0]
                if x - l == m - x:
                    res.appendleft(l)
                    heapq.heappop(less)
                elif x - l < m - x:
                    res.appendleft(l)
                    heapq.heappop(less)
                else:
                    res.append(m)
                    heapq.heappop(more)
            elif less:
                res.appendleft(-heapq.heappop(less))
            else:
                res.append(heapq.heappop(more))
            k -= 1

        return res