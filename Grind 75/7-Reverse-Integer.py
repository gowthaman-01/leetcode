class Solution:
    def reverse(self, x: int) -> int:
        cur, num = 0, abs(x)
        while num != 0:
            digit = num % 10
            if (cur > ((2 ** 31) - 1) // 10 and x > 0) or (cur > (2 ** 31) // 10 and x < 0):
                return 0
            if (cur == ((2 ** 31) - 1) // 10 and x > 0) or (cur > (2 ** 31) // 10 and x < 0):
                if (digit > 7 and x > 0) or (digit > 8 and x < 0):
                    return 0
            
            num = num // 10
            cur = cur * 10 + digit       
        if x < 0:
            return -cur
        return cur