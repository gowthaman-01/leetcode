class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.empty()) {
            return 0;
        }
        unordered_set<int> set(nums.begin(), nums.end());
        int longest = 1;
        for (int num: nums) {
            if (set.count(num - 1)) {
                continue;
            }
            int cur = num; int count = 0; 
            while (set.count(cur)) {
                count++; 
                cur++;
                longest = max(longest, count);
            }
        }
        return longest;
    }
};