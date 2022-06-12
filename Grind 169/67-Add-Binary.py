def addBinary(self, a: str, b: str) -> str:
    if len(a) > len(b):
        b = '0' * (len(a) - len(b)) + b
    elif len(b) > len(a):
        a = '0' * (len(b) - len(a)) + a
    
    pos = -1
    output = ''
    carry = False
    for i in range(len(a)):
        if a[pos] == '1' and b[pos] == '1':
            if carry:
                output = '1' + output
            else:
                output = '0' + output
                carry = True
        elif a[pos] == '1' or b[pos] == '1':
            if carry:
                output = '0' + output
            else:
                output = '1' + output
        else:
            if carry:
                output = '1' + output
                carry = False
            else:
                output = '0' + output
        pos -= 1
    if carry:
        output = '1' + output
    
    return output
                    