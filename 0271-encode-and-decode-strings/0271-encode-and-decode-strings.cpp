class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        std::string encodedString = "";
        for (string& str: strs) {
            encodedString += std::to_string(str.length()) + "/" + str;
        }
        return encodedString;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        int pos = 0;
        std::vector<string> decodedStrs;
        
        while (pos < s.length()) {
            std::string lengthString = "";
            while (s[pos] != '/') {
                lengthString += s[pos++];
            }
            int length = std::stoi(lengthString);
            pos++;
            
            std::string decodedStr = "";
            while (length--) {
                decodedStr += s[pos++];
            }
            
            decodedStrs.push_back(decodedStr);
        }
        
        return decodedStrs;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));