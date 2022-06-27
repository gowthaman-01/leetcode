class Element:
    def __init__(self):
        self.val = None
        self.min = None


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        element = Element()
        element.val = val
        if not self.stack:
            element.min = val
        else:
            element.min = min(val, self.stack[-1].min)
        self.stack.append(element)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].val

    def getMin(self) -> int:
        return self.stack[-1].min
