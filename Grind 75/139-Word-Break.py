class Solution:
    def prefix(self, s, word):
        if len(word) > len(s):
            return False
        for i in range(len(word)):
            if word[i] != s[i]:
                return False
        return True

    def suffix(self, s, word):
        l = len(word)
        return s[l:]

    def helper(self, s, wordDict, store):
        if s == "":
            return True
        if s in store:
            return store[s]
        for word in wordDict:
            if self.prefix(s, word):
                if self.helper(self.suffix(s, word), wordDict, store):
                    store[s] = True
                    return store[s]
        store[s] = False
        return store[s]

    def wordBreak(self, s, wordDict) -> bool:
        store = {}
        return self.helper(s, wordDict, store)
