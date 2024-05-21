class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1; 
        std::vector<int> output(nums.size(), 0);
        
        for (int i = nums.size() - 1; i >= 0; i--) {
            output[i] = product; 
            product *= nums[i];
        }
        
        product = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            output[i] *= product;
            product *= nums[i];
        }
        
        return output;
    }
};
