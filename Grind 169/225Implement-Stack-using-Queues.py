from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque([])
        self.size = 0

    def push(self, x: int) -> None:
        self.q.append(x)
        if self.size != 0:
            for i in range(self.size):
                self.q.append(self.q.popleft())
        self.size += 1

    def pop(self) -> int:
        self.size -= 1
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.size == 0
