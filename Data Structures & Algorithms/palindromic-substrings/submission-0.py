class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        res = 0

        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            res += 1

        for i in range(0, n):
            for j in range(0, i):
                if s[i] == s[j]:
                    if (i-j == 1):
                        dp[i][j] = True
                        res += 1


                    elif dp[i-1][j+1] == True:
                        dp[i][j] = True
                        res += 1

        
        return res
                    
                    
        
