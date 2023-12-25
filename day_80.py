class Solution:
    def spirallyTraverse(self, matrix, r, c):
        spiral_order = []
        top_row, bottom_row = 0, r - 1
        left_col, right_col = 0, c - 1
        
        while top_row <= bottom_row and left_col <= right_col:
            # Traverse from left to right
            for i in range(left_col, right_col + 1):
                spiral_order.append(matrix[top_row][i])
            top_row += 1
            
            # Traverse from top to bottom
            for i in range(top_row, bottom_row + 1):
                spiral_order.append(matrix[i][right_col])
            right_col -= 1
            
            # Ensure it's not the same row
            if top_row <= bottom_row:
                # Traverse from right to left
                for i in range(right_col, left_col - 1, -1):
                    spiral_order.append(matrix[bottom_row][i])
                bottom_row -= 1
            
            # Ensure it's not the same column
            if left_col <= right_col:
                # Traverse from bottom to top
                for i in range(bottom_row, top_row - 1, -1):
                    spiral_order.append(matrix[i][left_col])
                left_col += 1
        
        return spiral_order

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix = []
        for i in range(r):
            row = []
            for j in range(c):
                row.append(values[k])
                k += 1
            matrix.append(row)
        
        obj = Solution()
        ans = obj.spirallyTraverse(matrix, r, c)
        for i in ans:
            print(i, end=" ")
        print()
