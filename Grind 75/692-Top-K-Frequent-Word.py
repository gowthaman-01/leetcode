import heapq


def topKFrequent(words, k):
    wordToFreq = {}
    for word in words:
        wordToFreq[word] = wordToFreq.get(word, 0) + 1

    freqToWord = {}
    for word in wordToFreq:
        freqToWord[wordToFreq[word]] = freqToWord.get(
            wordToFreq[word], []) + [word]

    heap = []
    for freq in freqToWord:
        node = (-freq, freqToWord[freq])
        heap.append(node)

    heapq.heapify(heap)
    output = []
    while k and heap:
        top = heapq.heappop(heap)
        top[1].sort()
        for word in top[1]:
            output.append(word)
            k -= 1
            if k == 0:
                return output
    return output
