from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Define a dictionary mapping digits to letters
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def dfs(current, next_digits):
            # If there are no more digits to process, add the current combination to the result
            if not next_digits:
                result.append(current)
                return

            # Get the letters corresponding to the next digit
            letters = digit_to_letters[next_digits[0]]

            # Explore all possible combinations with the next digit's letters
            for letter in letters:
                dfs(current + letter, next_digits[1:])

        result = []
        dfs("", digits)
        return result

if __name__ == "__main__":
    solution = Solution()
    digits = "23"
    result = solution.letterCombinations(digits)
    print(result)
