class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freq_map;
        for (int num: nums) {
            freq_map[num]++;
        }

        std::vector<std::vector<int>> buckets(nums.size() + 1);
        for (auto& [num, freq]: freq_map) {
            buckets[freq].push_back(num);
        }

        std::vector<int> res;
        for (int i = nums.size(); i >= 0; i--) {
            if (k == 0) {
                return res;
            }

            for (int n: buckets[i]) {
                res.push_back(n);
                k--;
            }
        }

        return res;
    }
};