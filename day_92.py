# import sys

class Solution:
    def square(self, n):
        return n * n

    def solveWordWrapUtil(self, words, n, length, wordIndex, remLength, memo):
        if wordIndex == n - 1:
            memo[wordIndex][remLength] = 0 if words[wordIndex] < remLength else self.square(remLength)
            return memo[wordIndex][remLength]

        currWord = words[wordIndex]

        if currWord < remLength:
            return min(
                self.solveWordWrapUsingMemo(words, n, length, wordIndex + 1,
                                            remLength - currWord if remLength == length else remLength - currWord - 1,
                                            memo),
                self.square(remLength) +
                self.solveWordWrapUsingMemo(words, n, length, wordIndex + 1,
                                            length - currWord, memo))

        else:
            return (self.square(remLength) +
                    self.solveWordWrapUsingMemo(words, n, length, wordIndex + 1,
                                                length - currWord, memo))

    def solveWordWrapUsingMemo(self, words, n, length, wordIndex, remLength, memo):
        if memo[wordIndex][remLength] != -1:
            return memo[wordIndex][remLength]

        memo[wordIndex][remLength] = self.solveWordWrapUtil(words, n, length, wordIndex, remLength, memo)
        return memo[wordIndex][remLength]

    def solveWordWrap(self, words, k):
        n = len(words)
        memo = [[-1] * (k + 1) for _ in range(n)]
        return self.solveWordWrapUsingMemo(words, n, k, 0, k, memo)
        
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		k = int(input())
		obj = Solution()
		ans = obj.solveWordWrap(nums, k)
		print(ans)