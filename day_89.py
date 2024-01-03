class Solution:
    def longestPalin(self, S):
        """
        Finds the longest palindromic substring within a given string S.

        Args:
        - S (str): The input string.

        Returns:
        - str: The longest palindromic substring found in S.
        """

        start = 0
        end = 0
        
        for i in range(len(S)):
            # odd part
            low = i - 1
            high = i
            while low >= 0 and high < len(S) and S[low] == S[high]:
                if high - low + 1 > end:
                    end = high - low + 1
                    start = low
                low -= 1
                high += 1
            
            # Even part
            low = i - 1
            high = i + 1
            while low >= 0 and high < len(S) and S[low] == S[high]:
                if high - low + 1 > end:
                    end = high - low + 1
                    start = low
                low -= 1
                high += 1
        
        if end == 0:
            return S[start:start + 1]
        return S[start:start + end]
  

if __name__ == '__main__':
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        S = input("Enter the string: ")

        ob = Solution()

        ans = ob.longestPalin(S)

        print("Longest palindromic substring:", ans)
