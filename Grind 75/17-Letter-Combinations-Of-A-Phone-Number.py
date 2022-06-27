class Solution:
    def combine(self, digits, rep, store):
        if digits in store:
            return store[digits]
        output = []
        if len(digits) == 0:
            return output
        if len(digits) == 1:
            return rep[digits[0]]
        for c in rep[digits[0]]:
            res = self.combine(digits[1:], rep, store)
            for i in range(len(res)):
                new = c + res[i]
                output.append(new)
        store[digits] = output
        return output

    def letterCombinations(self, digits: str):
        rep = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        store = {}
        combinations = self.combine(digits, rep, store)
        return combinations
