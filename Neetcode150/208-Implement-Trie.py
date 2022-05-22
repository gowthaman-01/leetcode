class Trie:
    def __init__(self):
        self.map = {}

    def insert(self, word: str) -> None:
        for i in range(0, len(word)):
            current = self.map.get(word[0: i], '')
            if not current:
                self.map[word[0: i]] = 'prefix'
            elif current == 'word' or current == 'prefix and word':
                self.map[word[0: i]] = 'prefix and word'
            else:
                self.map[word[0: i]] == 'prefix'

        current = self.map.get(word, '')
        if not current:
            self.map[word] = 'prefix and word'
        elif current == 'prefix' or current == 'prefix and word':
            self.map[word] = 'prefix and word'
        else:
            self.map[word] == 'word'

    def search(self, word: str) -> bool:
        result = self.map.get(word, '')
        return result == 'word' or result == 'prefix and word'

    def startsWith(self, prefix: str) -> bool:
        result = self.map.get(prefix, '')
        return result == 'prefix' or result == 'prefix and word'
