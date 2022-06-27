def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    if sum(cost) > sum(gas):
        return -1
    total, possible = 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]
        if total < 0:
            total = 0
            possible = i + 1
    return possible
