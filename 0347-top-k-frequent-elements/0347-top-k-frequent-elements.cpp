class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freqMap; 
        std::vector<int> uniqueNums; 
        
        for (int num: nums) {
            if (!freqMap.count(num)) {
                uniqueNums.push_back(num);
            }
            freqMap[num]++;
        }
        
        // Quick select
        int swapIndex = 0; 
        int currentIndex = 0; 
        int pivotIndex = uniqueNums.size() - 1;
        
        while (true) {
            while (currentIndex < pivotIndex) {
                if (freqMap[uniqueNums[currentIndex]] <= freqMap[uniqueNums[pivotIndex]]) {
                    std::swap(uniqueNums[currentIndex], uniqueNums[swapIndex++]); 
                } 
                currentIndex++;
            }         
            std::swap(uniqueNums[pivotIndex], uniqueNums[swapIndex]);
            if (swapIndex == uniqueNums.size() - k) { 
                return std::vector<int>(uniqueNums.begin() + swapIndex, uniqueNums.end());
            } else if (swapIndex > uniqueNums.size() - k) {
                currentIndex = 0;
                pivotIndex = swapIndex - 1;
                swapIndex = 0;
            } else {
                currentIndex = swapIndex + 1;
                int pivotIndex = uniqueNums.size() - 1;
                swapIndex++;
            }
        }

        // Code should never reach here
        return {}
    }
};
