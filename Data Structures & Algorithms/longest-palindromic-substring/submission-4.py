class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(start, longest):
            if start > len(s):
                return longest
            string = ""
            for i in range(start, len(s)):
                string += s[i]
                string_reverse = string[::-1]
                if string == string_reverse:
                    if len(string) > len(longest):
                        longest = string
                    print(longest)
            longest = isPalindrom(start+1, longest)

            return longest

        longest = isPalindrom(0, "")
        return longest

                

