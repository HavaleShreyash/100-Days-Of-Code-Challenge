from typing import List

class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        def trim_number(num: str, trimi: int) -> int:
            return int(num[-trimi:])
        
        def find_kth_smallest(nums: List[str], ki: int, trimi: int) -> int:
            trimmed_nums = [trim_number(num, trimi) for num in nums]
            pq = sorted(range(len(nums)), key=lambda i: (trimmed_nums[i], i))
            return pq[ki - 1]

        answers = []
        for ki, trimi in queries:
            original_nums = nums.copy()
            smallest_index = find_kth_smallest(nums, ki, trimi)
            answers.append(smallest_index)
            nums = original_nums  
            
        return answers

if __name__ == "__main__":
    # Example usage:
    solution = Solution()
    nums = input("Enter the list of strings nums: ").split()
    num_of_queries = int(input("Enter the number of queries: "))
    queries = [list(map(int, input(f"Enter two elements for row {i+1}: ").split())) for i in range(num_of_queries)]
    print(solution.smallestTrimmedNumbers(nums, queries))


#Sample Input:
#Enter the list of strings nums: 100 200 300 400
#Enter the number of queries: 2
#Enter two elements for row 1: 2 0
#Enter two elements for row 2: 2 1