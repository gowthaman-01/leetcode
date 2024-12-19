class Solution {
public:
    string minWindow(string s, string t) {
        std::unordered_map<char, int> s_map;
        std::unordered_map<char, int> t_map;

        for (char c: t) {
            t_map[c]++;
        }

        int cur = 0, needed = t_map.size();
        int l = 0, start = 0;
        int min_length = s.length() + 1;

        for (int r = 0; r < s.length(); r++) {
            if (!t_map.count(s[r])) {
                continue;
            }
  
            s_map[s[r]]++;
            if (s_map[s[r]] == t_map[s[r]]) {
                cur++;
                while (cur == needed) {
                    if (r - l + 1 < min_length) {
                        min_length = r - l + 1;
                        start = l;
                    }

                    if (t_map.count(s[l])) {
                        s_map[s[l]]--;
                        if (s_map[s[l]] < t_map[s[l]]) {
                            cur--;
                        }
                    }

                    l++;
                }
            }
            
        }

        return min_length <= s.length() 
               ? s.substr(start, min_length) 
               : "";
    }
};

