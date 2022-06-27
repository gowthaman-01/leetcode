def reverseBits(n):
    res = 0
    for i in range(32):
        bit = (n >> i) & 1
        bit = bit << (31 - i)
        res = res | bit
    return res
            