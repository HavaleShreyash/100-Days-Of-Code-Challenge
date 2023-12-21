class Solution:

    def findMinDiff(self, A, N, M):
        if M == 0 or N == 0:
            return 0

        if N < M:
            return -1

        A.sort()  # Sort the array

        min_diff = float('inf')  # Initialize min_diff with a large value

        # Find the minimum difference by traversing through the sorted array
        for i in range(N - M + 1):
            min_diff = min(min_diff, A[i + M - 1] - A[i])

        return min_diff

# Driver code
if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    
    for _ in range(t):
        N = int(input("Enter size of array: "))
        A = [int(x) for x in input("Enter elements separated by space: ").split()]
        M = int(input("Enter number of students: "))

        solObj = Solution()
        print(solObj.findMinDiff(A, N, M))
