class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size() - 1;

        if (nums[l] < nums[r]) {
            return nums[l];
        }

        while (l < r){
            int m = (l + r) / 2;
            if (nums[m] > nums[m + 1]) {
                return nums[m + 1];
            } else if (nums[m] < nums[m - 1]) {
                return nums[m];
            } else if (nums[m] > nums[l] && nums[m] > nums[r]) {
                l = m + 1;
            } else if (nums[m] < nums[l] && nums[m] <  nums[r]) {
                r = m - 1;
            }
        }

        return nums[l];
    }
};