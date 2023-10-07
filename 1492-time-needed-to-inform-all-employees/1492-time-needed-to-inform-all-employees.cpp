class Solution {
public:
    int numOfMinutes(int n, int headID, vector<int>& manager, vector<int>& informTime) {
        unordered_map<int, vector<int>> managerToEmployee; 
        for (int i = 0; i < n; i++) {
            if (i == headID) continue;
            managerToEmployee[manager[i]].push_back(i);
        }
        queue<pair<int, int>> q({{headID, 0}});
        int minutes = 0; 
        while (!q.empty()) {
            pair<int, int> currentManagerPair = q.front();
            int currentManager = currentManagerPair.first; 
            int currentTime = currentManagerPair.second;
            q.pop(); 
            for (int employee: managerToEmployee[currentManager]) {
                int newTime = currentTime + informTime[currentManager]; 
                q.push({employee, newTime});
                minutes = max(minutes, newTime);
            }
        }
        return minutes;
    }
};