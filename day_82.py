class Solution:
    
    def search(self, matrix, n, m, x):
        i = 0
        j = m - 1
    
        while i < n and j >= 0:
            if matrix[i][j] == x:  
                return True
    
            if j >= 0 and matrix[i][j] > x:
                j -= 1
            else:
                i += 1
    
        return False

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		size = input().strip().split()
		r = int(size[0])
		c = int(size[1])
		line = input().strip().split()
		matrix = [ [0 for _ in range(c)] for _ in range(r) ]
		for i in range(r):
			for j in range(c):
				matrix[i][j] = int( line[i*c+j] )
		target = int(input())
		obj = Solution()
		if (obj.search(matrix,r,c,target)): 
			print(1) 
		else: 
			print(0)