class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        result = [''] * numRows
        index, step = 0, 1

        for char in s:
            result[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(result)

if __name__ == "__main__":
    solution = Solution()
    s1 = "PAYPALISHIRING"
    numRows1 = 3
    print(solution.convert(s1, numRows1))  # Output: "PAHNAPLSIIGYIR"

    s2 = "PAYPALISHIRING"
    numRows2 = 4
    print(solution.convert(s2, numRows2))  # Output: "PINALSIGYAHRPI"

    s3 = "A"
    numRows3 = 1
    print(solution.convert(s3, numRows3))  # Output: "A"
