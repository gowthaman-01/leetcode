def insert(intervals):
    output = []
    for i in range(len(intervals)):
        s1, e1 = newInterval[0], newInterval[1]
        s2, e2 = intervals[i][0], intervals[i][1]
        if s1 > e2:
            output += [intervals[i]]
            continue
        if e1 < s2:
            return output + [newInterval] + intervals[i::]
        else:
            newInterval = [min(s1, s2), max(e1, e2)]
    return output + [newInterval]
