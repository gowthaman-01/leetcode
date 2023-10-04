class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> map({{'(', ')'}, {'[', ']'}, {'{', '}'}});
        stack<char> st; 
        for (char c: s) {
            if (map.count(c)) {
                st.push(c);
            } else {
                if (!st.size() || c != map[st.top()]) {
                    return false; 
                }
                st.pop();
            }
        }
        return !st.size();
    }
};