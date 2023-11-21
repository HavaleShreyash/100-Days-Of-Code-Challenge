class Solution:
    def sortColors(self, nums):
        left = 0  # pointer for the red section
        right = len(nums) - 1  # pointer for the blue section
        i = 0  # pointer for iteration

        while i <= right:
            if nums[i] == 0:  # red color
                nums[i], nums[left] = nums[left], nums[i]
                left += 1
                i += 1
            elif nums[i] == 2:  # blue color
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            else:  # white color
                i += 1

if __name__ == "__main__":
    # Test cases
    solution = Solution()
    
    nums1 = [2, 0, 2, 1, 1, 0]
    solution.sortColors(nums1)
    print(nums1)  # Output: [0, 0, 1, 1, 2, 2]
    
    nums2 = [2, 0, 1]
    solution.sortColors(nums2)
    print(nums2)  # Output: [0, 1, 2]