def romanToInt(s):
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in s[::-1]:  # Reverse the string and iterate from right to left
        value = roman_to_int[char]
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value

    return total

if __name__ == "__main__":
    # Test cases
    print(romanToInt("III"))       # Output: 3
    print(romanToInt("LVIII"))     # Output: 58
    print(romanToInt("MCMXCIV"))   # Output: 1994
