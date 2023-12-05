class Solution:
    def maxSubArraySum(self, nums, size):
        """
        Finds the sum of the contiguous subarray with the maximum sum.
        
        Args:
        nums (list): The input list of integers.
        size (int): The size of the input list.
        
        Returns:
        int: The sum of the contiguous subarray with the maximum sum.
        """

        max_sum = nums[0]  # Initialize the maximum sum with the first element
        current_sum = nums[0]  # Initialize current sum with the first element

        # Traverse through the array starting from the second element
        for i in range(1, size):
            # Update current sum by choosing between the current element and the sum so far
            current_sum = max(nums[i], current_sum + nums[i])

            # Update the maximum sum if the current sum becomes larger
            max_sum = max(max_sum, current_sum)

        return max_sum

def main():
    test_cases = int(input("Enter the number of test cases: "))
    while test_cases > 0:
        size = int(input("Enter the size of the array: "))
        nums = list(map(int, input("Enter space-separated array elements: ").split()))

        solution_obj = Solution()
        max_subarray_sum = solution_obj.maxSubArraySum(nums, size)

        print("Maximum Subarray Sum:", max_subarray_sum)

        test_cases -= 1

if __name__ == "__main__":
    main()