class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> unique_nums(nums.begin(), nums.end());
        int max_count = 0;
        for (int num: nums) {
            if (unique_nums.count(num - 1)) {
                continue;
            }
            int count = 0;
            while (unique_nums.count(num)) {
                count++;
                num++;
            }
            max_count = std::max(max_count, count);
        }

        return max_count;
    }
};