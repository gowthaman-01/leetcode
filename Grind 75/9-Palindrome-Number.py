def isPalindrome(x):
    if x < 0:
        return False
    div = 1
    while x // div >= 10:
        div *= 10
    while x:
        left = x // div
        right = x % 10
        if right != left:
            return False
        x = x % div
        x = x // 10
        div /= 100
    return True
