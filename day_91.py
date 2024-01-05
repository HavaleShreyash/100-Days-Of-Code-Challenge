class Solution:
    def find_permutation(self, S):
        def backtrack(curr, remaining):
            if not remaining:
                permutations.add(''.join(curr))
                return
            
            for i in range(len(remaining)):
                curr.append(remaining[i])
                backtrack(curr, remaining[:i] + remaining[i+1:])
                curr.pop()
        
        permutations = set()
        backtrack([], list(S))
        return sorted(list(permutations))


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()