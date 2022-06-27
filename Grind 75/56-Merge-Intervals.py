def merge(intervals):
    intervals.sort()
    cur = intervals[0]
    output = []
    for interval in intervals[1:]:
        ll, lr, rl, rr = cur[0], cur[1], interval[0], interval[1]
        if lr < rl:
            output.append(cur)
            cur = interval
        elif lr > rr:
            continue
        else:
            cur = [cur[0], interval[1]]

    if not output or output[-1] != cur:
        output.append(cur)

    return output
