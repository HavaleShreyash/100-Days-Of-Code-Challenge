import math

class Solution:
    # Function to rearrange the array elements alternately.
    def rearrange(self, arr, n):
        # Store both max_elem and min_elem, these will be used as divisors and multipliers
        max_idx = n - 1
        min_idx = 0
        max_elem = arr[max_idx] + 1  # Use max_elem as a temporary storage
        
        # Traverse the array and store both max and min elements at their respective positions
        for i in range(n):
            # If the current index is even, store the maximum element
            if i % 2 == 0:
                arr[i] += (arr[max_idx] % max_elem) * max_elem
                max_idx -= 1
            # If the current index is odd, store the minimum element
            else:
                arr[i] += (arr[min_idx] % max_elem) * max_elem
                min_idx += 1
        
        # Update the array elements with their new values
        for i in range(n):
            arr[i] = arr[i] // max_elem  # Retrieve the stored values by dividing with max_elem


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()