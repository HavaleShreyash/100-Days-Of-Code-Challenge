class Solution:
    def intToRoman(self, num: int) -> str:
        # Create a dictionary to map Roman numeral symbols to their values.
        roman_numerals = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        # Sort the values in descending order.
        values = sorted(roman_numerals.keys(), reverse=True)
        
        # Initialize an empty string to build the Roman numeral.
        result = ""
        
        # Iterate through the values and construct the Roman numeral.
        for value in values:
            while num >= value:
                result += roman_numerals[value]
                num -= value
        
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.intToRoman(3))  # Output: "III"
    print(solution.intToRoman(58))  # Output: "LVIII"
    print(solution.intToRoman(1994))  # Output: "MCMXCIV"
