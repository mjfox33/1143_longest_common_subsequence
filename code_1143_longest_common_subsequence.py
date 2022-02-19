class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        dp = [ [0]*n2 for _ in range(n1)]
        for p1 in range(n1):
            for p2 in range(n2):
                if text1[p1] == text2[p2]:
                    if p1 == 0 or p2 == 0:
                        dp[p1][p2] = 1
                    else:
                        dp[p1][p2] = dp[p1-1][p2-1] + 1
                else:
                    if p1 == 0 and p2 == 0:
                        dp[p1][p2] = 0
                    elif p1 == 0 and p2 > 0:
                        dp[p1][p2] = dp[p1][p2-1]
                    elif p1>0 and p2 == 0:
                        dp[p1][p2] = dp[p1-1][p2]
                    else:
                        dp[p1][p2] = max(dp[p1-1][p2], dp[p1][p2-1])
        return min(n1,n2,max(max(dp)))
