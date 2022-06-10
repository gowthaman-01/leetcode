def longestCommonPrefix(strs):
    pos, letter, output = 0, 0, ""
    while True:
        if pos < len(strs[0]):
            letter = strs[0][pos]
        else:
            return output
        for s in strs:
            if pos >= len(s):
                return output
            if s[pos] != letter:
                return output
        output += letter
        pos += 1
                