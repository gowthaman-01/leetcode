class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int max_length = 0;

        std::unordered_set<int> unique_nums(nums.begin(), nums.end());
        for (const int num: unique_nums) {
            if (unique_nums.count(num - 1)) {
                continue;
            }

            int cur_length = 0;
            int cur_num = num;
            while (unique_nums.count(cur_num)) {
                cur_length++;
                cur_num++;
            }

            max_length = std::max(max_length, cur_length);
        }

        return max_length;
    }
};