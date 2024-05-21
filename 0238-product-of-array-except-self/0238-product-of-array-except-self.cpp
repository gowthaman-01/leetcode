class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1; 
        int zeroCount = 0;
        int zeroIndex = 0;
        
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                zeroIndex = i;
                zeroCount++;
            } else {
                product *= nums[i];
            }
        }
        
        if (zeroCount > 1) {
            return std::vector<int>(nums.size(), 0);
        }
        
        for (int i = 0; i < nums.size(); i++) {
            if (zeroCount) {
                if (i == zeroIndex) {
                    nums[i] = product; 
                } else {
                    nums[i] = 0;
                }
            } else {
               nums[i] = product / nums[i]; 
            }
        }
        
        return nums;
    }
};