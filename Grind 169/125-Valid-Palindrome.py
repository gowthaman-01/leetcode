def ValidPalindrome(s):
    l, r = 0, len(s) - 1
    while l <= r:
        if not s[l].isalnum():
            l += 1
            continue
        elif not s[r].isalnum():
            r -= 1
            continue
        if s[r].isnumeric():
            if s[r] != s[l]:
                return False
        if s[r].lower() != s[l].lower():
            return False
        r -= 1 
        l += 1
    return True

print(ValidPalindrome("race a car"))