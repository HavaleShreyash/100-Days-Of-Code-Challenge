class Solution:
    def findOccurrence(self, mat, target):
        """
        Count the number of occurrences of the given target word in a 2D matrix.

        Parameters:
        - mat (list of lists): N*M 2D array of characters.
        - target (str): Target word to search for.

        Returns:
        int: Number of occurrences of the target word.

        Time Complexity:
        O(R * C * 22 * len), where len is the length of the target string.

        Space Complexity:
        O(1) (excluding recursion stack).

        Constraints:
        1 ≤ len ≤ 15
        1 ≤ R, C ≤ 50
        """

        def is_valid(x, y, visited):
            """
            Check if the given coordinates are valid and have not been visited.

            Parameters:
            - x (int): X-coordinate.
            - y (int): Y-coordinate.
            - visited (list of lists): 2D array to track visited cells.

            Returns:
            bool: True if the coordinates are valid and not visited; otherwise, False.
            """
            return 0 <= x < R and 0 <= y < C and not visited[x][y]

        def dfs(x, y, index):
            """
            Depth-first search to explore all possible paths.

            Parameters:
            - x (int): Current X-coordinate.
            - y (int): Current Y-coordinate.
            - index (int): Current index in the target word.

            Returns:
            int: Number of occurrences starting from the current position.

            """
            if index == len(target) - 1:
                return 1

            visited[x][y] = True
            count = 0

            # Move in all possible directions
            for d in directions:
                new_x, new_y = x + d[0], y + d[1]
                if is_valid(new_x, new_y, visited) and mat[new_x][new_y] == target[index + 1]:
                    count += dfs(new_x, new_y, index + 1)

            visited[x][y] = False
            return count

        R, C = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        result = 0
        for i in range(R):
            for j in range(C):
                if mat[i][j] == target[0]:
                    visited = [[False] * C for _ in range(R)]
                    result += dfs(i, j, 0)

        return result

# Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        R = int(line[0])
        C = int(line[1])
        mat = []
        for _ in range(R):
            mat.append([x for x in input().strip().split()])
        target = input()
        obj = Solution()
        print(obj.findOccurrence(mat, target))
