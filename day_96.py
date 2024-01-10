class Solution:
    def computeLPSArray(self, pat):
        length = 0
        lps = [0] * len(pat)
        i = 1

        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def lps(self, s):
        lps_arr = self.computeLPSArray(s)
        n = len(s)
        return lps_arr[n - 1] if n > 0 else 0

# Driver Code
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ob = Solution()
        answer = ob.lps(s)
        print(answer)
