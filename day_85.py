class Solution:
    def maxArea(self,M, n, m):
        def max_histogram_area(hist):
            stack = []
            max_area = 0
            index = 0
    
            while index < len(hist):
                if not stack or hist[stack[-1]] <= hist[index]:
                    stack.append(index)
                    index += 1
                else:
                    top_of_stack = stack.pop()
                    area = (hist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                    max_area = max(max_area, area)
    
            while stack:
                top_of_stack = stack.pop()
                area = (hist[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
                max_area = max(max_area, area)
    
            return max_area

        histogram = [0] * m
        max_area = 0
    
        for i in range(n):
            for j in range(m):
                histogram[j] = histogram[j] + 1 if M[i][j] == 1 else 0
    
            max_area = max(max_area, max_histogram_area(histogram))
    
        return max_area


if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C = map(int, input().strip().split())
        A = []
        for i in range(R):
            line = [int(x) for x in input().strip().split()]
            A.append(line)
        print(Solution().maxArea(A, R, C)) 