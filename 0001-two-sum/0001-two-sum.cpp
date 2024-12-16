class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> num_to_index(nums.size());
        
        for (int i = 0; i < nums.size(); i++) {
            int other = target - nums[i];
            if (num_to_index.count(other)) {
                return {num_to_index[other], i};
            } else {
                num_to_index[nums[i]] = i;
            }
        }

        return {};
    }
};