class Solution:
    def nextPermutation(self, N, nums):
        """
        Rearranges the list of numbers into the lexicographically next greater permutation.
        If such arrangement is not possible, it sorts the list in ascending order.

        Args:
        - N (int): The size of the list.
        - nums (list): The list of numbers.

        Returns:
        - list: The next permutation.
        """
        def find_next_permutation(nums):
            size = len(nums)
            i = size - 2

            # Find the largest index i such that nums[i] < nums[i + 1]
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1

            # If no such index exists, return the reversed list
            if i < 0:
                return nums[::-1]

            j = size - 1
            # Find the largest index j such that nums[i] < nums[j]
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # Reverse the sublist nums[i+1:]
            nums[i + 1:] = nums[i + 1:][::-1]
            return nums

        return find_next_permutation(nums)

# Driver Code
if __name__ == '__main__':
    test_cases = int(input("Enter the number of test cases: "))
    for _ in range(test_cases):
        nums = list(map(int, input("Enter the numbers separated by space: ").split()))
        N = len(nums)

        obj = Solution()
        result = obj.nextPermutation(N, nums)
        for num in result:
            print(num, end=" ")
        print()
