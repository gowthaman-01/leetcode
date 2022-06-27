# DFS
class DFS:
    def fill(self, matrix):
        graph = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    graph[i] = graph.get(i, []) + [j]
        return graph

    def dfs(self, graph, node, visited):
        if node not in visited:
            visited.add(node)
            for neighbour in graph[node]:
                self.dfs(graph, neighbour, visited)

    def findCircleNum(self, isConnected) -> int:
        graph, visited, province = self.fill(isConnected), set(), 0
        for node in graph.keys():
            if node not in visited:
                province += 1
                self.dfs(graph, node, visited)
        return province

# BFS
