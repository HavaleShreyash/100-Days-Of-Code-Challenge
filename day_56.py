class Solution:
    def find_minimum_multiplications(self, given_number: int, multiplier: int) -> int:
        """
        Finds the minimum number of times 'multiplier' needs to be multiplied by integers from 1 to 10
        such that the last digit of the product matches the last digit of a given number 'given_number'.

        Args:
        given_number (int): The given number.
        multiplier (int): The value to be multiplied.

        Returns:
        int: The minimum number of times 'multiplier' needs to be multiplied, or -1 if not found.
        """
        if given_number == 0:
            return 0
        for i in range(1, 11):
            if (i * multiplier) % 10 == given_number % 10:
                return i
        return -1

if __name__ == "__main__":
    user_input_number = int(input("Enter the number: "))
    user_input_multiplier = int(input("Enter the value to be multiplied: "))

    solution = Solution()
    result = solution.find_minimum_multiplications(user_input_number, user_input_multiplier)

    print(result)

#Sample Input and output:
# Enter the number: 56
# Enter the value to be multiplied: 7
# 2