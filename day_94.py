class Solution:
    def search(self, pat, txt):
        M = len(pat)
        N = len(txt)
        lps = [0] * M
        j = 0  # index for pat[]

        self.computeLPSArray(pat, M, lps)

        i = 0  # index for txt[]
        res = []
        while i < N:
            if pat[j] == txt[i]:
                i += 1
                j += 1

            if j == M:
                res.append(i - j + 1)
                j = lps[j - 1]

            # mismatch after j matches
            elif i < N and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        if not res:  # If no occurrences found
            return [-1]

        return res

    def computeLPSArray(self, pat, M, lps):
        len_longest_suffix = 0
        lps[0] = 0  # lps[0] is always 0
        i = 1

        while i < M:
            if pat[i] == pat[len_longest_suffix]:
                len_longest_suffix += 1
                lps[i] = len_longest_suffix
                i += 1
            else:
                if len_longest_suffix != 0:
                    len_longest_suffix = lps[len_longest_suffix - 1]
                else:
                    lps[i] = 0
                    i += 1

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if ans[0] == -1:  # If no occurrences found
            print(-1)
        else:
            for value in ans:
                print(value, end=' ')
            print()
