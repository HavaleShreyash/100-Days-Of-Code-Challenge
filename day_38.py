class Solution:
    def spiralOrder(self, matrix):
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    result.append(row.pop(0))
        return result


if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))  # Output: [1,2,3,6,9,8,7,4,5]
    print(solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
