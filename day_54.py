# Code that finds the maximum length of a subarray with equal number of 0s and 1s
import sys

def findMaxLength(nums):
    count = 0
    maximum_length = 0
    count_dictionary = {0: -1}
    for i in range(len(nums)):
        if nums[i] == 0:
            count -=1
        else:
            count +=1

        if count in count_dictionary:
            maximum_length = max(maximum_length, i - count_dictionary[count])
        else:
            count_dictionary[count] = i

    return maximum_length

if __name__ == "__main__":
    input_str = input("Enter a string:")
    nums = [int(bit) for bit in input_str]

    result = findMaxLength(nums)
    print(result)