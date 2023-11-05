from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0  # If the list is empty, there are no unique elements.

        unique_count = 1  # Initialize the count of unique elements to 1, assuming the first element is unique.

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_count] = nums[i]
                unique_count += 1

        return unique_count

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 2]
    k = solution.removeDuplicates(nums)
    print(f"Output: {k}, nums = {nums[:k]}")

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = solution.removeDuplicates(nums)
    print(f"Output: {k}, nums = {nums[:k]}")
