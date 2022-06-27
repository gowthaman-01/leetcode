class Trie:
    def __init__(self):
        self.wordSet = set()
        self.prefixSet = set()

    def insert(self, word: str) -> None:
        self.wordSet.add(word)
        for i in range(1, len(word)):
            self.prefixSet.add(word[0: i])

    def search(self, word: str) -> bool:
        return word in self.wordSet

    def startsWith(self, prefix: str) -> bool:
        return prefix in self.wordSet or prefix in self.prefixSet
