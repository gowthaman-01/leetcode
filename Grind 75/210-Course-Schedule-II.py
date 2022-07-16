class Solution:
    def cycle(self, course, graph, visited):
        if course in visited: return True
        if graph[course] == []: return False
        visited.add(course)
        for n in graph[course]:
            if self.cycle(n, graph, visited): return True
        visited.remove(course)
        graph[course] = []
        return False
        
    def visit(self, course, graph, res, visited):
        if course not in visited:
            visited.add(course)
            for n in graph[course]:
                self.visit(n, graph, res, visited)
            res.append(course)
                  
    def findOrder(self, numCourses: int, prerequisites):
        graph, copy = {}, {}
        
        # Build graph
        for n in range(numCourses): 
            graph[n] = []
            copy[n] = []
        for to, req in prerequisites:
            graph[req].append(to)
            copy[req].append(to)
        
        # Check for cycle
        for course in graph:
            visited = set()
            if self.cycle(course, copy, visited): return []
            
        res, visited = [], set()
        # DFS
        for course in graph:
            if course not in visited:
                self.visit(course, graph, res, visited)
        
        return res[-1::-1]
        
        
        