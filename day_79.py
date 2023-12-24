from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Remove duplicates in-place in a sorted array such that each unique element appears at most twice.

        Args:
        - nums: A list of integers sorted in non-decreasing order.

        Returns:
        - int: The length of the modified array containing unique elements at most twice.
        """
        nextIdx = 0
        itemToRemove = None
        
        for num in nums:
            if num == itemToRemove:
                continue
            else:
                nums[nextIdx] = num
                if nextIdx > 0 and num == nums[nextIdx - 1]:
                    itemToRemove = num
                nextIdx += 1
        
        return nextIdx

# Example usage:
nums1 = [1, 1, 1, 2, 2, 3]
solution = Solution()
k = solution.removeDuplicates(nums1)
print(k)  # This will output the length of the modified array
print(nums1[:k])  # This will print the modified array with unique elements at most twice
