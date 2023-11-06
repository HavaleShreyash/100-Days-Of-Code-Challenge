class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1

        return right  # When left > right, return right as the floor of the square root

if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    print(solution.mySqrt(4))  # Output: 2
    print(solution.mySqrt(8))  # Output: 2
