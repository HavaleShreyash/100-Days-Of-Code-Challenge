from bisect import bisect_right as upper_bound

class Solution:
    def median(self, m, r, d):
        mi = m[0][0]
        mx = 0
        for i in range(r):
            if m[i][0] < mi:
                mi = m[i][0]
            if m[i][d-1] > mx :
                mx =  m[i][d-1]
            
        desired = (r * d + 1) // 2
            
        while (mi < mx):
            mid = mi + (mx - mi) // 2
            place = [0]
                
            # Find count of elements smaller than or equal to mid
            for i in range(r):
                    j = upper_bound(m[i], mid)
                    place[0] = place[0] + j
            if place[0] < desired:
                mi = mid + 1
            else:
                mx = mid

        return mi 


if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        r,c = map(int,input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        for i in range(r):
            t=[int(el) for el in input().split()]
            for j in range(c):
                matrix[i][j]=t[j]
        ans = ob.median(matrix, r, c);
        print(ans)