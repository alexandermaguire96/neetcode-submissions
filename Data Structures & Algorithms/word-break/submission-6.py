class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if dp[i]:
                string = ""
                for j in range(i, len(s)):
                    string += s[j]

                    
                    if string in wordDict:
                        dp[j+1] = True



        return dp[-1]

                

                