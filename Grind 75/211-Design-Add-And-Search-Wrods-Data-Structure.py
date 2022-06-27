class WordDictionary:
    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t['-'] = True

    def search_helper(self, word, index, trie):
        for i in range(index, len(word)):
            if word[i] == '.':
                for possible in trie:   
                    if possible != '-' and self.search_helper(word, i + 1, trie[possible]):
                        return True
                return False       
            else:
                if word[i] in trie:
                    trie = trie[word[i]]
                else:
                    return False
        return '-' in trie
        
    def search(self, word: str) -> bool:
        return self.search_helper(word, 0, self.trie)

