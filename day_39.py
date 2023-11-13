def buildArray(nums):
    n = len(nums)

    for i in range(n):
        nums[i] += (nums[nums[i]] % n) * n

    for i in range(n):
        nums[i] //= n

    return nums

if __name__ == "__main__":
    # Example 1
    nums1 = [0, 2, 1, 5, 3, 4]
    output1 = buildArray(nums1)
    print(output1)  # Output: [0, 1, 2, 4, 5, 3]

    # Example 2
    nums2 = [5, 0, 1, 2, 3, 4]
    output2 = buildArray(nums2)
    print(output2)  # Output: [4, 5, 0, 1, 2, 3]
