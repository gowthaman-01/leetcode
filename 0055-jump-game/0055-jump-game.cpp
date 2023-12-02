class Solution {
public:
    bool canJump(vector<int>& nums) {
        vector<bool>reachable(nums.size(), false);
        reachable[nums.size() - 1] = true;
        for (int i = nums.size() - 2; i >= 0; i--) {
            for (int j = 1; j <= nums[i]; j++) {
                if ((i + j) < nums.size() && reachable[i + j]) {
                    reachable[i] = true;
                    break;
                }
            }
        }
        return reachable[0];
    }
};