class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), [](vector<int> v1, vector<int> v2) {
            return v1[0] < v2[0];
        });
        int s = intervals[0][0];
        int e = intervals[0][1];
        vector<vector<int>> res;
        for (int i = 1; i < intervals.size(); i++) {
            int ns = intervals[i][0];
            int ne = intervals[i][1];
            if (ns > e) {
                res.push_back({s, e});
                s = ns; 
            } 
            e = max(e, ne);
        }
        res.push_back({s, e});
        return res;
    }
};