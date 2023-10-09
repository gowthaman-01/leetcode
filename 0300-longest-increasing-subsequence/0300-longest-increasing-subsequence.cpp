class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int longest = 1; 
        vector<pair<int, int>>dp; 
        for (int num: nums) {
            int cur = 0;
            for (pair<int, int> p: dp) {
                if (p.first < num) {
                    cur = max(cur, p.second); 
                }
            }
            dp.push_back({num, cur + 1});
            longest = max(longest, cur + 1);
        }
        return longest;
    }
};