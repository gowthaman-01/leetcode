def myAtoi(s):
    signs, sign, numString = {'-', '+'}, None, ''
    numbers = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    maxNumber = 2 ** 31
    for c in s:
        if numString:
            if c not in numbers:
                break
            numString += c
        else:
            if sign != None and c not in numbers:
                return 0
            elif c == ' ':
                continue
            elif c in signs and sign == None:
                sign = c

            elif c in numbers:
                numString += c
            else:
                return 0
    if not numString:
        return 0
    pos = len(numString) - 1
    number, place = 0, 1
    while pos >= 0:
        number += numbers[numString[pos]] * place
        place *= 10
        pos -= 1

    if sign == '+' or sign == None:
        if number > maxNumber - 1:
            return maxNumber - 1
        return number
    else:
        if -number < -maxNumber:
            return -maxNumber
        return -number
