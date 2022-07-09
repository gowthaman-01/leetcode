import random
class RandomizedSet:

    def __init__(self):
        self.store = []
        self.index = {}

    def insert(self, val: int) -> bool:
        if val in self.index:
            return False
        l = len(self.store)
        self.store.append(val)
        self.index[val] = l
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index:
            return False
        i = self.index[val]
        if len(self.store) > 1 and i != len(self.store) - 1:
            self.store[i] = self.store[-1]
            self.index[self.store[i]] = i
        self.store.pop()
        self.index.pop(val)
        return True

    def getRandom(self) -> int:
        l = len(self.store)
        i = random.randint(0, l - 1)
        return self.store[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()