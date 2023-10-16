from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Find the shortest string in the array
        shortest_str = min(strs, key=len)

        for i, char in enumerate(shortest_str):
            for string in strs:
                if string[i] != char:
                    return shortest_str[:i]

        return shortest_str

if __name__ == "__main__":
    strs1 = ["flower", "flow", "flight"]
    solution1 = Solution()
    print(solution1.longestCommonPrefix(strs1))  

    strs2 = ["dog", "racecar", "car"]
    solution2 = Solution()
    print(solution2.longestCommonPrefix(strs2))  