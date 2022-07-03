class Solution:
    def pow(self, x, n, store):
        if n in store: return store[n]
        value = self.pow(x, n // 2, store) * self.pow(x, n // 2, store) * self.pow(x, n % 2, store)
        store[n] = value
        return value
        
    def myPow(self, x: float, n: int) -> float:
        if x == 0: return 0
        if n == 0: return 1
        store = {0: 1, 1: x, 2: x ** 2}
        value = self.pow(x, abs(n), store)
        if n < 0:
            return 1 / value
        return value
        