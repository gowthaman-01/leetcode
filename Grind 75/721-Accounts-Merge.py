# Union find
class Solution:
    def find(self, parent, i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        return parent[i]
    
    def combine(self, parent, i, j):
        pi, pj = self.find(parent, i), self.find(parent, j)
        if pi == pj: return 
        parent[pi] = pj
        
    def accountsMerge(self, accounts):
        parent, emailAccount = [i for i in range(len(accounts))], {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in emailAccount:
                    emailAccount[email] = i
                else:
                    self.combine(parent, i, emailAccount[email])
        new, visited = {}, set()
        for acc in range(len(parent)):
            par = self.find(parent, acc)
            if par in new:
                for email in accounts[acc][1:]:
                    if email not in visited:
                        visited.add(email)
                        new[par].append(email)
            else:
                add = []
                for email in accounts[acc][1:]:
                    if email not in visited:
                        visited.add(email)
                        add.append(email)  
                new[par] = add
        res = []
        for acc, email in new.items():
            email.sort()
            email = [accounts[acc][0]] + email
            res.append(email)
        return res
    
# DFS
from collections import defaultdict
class Solution:
    def dfs(self, email, graph, visited, new):
        if email not in visited:
            visited.add(email)
            new.append(email)
            for n in graph[email]:
                self.dfs(n, graph, visited, new)
         
    def accountsMerge(self, accounts):
        graph, res, emailOwner, visited = defaultdict(list), [], {}, set()
        # Construct graph
        for account in accounts:
            for i in range(1, len(account)):
                emailOwner[account[i]] = account[0]
                if i + 1 < len(account):
                    graph[account[i]].append(account[i + 1])
                    graph[account[i + 1]].append(account[i])
                else:
                    if account[i] not in graph: graph[account[i]] = []
        # Run dfs on each email
        for email in graph:
            if email not in visited:
                new = []
                self.dfs(email, graph, visited, new)  
                new.sort()
                new = [emailOwner[email]] + new
                res.append(new)
        return res