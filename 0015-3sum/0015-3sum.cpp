class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> triplets;

        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] > 0) break;
            if (i > 0 && nums[i] == nums[i - 1]) continue;

            int target = -nums[i];
            int l = i + 1; int r = nums.size() - 1;
            
            while (l < r) {
                int complement = nums[l] + nums[r];
                if (complement == target) {
                    triplets.push_back({nums[i], nums[l], nums[r]});
                    do {
                        l++;
                    } while (l < r && nums[l] == nums[l - 1]);
                    r--;
                } else if (complement > target) {
                    r--;
                } else {
                    l++;
                }
            }
        }

        return triplets;
    }
};

