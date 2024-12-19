class Codec {
public:

    // Encodes a list of strings to a single string.
    string encode(vector<string>& strs) {
        std::string encoded_string = "";
        for (const std::string& str: strs) {
            encoded_string.append(std::to_string(str.length()))
                          .append("/")
                          .append(str);
        }

        return encoded_string;
    }

    // Decodes a single string to a list of strings.
    vector<string> decode(string s) {
        std::vector<std::string> decoded_strings;
        size_t pos = 0;

        while (pos < s.size()) {
            size_t slash = s.find("/", pos);
            size_t string_length = std::stoi(s.substr(pos, slash - pos));
            decoded_strings.push_back(s.substr(slash + 1, string_length));
            pos = slash + string_length + 1;
        }

        return decoded_strings;
    }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));