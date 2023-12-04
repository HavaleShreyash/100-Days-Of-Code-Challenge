class Solution:
    def merge_sorted_arrays(self, arr1, arr2, size_arr1, size_arr2):
        """
        Merges two sorted arrays in-place.

        Args:
        arr1 (list): First sorted array
        arr2 (list): Second sorted array
        size_arr1 (int): Size of arr1
        size_arr2 (int): Size of arr2

        Returns:
        None (modifies arr1 and arr2 in place)
        """
        # Initialize indices for arr1 and arr2
        index_arr1 = size_arr1 - 1
        index_arr2 = 0
        
        # Merge arr1 and arr2 in-place
        while index_arr1 >= 0 and index_arr2 < size_arr2:
            if arr1[index_arr1] >= arr2[index_arr2]:
                arr1[index_arr1], arr2[index_arr2] = arr2[index_arr2], arr1[index_arr1]
                index_arr1 -= 1
                index_arr2 += 1
            else:
                break
        
        # Sort both arrays separately
        arr1.sort()
        arr2.sort()


if __name__ == '__main__':
    test_cases = int(input())
    
    # Loop through each test case
    for _ in range(test_cases):
        # Input for the sizes of arrays size_arr1 and size_arr2
        size_arr1, size_arr2 = map(int, input().strip().split())
        
        # Input for elements of arr1 and arr2
        arr1 = list(map(int, input().strip().split()))
        arr2 = list(map(int, input().strip().split()))
        
        # Create an instance of the Solution class
        solution_obj = Solution()
        
        # Merge the arrays and print the modified arrays
        solution_obj.merge_sorted_arrays(arr1, arr2, size_arr1, size_arr2)
        print(*arr1, end=" ")
        print(*arr2)