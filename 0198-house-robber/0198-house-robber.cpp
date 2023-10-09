struct Decision {
    int rob; 
    int skip;
};

class Solution {
public:
    int rob(vector<int>& nums) {
        vector<Decision>dp; 
        for (int i = 0; i < nums.size(); i++) {
            if (!dp.size()) {
                dp.push_back({nums[i], 0});
            } else {
                dp.push_back({nums[i] + dp[i - 1].skip, max(dp[i - 1].rob, dp[i - 1].skip)}); 
            }
        }
        return max(dp[nums.size() - 1].rob, dp[nums.size() - 1].skip);
    }
};