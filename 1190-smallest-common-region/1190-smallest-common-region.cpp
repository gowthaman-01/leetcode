class Solution {
public:
    string findSmallestRegion(vector<vector<string>>& regions, string region1, string region2) {
        unordered_map<string, string> map; 
        for (vector<string> rList: regions) {
            for (int i = 1; i < rList.size(); i++) {
                map[rList[i]] = rList[0];
            }
        }
        unordered_set<string>bigger; 
        while(region1 != "") {
            bigger.insert(region1); 
            region1 = map[region1];
        } 
        while(!bigger.count(region2)) {
            region2 = map[region2];
        }
        return region2; 
    }
};