class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::unordered_set<int>unique_nums;
        for (int num: nums) {
            if (unique_nums.count(num)) {
                return true;
            }
            unique_nums.insert(num);
        }
        return false;
    }
};