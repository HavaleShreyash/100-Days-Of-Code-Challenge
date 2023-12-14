class Solution:
    def factorial(self, N):
        """
        Calculate the factorial of a number N and return the digits in a list.

        Args:
        - N (int): Input number to calculate factorial

        Returns:
        - list: List of digits representing the factorial of N
        """

        # Initialize the result with 1 digit (as 1! = 1)
        ans = [1]

        # Calculate factorial
        for i in range(2, N + 1):
            carry = 0
            # Multiply each digit of the result with the current number and maintain carry
            for j in range(len(ans)):
                res = i * ans[j] + carry
                ans[j] = res % 10 # Store the last digit in the current position
                carry = res // 10 # Update carry for next iteration
            
            # Add remaining carry digits
            while carry != 0:
                ans.append(carry % 10) # Reverse the list to get the correct factorial representation
                carry //= 10
        
        ans.reverse()
        return ans

if __name__ == '__main__':
    t = int(input("Enter number of test cases: "))
    for _ in range(t):
        N = int(input("Enter value of N: "))
        ob = Solution()
        ans = ob.factorial(N)
        for digit in ans:
            print(digit, end="")
        print()