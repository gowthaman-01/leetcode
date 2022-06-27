class Solution:
    def rec(self, i, target, cur, candidates):
        if i >= len(candidates) or target < 0:
            return None
        if target == 0:
            return [cur]
        pos1 = self.rec(
            i, target - candidates[i], cur + [candidates[i]], candidates)
        pos2 = self.rec(i + 1, target, cur, candidates)
        if pos1 and pos2:
            return pos1 + pos2
        else:
            return pos1 or pos2

    def combinationSum(self, candidates, target):
        return self.rec(0, target, [], candidates)
