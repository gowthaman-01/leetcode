class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> set(nums.begin(), nums.end());
        int longest = 0;
        for (int num: nums) {
            if (!set.count(num - 1)) {
                int cur = 0; 
                while (set.count(num)) {
                    cur++;
                    num++;
                }
                longest = max(longest, cur);
            }
        }
        return longest;
    }
};