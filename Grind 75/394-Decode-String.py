class Solution:
    def decodeString(self, s):
        stack, cur, pos, res = [], "", 0, ""
        while pos < len(s):
            if s[pos].isnumeric():
                num = ""
                while s[pos].isnumeric():
                    num += s[pos]
                    pos += 1
                stack.append(num)
                stack.append(s[pos])
            elif s[pos].isalpha():
                stack.append(s[pos])
            else:
                top = stack.pop()
                while top.isalpha():
                    cur = top + cur
                    top = stack.pop()
                num = stack.pop()
                stack.append(int(num) * cur)
                cur = ""
            pos += 1
        for c in stack:
            res += c
        return res
                