class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for word in strs:
            encoded_string += str(len(word)) + "#" + word

        return encoded_string

        
    # decoded_strs = decode(encoded_string);
    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []

        while i < len(s):
            j = i

            # find the separator
            while s[j] != "#":
                j += 1
                # pointer at #

            length = int(s[i:j])

            #length#
            word = s[j+1 : j+1 + length]
            decoded_strs.append(word)
            i = j + 1 + length
            
        return decoded_strs;
