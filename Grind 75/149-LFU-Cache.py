class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        self.cache = {}
    
    def remove(self, node):
        remove = self.cache[node.key]
        previous = remove.prev
        after = remove.next
        previous.next = after
        after.prev = previous
        
    def insert(self, node):
        current = self.left.next
        self.left.next = node
        node.prev = self.left
        node.next = current
        current.prev = node
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            old = self.cache[key]
            self.remove(old)
        new = Node(key, value)
        self.insert(new)
        self.cache[key] = new
        if len(self.cache) > self.capacity:
            least = self.right.prev
            self.remove(least)
            self.cache.pop(least.key)
        