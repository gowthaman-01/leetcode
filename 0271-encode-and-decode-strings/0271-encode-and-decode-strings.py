class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return "".join(f"{len(s)}/{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_strings = []
        pos = 0

        while pos < len(s):
            slash = s.find("/", pos)
            string_length = int(s[pos: slash])
            decoded_strings.append(s[slash + 1: slash + string_length + 1])
            pos = slash + string_length + 1
        
        return decoded_strings

        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))