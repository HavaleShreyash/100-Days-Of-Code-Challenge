class Solution:
    def editDistance(self, s, t):
        m, n = len(s), len(t)
        
        # Creating a dp table to store the minimum operations required
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Filling the dp table based on the lengths of s and t
        for i in range(m + 1):
            for j in range(n + 1):
                # If s is empty, the only option is to insert all characters of t
                if i == 0:
                    dp[i][j] = j
                # If t is empty, the only option is to remove all characters of s
                elif j == 0:
                    dp[i][j] = i
                # If characters match, no operation needed, move to the previous characters
                elif s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # If characters don't match, consider all operations (insert, remove, replace)
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1],    # Insert
                                       dp[i - 1][j],    # Remove
                                       dp[i - 1][j - 1] # Replace
                                       )
        
        return dp[m][n]

if __name__ == '__main__':
    T = int(input("Enter the number of test cases: "))
    for _ in range(T):
        s, t = input().split()
        ob = Solution()
        ans = ob.editDistance(s, t)
        print(ans)
