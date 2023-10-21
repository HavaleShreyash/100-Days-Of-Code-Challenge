def removeElement(nums, val):
    k = 0
    j = 0
    while j < len(nums):
        if nums[j] == val:
            nums.pop(j)
            k += 1
        else:
            j += 1

    return len(nums), nums

# Example usage:
nums = [3, 2, 2, 3]
val = 3
k, modified_nums = removeElement(nums, val)
print("Output:", k, "nums:", modified_nums)
