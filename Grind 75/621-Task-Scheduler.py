from collections import deque
import heapq
def leastInterval(tasks, n):
    freq, q = {}, deque([])
    for task in tasks:
        freq[task] = freq.get(task, 0) - 1
    heap = list(freq.values())
    heapq.heapify(heap)
    time, completed = 0, 0
    while completed < len(tasks):
        if heap:
            top_freq = heapq.heappop(heap)
            time += 1
            top_freq += 1
            completed += 1
            if top_freq != 0:
                q.append((time + n, top_freq))
            if q and q[0][0] == time:
                heapq.heappush(heap, q.popleft()[1])
        else:
            next_task = q.popleft()
            time = next_task[0] + 1
            next_freq = next_task[1] + 1
            if next_freq != 0:
                q.append((time + n, next_freq))
            completed += 1
    return time