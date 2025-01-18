class Solution {
private:
    void dfs(int course, std::vector<std::vector<int>>& schedule, 
        std::vector<int>& state, std::vector<int>& order, bool& valid) {
            if (state[course] == 1) {
                valid = false;
                return;
            }

            if (state[course] == 2 || !valid) {
                return;
            }

            state[course] = 1;

            for (int other_course: schedule[course]) {
                dfs(other_course, schedule, state, order, valid);
                if (!valid) {
                    return;
                }
            }

            state[course] = 2;
            order.push_back(course);
    }
    
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<std::vector<int>> schedule(numCourses);
        for (auto prerequisite: prerequisites) {
            schedule[prerequisite[0]].push_back(prerequisite[1]);
        }

        std::vector<int> state(numCourses);
        std::vector<int> order;
        bool valid = true;
        
        for (int course = 0; course < numCourses; course++) {
            dfs(course, schedule, state, order, valid);
            if (!valid) {
                return {};
            }
        }

        return order;
    }
};