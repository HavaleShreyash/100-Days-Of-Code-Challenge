class Solution:

    def rowWithMax1s(self,mat, R, C):
        max_row_index = -1  # Initialize with -1 for cases where there are no 1s
        max_ones = 0  # Keep track of maximum 1s found

        # Start from the top-right corner of the matrix
        row = 0
        col = C - 1

        while row < R and col >= 0:
            # If current element is 1, move left to find the leftmost 1 in this row
            if mat[row][col] == 1:
                col -= 1
                max_row_index = row
                max_ones += 1
            else:
                # Move to the next row
                row += 1

        if max_ones == 0:
            return -1  # If no 1s found, return -1

        return max_row_index


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(m)] for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                arr[i][j] = inputLine[i * m + j]
        ob = Solution()
        ans = ob.rowWithMax1s(arr, n, m)
        print(ans)
        tc -= 1