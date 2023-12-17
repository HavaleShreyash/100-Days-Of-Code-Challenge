class Solution:
    def maxProfit(self, K, N, A):
        """
        Calculates the maximum profit that can be obtained by performing at most K transactions
        on a given list of stock prices.

        Args:
        - K (int): Maximum number of transactions allowed
        - N (int): Number of stock prices in the list
        - A (list): List containing stock prices

        Returns:
        - int: Maximum profit achievable
        """
        if not A or N < 2:
            return 0

        if K >= N // 2:
            max_profit = 0
            for i in range(1, N):
                if A[i] > A[i - 1]:
                    max_profit += A[i] - A[i - 1]
            return max_profit

        dp = [[0] * N for _ in range(K + 1)]

        for k in range(1, K + 1):
            max_diff = -A[0]
            for j in range(1, N):
                dp[k][j] = max(dp[k][j - 1], A[j] + max_diff)
                max_diff = max(max_diff, dp[k - 1][j] - A[j])

        return dp[K][N - 1]


# Driver Code
if __name__ == '__main__':
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        K = int(input("Enter the maximum number of transactions allowed: "))
        N = int(input("Enter the number of stock prices: "))
        A = input("Enter the stock prices separated by space: ").split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print("Maximum profit:", ob.maxProfit(K, N, A))
