class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> numToIndex;
        for (int i = 0; i < nums.size(); i++) {
            int otherNumber = target - nums[i];
            if (numToIndex.count(otherNumber)) {
                return {i, numToIndex[otherNumber]};
            } else {
                numToIndex[nums[i]] = i;
            }
        }
        return {};
    }
};