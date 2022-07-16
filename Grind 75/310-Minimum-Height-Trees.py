from collections import deque
class Solution:
    def findMinHeightTrees(self, n, edges):
        graph, q = {}, deque([])
        for i in range(n): graph[i] = set()
        for start, end in edges:
            graph[start].add(end)
            graph[end].add(start)
        for node in graph:
            if len(graph[node]) == 1:
                q.append(node)
        while len(graph) > 2:
            for i in range(len(q)):
                top = q.popleft()
                node = graph[top].pop()
                graph[node].remove(top)
                graph.pop(top)
                if len(graph[node]) == 1:
                    q.append(node)
        return list(graph.keys())
                    