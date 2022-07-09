class Solution:
    def calculate(self, s: str) -> int:
        stack, sign, cur, pos = [], 1, 0, 0
        nums = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        operator = {"+", "-", "/", "*"}
        
        while pos < len(s):
            c = s[pos]
            if c == " ":
                pos += 1
                continue
            if c in nums:
                cur = cur * 10 + int(c)
                if pos + 1 >= len(s) or s[pos + 1] not in nums:
                    stack.append(cur * sign)
                    cur = 0
            else:
                if c == "+":
                    sign = 1
                elif c == "-":
                    sign = -1
                else:
                    left = stack.pop()
                    pos += 1
                    while s[pos] == " ":
                        pos += 1
                    right = int(s[pos])
                    while pos + 1 < len(s) and s[pos + 1] in nums:
                        pos += 1
                        right = right * 10 + int(s[pos])
                    if c == "*":
                        new = left * right
                        stack.append(new)
                    else:
                        new = abs(left) // abs(right)
                        if left < 0:
                            new = -new
                        stack.append(new)
                    cur = 0
            pos += 1
        return sum(stack)
                