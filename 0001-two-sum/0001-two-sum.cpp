class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_to_index;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];
            if (num_to_index.count(complement)) {
                return {i, num_to_index[complement]};
            }
            num_to_index[nums[i]] = i;
        }

        return {};
    }
};