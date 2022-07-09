class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) < 2: return 0
        intervals.sort()
        res, prev = 0, intervals[0]
        for interval in intervals[1:]:
            if interval[0] < prev[1]:
                if interval[1] < prev[1]:
                    prev = interval
                res += 1
            else:
                prev = interval
        return res
