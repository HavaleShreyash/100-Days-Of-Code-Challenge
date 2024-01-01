class Solution:
    def lookandsay(self, n):
        if n == 1:
            return "1"  # Base case
        
        prev = "1"
        for i in range(2, n + 1):
            new_str = ""
            count = 1
            
            # Process the previous row to generate the current row
            for j in range(1, len(prev)):
                # If current digit is same as previous, increase count
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    new_str += str(count) + prev[j - 1]  # Append count and digit
                    count = 1  # Reset count for new digit
            
            # For the last digit in the previous row
            new_str += str(count) + prev[-1]
            
            prev = new_str  # Update previous row for the next iteration
        
        return prev

# Driver Code
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        solObj = Solution()
        print(solObj.lookandsay(n))
