class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        if (nums.size() == 0) {
            return 0;
        }
        int l = 0; 
        int r = nums.size() - 1;
        while (true) {
            while (nums[l] != val && l < r) {
                l++;
            }
            while (nums[r] == val && l < r) {
                r--;
            }
            if (l >= r) {
                if (l == r && nums[l] != val) {
                    return l + 1;
                } else {
                    return l;
                }
                
            }
            
            nums[l] = nums[r];
            l++;
            r--;
        }
    }
};