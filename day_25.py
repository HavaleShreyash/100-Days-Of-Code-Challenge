
from typing import List

class Solution:
    def r(self,n,ij,ji,j,i):
        if i==n:
            return 1
        ans=0
        for e in range(n):
            if j[e] or ij[i+e] or ji[i-e]:
                continue
            ij[i+e]=1
            ji[i-e]=1
            j[e]=1
            ans=ans+self.r(n,ij,ji,j,i+1)
            ij[i+e]=0
            ji[i-e]=0
            j[e]=0
        return ans
        
    def totalNQueens(self, n: int) -> List[List[str]]:
        ans=self.r(n,[0]*2*n,[0]*2*n,[0]*n,0)
        return ans
        

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    print(solution.totalNQueens(4))  # Output: 2
    print(solution.totalNQueens(1))  # Output: 1
