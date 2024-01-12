class Solution:
    # Your task is to complete this function
    # Function should return an integer
    def countPS(self,string):
        mod = 1000000007
        n = len(string)

        # dp[i][j] stores the count of palindromic subsequences in the substring s[i:j+1]
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1  # Single characters are palindromic

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if string[i] == string[j]:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] + 1) % mod
                else:
                    dp[i][j] = (dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]) % mod

                dp[i][j] = (dp[i][j] + mod) % mod  # Ensure the result is non-negative

        return dp[0][n - 1]




import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        ob=Solution()
        print(ob.countPS(input().strip()))