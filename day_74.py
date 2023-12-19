class Solution:
     
    #Function to find if there exists a triplet in the 
    #array A[] which sums up to 'sum'.
    def find3Numbers(self,A, arr_size, sum):
 
        A.sort()
        for i in range(0, arr_size-2):
         

            l = i + 1
             
            r = arr_size-1
            while (l < r):
             
                if( A[i] + A[l] + A[r] == sum):
                    return True
                 
                elif (A[i] + A[l] + A[r] < sum):
                    l += 1
                else: 
                    r -= 1
     
        return False


import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,X=map(int,input().strip().split())
        A=list(map(int,input().strip().split()))
        ob=Solution()
        if(ob.find3Numbers(A,n,X)):
            print(1)
        else:
            print(0)