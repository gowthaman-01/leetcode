class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int>ways(nums.size(), 0); 
        ways[nums.size() - 1] = 0;
        for (int i = nums.size() - 2; i >= 0; i--) {
            int m = -1;
            for (int j = 1; j <= nums[i]; j++) {
                if (i + j == nums.size() - 1) {
                    m = 1; 
                    break;
                } else if (i + j < nums.size() - 1 && ways[i + j] > 0) {
                    m = m == -1 ? ways[i + j] + 1 : min(m, ways[i + j] + 1); 
                }  
            }
            ways[i] = m;
        }
        return ways[0];
    }
};
