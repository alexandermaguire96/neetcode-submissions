from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(Counter(t))
        print(Counter(s))
        return Counter(s) == Counter(t)
        