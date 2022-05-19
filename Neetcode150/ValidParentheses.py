from collections import deque
def isValid(s):
    size = 0
    stack = deque([])
    opening = {'(': 1, '[': 2, '{': 3}
    closing = {')': 1, ']': 2, '}': 3}
    for c in s: 
        if size == 0:
            if c in opening:
                stack.append(c)
                size += 1
                continue
            else: 
                return False
        if c in opening: 
            stack.append(c)
            size += 1
        else:
            top = stack.pop()
            if opening[top] != closing[c]: 
                return False
            size -= 1
    if size != 0: 
        return False
    else:
        return True
    
                
            