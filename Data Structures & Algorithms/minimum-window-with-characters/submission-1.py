from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(s) < len(t):
            return ""

        if s == t:
            return s
        
        l, r = 0,0
        
        dict_t = Counter(t)
        required = len(dict_t)
        formed = 0
        window_counts = {}
        min_len = float("inf")
        min_window = (None, None)

        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1

            if char in dict_t and window_counts[char] == dict_t[char]:
                formed += 1

            while l <= r and formed == required:
                char = s[l]

                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_window = (l,r)

                window_counts[char] -= 1
                if char in dict_t and window_counts[char] < dict_t[char]:
                    formed -= 1

                l += 1
            r += 1

        return "" if min_window[0] is None else s[min_window[0]: min_window[1] + 1]
