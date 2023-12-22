from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic(sub_arr):
            sub_arr.sort()
            diff = sub_arr[1] - sub_arr[0]
            for i in range(2, len(sub_arr)):
                if sub_arr[i] - sub_arr[i - 1] != diff:
                    return False
            return True
        
        result = []
        for i in range(len(l)):
            sub_array = nums[l[i]: r[i] + 1]
            result.append(is_arithmetic(sub_array))
        
        return result

# Example usage
solution = Solution()
nums1 = [4, 6, 5, 9, 3, 7]
l1 = [0, 0, 2]
r1 = [2, 3, 5]
print(solution.checkArithmeticSubarrays(nums1, l1, r1))  # Output: [True, False, True]

nums2 = [-12, -9, -3, -12, -6, 15, 20, -25, -20, -15, -10]
l2 = [0, 1, 6, 4, 8, 7]
r2 = [4, 4, 9, 7, 9, 10]
print(solution.checkArithmeticSubarrays(nums2, l2, r2))  # Output: [False, True, False, False, True, True]
