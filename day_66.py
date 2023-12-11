class Solution:
    def commonElements(self, A, B, C, n1, n2, n3):
        """
        Find the common elements in three sorted arrays.

        Args:
        A, B, C (list): Three sorted arrays.
        n1, n2, n3 (int): Sizes of arrays A, B, and C.

        Returns:
        list: An array containing the common elements in all three arrays, in sorted order.
              Returns an empty array if there are no common elements.
        """

        result = []  # To store common elements
        
        # Pointers for array traversal
        i, j, k = 0, 0, 0
        
        # Loop until any pointer reaches the end of its array
        while i < n1 and j < n2 and k < n3:
            # Check for common element
            if A[i] == B[j] == C[k]:
                # Avoid duplicates
                if not result or result[-1] != A[i]:
                    result.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        
        # If no common elements found, return empty array
        if not result:
            return []
        
        return result

# Driver code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n1, n2, n3 = list(map(int, input().split()))
        A = list(map(int, input().split()))
        B = list(map(int, input().split()))
        C = list(map(int, input().split()))
        
        ob = Solution()
        res = ob.commonElements(A, B, C, n1, n2, n3)
        
        if len(res) == 0:
            print(-1)
        else:
            for i in range(len(res)):
                print(res[i], end=" ")
            print()
