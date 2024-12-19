class Solution {
public:
    bool isValid(string s) {
        std::unordered_map<char, char> brackets = {
            {'(', ')'}, 
            {'{', '}'}, 
            {'[', ']'}
        };
        std::stack<char> st;

        for (char c: s) {
            if (brackets.count(c)) {
                st.push(c);
            } else {
                if (st.empty() || brackets[st.top()] != c) {
                    return false;
                } 
                st.pop();
            }
        }

        return st.empty();
    }
};