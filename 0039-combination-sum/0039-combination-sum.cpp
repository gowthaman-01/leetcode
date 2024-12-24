class Solution {
public:
    void findCombinations(std::vector<int>& candidates, int target,
                          std::vector<int>& current, int current_sum, int i,
                          std::vector<std::vector<int>>& combinations) {
        if (current_sum > target || i == candidates.size())
            return;
        if (current_sum == target) {
            combinations.emplace_back(current);
            return;
        }

        findCombinations(candidates, target, current, current_sum, i + 1,
                         combinations);

        current.push_back(candidates[i]);
        findCombinations(candidates, target, current,
                         current_sum + candidates[i], i, combinations);
        current.pop_back();
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        std::vector<std::vector<int>> combinations;
        std::vector<int> current;
        findCombinations(candidates, target, current, 0, 0, combinations);
        return combinations;
    }
};