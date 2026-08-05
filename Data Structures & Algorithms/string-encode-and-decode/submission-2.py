class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded = ""

        for s in strs:
            encoded += s + "?"
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        string = ""
        
        for c in s:

            if c == "?":
                decoded.append(string)
                print(string)
                string = ""
            else:
                string += c
        return decoded

