from collections import Counter

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        count_charachters = Counter(s)
        s_vowels = []
        for charachters in count_charachters.keys():
            if charachters in vowels:
                s_vowels.append(charachters)                
                s = s.replace(charachters, '_')                              
        s_vowels.sort()
        for char in s_vowels:
            s = s.replace('_', char, count_charachters[charachters])
        return s
    
if __name__ == "__main__":
    solution = Solution()
    input_strings = ["lEetcOde", "lYmpH", "aAeEiIoOuU", "bcdfgh"]
    
    for s in input_strings:
        sorted_string = solution.sortVowels(s)
        print(f"Input: {s}, Output: {sorted_string}")