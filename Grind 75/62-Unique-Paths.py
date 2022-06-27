class Solution:
    def helper(self, m, n, store):
        key1 = str(m) + ',' + str(n)
        if key1 in store:
            return store[key1]
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        paths = self.helper(m, n - 1, store) + self.helper(m - 1, n, store)
        store[key1] = paths
        return paths
    
    def uniquePaths(self, m: int, n: int) -> int:
        store = {}
        return self.helper(m, n, store)
