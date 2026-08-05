class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0
        maxFreq = 0
        window = defaultdict(int)

        for r in range(len(s)):

            # update information about s[r]
            window[s[r]] += 1
            maxFreq = max(maxFreq, window[s[r]])
            replacements = (r - l + 1) - maxFreq

            # while window is invalid:
            #     remove s[l]
            #     l += 1
            if replacements > k:
                window[s[l]] -= 1
                l += 1

                
            res = max(res, r - l + 1)

        return res