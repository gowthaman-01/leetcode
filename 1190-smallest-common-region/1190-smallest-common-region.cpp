struct Region {
    string name = "";
    string bigger = "";
};

class Solution {
public:
    string findSmallestRegion(vector<vector<string>>& regions, string region1, string region2) {
        unordered_map<string, Region>map; 
        for (vector<string> regionList: regions) {
            string biggerRegionName = regionList[0];
            Region biggerRegion; 
            if (map.count(biggerRegionName)) {
                biggerRegion = map[biggerRegionName];
            } else {
                biggerRegion.name = biggerRegionName;
                map[biggerRegionName] = biggerRegion;
            }
            for (int i = 1; i < regionList.size(); i++) {
                string smallerRegionName = regionList[i]; 
                Region smallerRegion; 
                if (map.count(smallerRegionName)) {
                    smallerRegion = map[smallerRegionName];
                } else {
                    smallerRegion.name = smallerRegionName; 
                }
                smallerRegion.bigger = biggerRegionName;
                map[smallerRegionName] = smallerRegion; 
            }
        }

        unordered_set<string>visited;
        Region r1 = map[region1]; Region r2 = map[region2]; 
        visited.insert(r1.name); 
        visited.insert(r2.name);
        while (true) {
            if (map.count(r1.bigger)) {
                r1 = map[r1.bigger];
                if (visited.count(r1.name)) return r1.name; 
                visited.insert(r1.name); 
            }
            if (map.count(r2.bigger)) {
                r2 = map[r2.bigger]; 
                if (visited.count(r2.name)) return r2.name; 
                visited.insert(r2.name);
            }
        }
        return "";
    }
};