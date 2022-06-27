def backspaceCompare(self, s: str, t: str) -> bool:
    sp, tp = len(s) - 1, len(t) - 1
    sb, tb = 0, 0
    while sp >= 0 and tp >= 0:
        if s[sp] == '#' or t[tp] == '#':
            if s[sp] == '#':
                sp -= 1
                sb += 1
            if t[tp] == '#':
                tp -= 1
                tb += 1
            continue
        if sb or tb:
            if sb:
                sp -= 1
                sb -= 1
            if tb:
                tp -= 1
                tb -= 1
            continue
        if s[sp] != t[tp]:
            return False
        tp -= 1
        sp -= 1
    while tp >= 0:
        if t[tp] == '#':
            tb += 1
            tp -= 1
        elif tb:
            tb -= 1
            tp -= 1
        else:
            return False
    while sp >= 0:
        if s[sp] == '#':
            sb += 1
            sp -= 1
        elif sb:
            sb -= 1
            sp -= 1
        else:
            return False
    return True
