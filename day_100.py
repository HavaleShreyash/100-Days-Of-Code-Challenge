from typing import List
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        """
        Find the shortest path that visits every node in the given graph.

        Parameters:
        - graph (List[List[int]]): An adjacency list representing the graph, where
          graph[i] is a list of nodes connected to node i.

        Returns:
        - int: The length of the shortest path that visits every node.

        Note:
        - The graph is assumed to be connected.

        Algorithm:
        - Precompute all-pairs shortest distances using Floyd-Warshall algorithm.
        - Perform a breadth-first search with backtracking to find the shortest path.
          The search is guided by a bitmask to keep track of visited nodes.
        """

        n = len(graph)

        # Precompute all-pairs shortest distances using Floyd-Warshall
        distances = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    distances[i][j] = 0
                else:
                    distances[i][j] = 1  # Edge weight is always 1

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

        # Perform a breadth-first search with backtracking
        queue = [(node, 1 << node, 0) for node in range(n)]  # (node, visited mask, path length)
        seen = set((node, 1 << node) for node in range(n))

        while queue:
            node, mask, length = queue.pop(0)
            if mask == (1 << n) - 1:  # All nodes visited
                return length

            for neighbor in graph[node]:
                new_mask = mask | (1 << neighbor)
                if (neighbor, new_mask) not in seen:
                    queue.append((neighbor, new_mask, length + 1))
                    seen.add((neighbor, new_mask))

        return -1  # Should never reach here

if __name__ == "__main__":
    # Example usage
    graph1 = [[1, 2, 3], [0], [0], [0]]  # Example 1 from the prompt
    graph2 = [[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]]  # Example 2 from the prompt

    solution = Solution()

    result1 = solution.shortestPathLength(graph1)
    print("Shortest path length for graph1:", result1)  # Output: 4

    result2 = solution.shortestPathLength(graph2)
    print("Shortest path length for graph2:", result2)  # Output: 4