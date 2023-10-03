class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map; 
        for (int i = 0; i < nums.size(); i++) {
            int cur = nums[i];
            if (map.count(target - cur)) {
                return {map[target - cur], i};
            } else {
                map[cur] = i;
            }
        }
        return {};
    }
};