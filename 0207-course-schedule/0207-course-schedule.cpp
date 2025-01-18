class Solution {
private:
    bool valid(int course, std::vector<std::vector<int>>& schedule, std::vector<bool>& visited) {
        if (visited[course]) {
            return false;
        }
        if (schedule[course].empty()) {
            return true;
        }

        visited[course] = true;
        for (auto other_course: schedule[course]) {
            if (!valid(other_course, schedule, visited)) { 
                return false;
            }
        }

        visited[course] = false;
        schedule[course] = {};
        return true;
    }

public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        std::vector<std::vector<int>> schedule(numCourses);
        for (auto prerequisite: prerequisites) {
            schedule[prerequisite[0]].push_back(prerequisite[1]);
        }

        std::vector<bool> visited(numCourses, false);
        for (int course = 0; course < numCourses; course++) {
            if (!valid(course, schedule, visited)) {
                return false;
            }
        }
        return true;
    }
};