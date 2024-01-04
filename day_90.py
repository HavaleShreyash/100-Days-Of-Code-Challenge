class Solution:
    def LongestRepeatingSubsequence(self, str):
        n = len(str)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if str[i - 1] == str[j - 1] and i != j:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]

# Driver code
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        str_input = input()
        ob = Solution()
        ans = ob.LongestRepeatingSubsequence(str_input)
        print(ans)
