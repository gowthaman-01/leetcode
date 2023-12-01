class Solution {
public:
    int hIndex(vector<int>& citations) {
        int l = 0; 
        for (int c: citations) {
            l = max(c, l);
        }
        vector<int> bucket(l + 1, 0); 
        for (int c: citations) {
            bucket[c]++;
        }
        int count = citations.size(); 
        int res = 0;
        for (int i = 0; i < l + 1; i++) {
            res = max(res, min(count, i));
            count -= bucket[i];
        }
        return res;
    }
};