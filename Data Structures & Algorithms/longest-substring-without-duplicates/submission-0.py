class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        SS = set()
        l = 0
        length = 0

        for r in range(len(s)):
            while s[r] in SS:
                SS.remove(s[l])
                l += 1
            SS.add(s[r])
            length = max(length, r-l +1)

        return length
        