def maximize_subsequences(text, pattern):
    if not text or not pattern:
        return 0

    dp = [[0] * (len(text) + 1) for _ in range(len(pattern) + 1)]

    for i in range(1, len(pattern) + 1):
        for j in range(1, len(text) + 1):
            dp[i][j] = dp[i][j - 1]
            if pattern[i - 1] == text[j - 1]:
                dp[i][j] += dp[i - 1][j - 1] + 1

    return dp[-1][-1]

def main():
    text = input().strip()
    pattern = input().strip()

    result = maximize_subsequences(text, pattern)
    print(result)

if __name__ == "__main__":
    main()

# Input for text: abcdabcd
# Input for pattern: abd
