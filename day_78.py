class Solution:
    def searchRange(self, nums, target):
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left - 1

        left = binarySearchLeft(nums, target)
        if left >= len(nums) or nums[left] != target:
            return [-1, -1]

        right = binarySearchRight(nums, target)
        return [left, right]

# Example usage:
nums1 = [5, 7, 7, 8, 8, 10]
target1 = 8
solution = Solution()
print(solution.searchRange(nums1, target1))  # Output: [3, 4]

nums2 = [5, 7, 7, 8, 8, 10]
target2 = 6
print(solution.searchRange(nums2, target2))  # Output: [-1, -1]

nums3 = []
target3 = 0
print(solution.searchRange(nums3, target3))  # Output: [-1, -1]
