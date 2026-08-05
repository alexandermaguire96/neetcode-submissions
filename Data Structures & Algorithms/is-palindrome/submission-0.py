class Solution:
    def isPalindrome(self, s: str) -> bool:
        #return true if palindrome ( racecar, mom)

        reverse = ""
        original = ""

        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                reverse += s[i]
            if s[i].isnumeric():
                reverse += s[i]

        for i in range(0, len(s),1):
            if s[i].isalpha():
                original += s[i]
            if s[i].isnumeric():
                original += s[i]


        print(reverse.lower())
        
        
        if reverse.lower() == original.lower():
            return True

        return False


