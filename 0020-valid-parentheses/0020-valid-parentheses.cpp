class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> bracketMap = {{'{', '}'}, {'(', ')'}, {'[', ']'}};
        std::stack<char> st;
        
        for (char c: s) {
            if (bracketMap.count(c)) {
                st.push(c);
            } else {
                if (st.empty()) {
                    return false;
                } 
                char top = st.top();
                st.pop();
                if (bracketMap[top] != c) {
                    return false;
                }
            }
        }
        
        return st.empty();
    }
};