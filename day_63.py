class Solution:
    def inversionCount(self, arr, n):
        """
        Counts the number of inversions in an array.

        Args:
        - arr: Input array
        - n: Size of the array arr[]

        Returns:
        - Count of inversions in the array
        """
        return self._mergeSortAndCount(arr, 0, n - 1)
    
    def _mergeSortAndCount(self, arr, left, right):
        """
        Recursively divides the array and counts inversions during merging.

        Args:
        - arr: Input array
        - left: Left index
        - right: Right index

        Returns:
        - Count of inversions during merging
        """
        count = 0
        if left < right:
            mid = (left + right) // 2
            count += self._mergeSortAndCount(arr, left, mid)
            count += self._mergeSortAndCount(arr, mid + 1, right)
            count += self._mergeAndCount(arr, left, mid, right)
        return count
    
    def _mergeAndCount(self, arr, left, mid, right):
        """
        Merges the divided arrays and counts inversions.

        Args:
        - arr: Input array
        - left: Left index
        - mid: Middle index
        - right: Right index

        Returns:
        - Count of inversions during merging
        """
        left_array = arr[left:mid + 1]
        right_array = arr[mid + 1:right + 1]
        
        left_index, right_index, merged_index = 0, 0, left
        inversion_count = 0
        
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] <= right_array[right_index]:
                arr[merged_index] = left_array[left_index]
                left_index += 1
            else:
                arr[merged_index] = right_array[right_index]
                right_index += 1
                inversion_count += (mid + 1) - (left + left_index)
            merged_index += 1
        
        while left_index < len(left_array):
            arr[merged_index] = left_array[left_index]
            left_index += 1
            merged_index += 1
        
        while right_index < len(right_array):
            arr[merged_index] = right_array[right_index]
            right_index += 1
            merged_index += 1
        
        return inversion_count

if __name__ == '__main__':
    # Number of test cases
    num_test_cases = int(input())

    for _ in range(num_test_cases):
        # Size of the array
        array_size = int(input())
        
        # Input array
        input_array = list(map(int, input().strip().split()))
        
        # Creating an instance of the Solution class
        solution_obj = Solution()
        
        # Calculating and printing the count of inversions
        inversion_count = solution_obj.inversionCount(input_array, array_size)
        print(inversion_count)