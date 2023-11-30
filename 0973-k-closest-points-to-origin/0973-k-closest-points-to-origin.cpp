struct element {
    int dist; 
    int i; 
};

class Solution {
public:
    static bool comp (element e1, element e2) {
        return e1.dist > e2.dist;
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        vector<element> heap; 
        vector<vector<int>> res;
        for(int i = 0; i < points.size(); i++) {
            int dist = pow(points[i][0], 2) + pow(points[i][1], 2);
            heap.push_back({dist, i});
        }
        make_heap(heap.begin(), heap.end(), comp);
        while (k--) {
            pop_heap(heap.begin(), heap.end(), comp); 
            element last = heap.back();
            res.push_back(points[last.i]);
            heap.pop_back();
        }
        return res;        
    }
};