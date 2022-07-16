class Solution:
    def cycle(self, course, graph, visited):
        if course in visited: return True
        if graph[course] == []: return False
        visited.add(course)
        for n in graph[course]:
            if self.cycle(n, graph, visited): return True
        graph[course] = []
        visited.remove(course)
        return False
    
    def canFinish(self, numCourses: int, prerequisites):
        graph = {}
        for n in range(numCourses): graph[n] = []
        for to, req in prerequisites:
            graph[req].append(to)
        for course in graph:
            visited = set()
            if self.cycle(course, graph, visited): return False
        return True