class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "/" + s

        return encoded_string

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []
        pos = 0

        while pos < len(s):
            length_string = ""
            while s[pos] != "/":
                length_string += s[pos]
                pos += 1       
            length = int(length_string)
            pos += 1      
            decoded_strings.append(s[pos: pos + length])
            pos += length

        return decoded_strings
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))