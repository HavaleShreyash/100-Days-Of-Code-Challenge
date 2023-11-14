class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        data = (s.strip()).split(" ")
        return(len(data[-1]))
    
if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))
    print(s.lengthOfLastWord("   fly me   to   the moon  "))