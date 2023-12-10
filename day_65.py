class Solution:
    def getPairsCount(self, arr, size, target):
        """
        Function to count pairs in an array with a given sum.

        Args:
        arr: List[int] - Input array.
        size: int - Size of the array.
        target: int - Target sum to find pairs.

        Returns:
        int: Count of pairs that sum up to the given target.
        """
        # Create a dictionary to store the frequency of elements
        element_count = {}
        pair_count = 0
        
        # Traverse through the array
        for i in range(size):
            # Check if the complement for the current element exists in the dictionary
            complement = target - arr[i]
            if complement in element_count:
                # Increment the count by the frequency of the complement
                pair_count += element_count[complement]
                
            # Update the count of the current element in the dictionary
            if arr[i] in element_count:
                element_count[arr[i]] += 1
            else:
                element_count[arr[i]] = 1
        
        return pair_count

# Driver Code
if __name__ == '__main__':
    test_cases = int(input())
    while test_cases > 0:
        size, target = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        solver = Solution()
        result = solver.getPairsCount(arr, size, target)
        print(result)
        test_cases -= 1