class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map; 
        for (int i = 0; i < nums.size(); i++) {
            int cur = nums[i];
            if (map.count(cur) && i - map[cur] <= k) {
                return true;
            }
            map[cur] = i;
        }
        return false;
    }
};