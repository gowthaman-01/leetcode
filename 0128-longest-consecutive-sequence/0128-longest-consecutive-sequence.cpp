class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        std::unordered_set<int> numSet; 
        
        for (int num: nums) {
            numSet.insert(num);
        }
        
        int longestCount = 0; 
        for (int num: nums) {
            if (numSet.count(num - 1)) {
                continue; 
            } else {
                int count = 0; 
                while (numSet.count(num)) {
                    num++; 
                    count++;
                }
                longestCount = max(count, longestCount);
            }
        }
        
        return longestCount; 
    }
};