class Solution:
    def trappingWater(self, arr, n):
        left = 0
        right = n - 1

        l_max = 0
        r_max = 0

        result = 0
        while left <= right:
            if r_max <= l_max:
                result += max(0, r_max - arr[right])
                r_max = max(r_max, arr[right])
                right -= 1
            else:
                result += max(0, l_max - arr[left])
                l_max = max(l_max, arr[left])
                left += 1

        return result


def main():
    T = int(input("Enter the number of test cases: "))
    while T > 0:
        n = int(input("Enter the size of the array: "))
        arr = [int(x) for x in input("Enter the elements of the array separated by space: ").strip().split()]
        obj = Solution()
        print("Trapped water amount:", obj.trappingWater(arr, n))
        T -= 1


if __name__ == "__main__":
    main()
