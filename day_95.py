def wordBreak(line, dictionary):
    n = len(line)
    # Create a DP array to store if a prefix ending at index i can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string can always be segmented
    
    for i in range(1, n + 1):
        for j in range(i):
            # Check if the prefix up to index j is a valid word and the suffix from j to i is also valid
            if dp[j] and line[j:i] in dictionary:
                dp[i] = True
                break

    return dp[n]

# Driver Code
if __name__ == '__main__':
    test_case = int(input())

    for _ in range(test_case):
        number_of_elements = int(input())
        dictionary = [word for word in input().strip().split()]
        line = input().strip()
        res = wordBreak(line, dictionary)
        if res:
            print(1)
        else:
            print(0)
