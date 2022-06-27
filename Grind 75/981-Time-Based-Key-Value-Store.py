from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.hash = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        node = (value, timestamp)
        self.hash[key].append(node)

    def get(self, key: str, timestamp: int) -> str:
        nodes = self.hash.get(key, "")
        if not nodes:
            return nodes
        l, r = 0, len(nodes) - 1
        output = ""
        while l <= r:
            m = (l + r) // 2
            value, time = nodes[m][0], nodes[m][1]
            if timestamp == time:
                return value
            elif timestamp > time:
                output = value
                l = m + 1
            else:
                r = m - 1
        return output
