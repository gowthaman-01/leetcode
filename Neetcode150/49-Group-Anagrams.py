def groupAnagrams(strs):
    output = {}
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        if tuple(count) in output:
            output[tuple(count)].append(s)
        else:
            output[tuple(count)] = [s]
    return output.values()
