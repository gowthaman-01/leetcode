from math import *


class Solution:
    def evaluate(self, num1, num2, operator):
        if operator == '*':
            return num1 * num2
        elif operator == '/':
            if num1 / num2 < 0:
                return ceil(num1 / num2)
            else:
                return floor(num1 / num2)
        elif operator == '+':
            return num1 + num2
        else:
            return num1 - num2

    def evalRPN(self, tokens):
        stack, operators = [], {'*', '+', '/', '-'}
        if len(tokens) == 1:
            return tokens[0]
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                num1, num2 = stack.pop(), stack.pop()
                stack.append(self.evaluate(num2, num1, token))
        return stack.pop()
