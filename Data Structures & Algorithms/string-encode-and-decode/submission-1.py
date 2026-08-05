class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""

        for word in strs:
            wordlength = len(word)
            string += str(wordlength)+ "#" + word

        print(string)
        return string

        

    def decode(self, s: str) -> List[str]:
        string = list()

        i = 0

        while i < len(s):
            stringLength = ""
            substring = ""


            while i < len(s):
                if s[i] == '#':
                    i += 1
                    break
                stringLength += s[i]
                i += 1
            print("hihi",stringLength)
            intLength = int(stringLength)
            substring = s[i: i+intLength]
            string.append(substring)

            i += intLength

        return string
