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
            int count = 0; 
            while (set.count(num)) {
                count++; 
                num++;
                longest = max(longest, count);
            }
        }
        return longest;
    }
};