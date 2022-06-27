def countBits(n):
    count = [0 for i in range(0, n + 1)]
    sig = 1
    for i in range(1, n + 1):
        if sig * 2 == i:
            sig = i
        count[i] = count[i - sig] + 1
    return count
