class Codec {
public:
    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        std::string encoded_string = "";
        for (std::string& str: strs) {
            encoded_string += std::to_string(str.length()) + "/" + str;
        }

        return encoded_string;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        std::vector<std::string> decoded_strings;   
        size_t pos = 0;
        
        while (pos < s.length()) {
            std::string length_string = "";
            while (s[pos] != '/') {
                length_string += s[pos++];
            }
            int length = std::stoi(length_string);
            pos++;

            std::string str = "";
            while (length--) {
                str += s[pos++];
            }
            decoded_strings.push_back(str);
        }
    
        return decoded_strings;  
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));