from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Initialize the carry to 1 since we want to add one.
        carry = 1
        result = []

        # Iterate over the digits from right to left.
        for i in range(len(digits) - 1, -1, -1):
            # Calculate the new digit by adding the current digit and the carry.
            new_digit = digits[i] + carry
            # Update the carry for the next iteration.
            carry = new_digit // 10
            # Update the new digit to be the remainder after dividing by 10.
            new_digit %= 10
            # Insert the new digit at the beginning of the result list.
            result.insert(0, new_digit)

        # If there is still a carry left after all iterations, insert it at the beginning.
        if carry:
            result.insert(0, carry)

        return result

if __name__ == "__main__":
    solution = Solution()
    digits1 = [1, 2, 3]
    print(solution.plusOne(digits1))  # Output: [1, 2, 4]

    digits2 = [4, 3, 2, 1]
    print(solution.plusOne(digits2))  # Output: [4, 3, 2, 2]

    digits3 = [9]
    print(solution.plusOne(digits3))  # Output: [1, 0]
