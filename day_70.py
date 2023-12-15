def is_balanced(s):
    """
    Checks if a string of brackets is balanced.

    Args:
    - s (str): String of brackets containing (), {}, and [].

    Returns:
    - str: "YES" if the brackets are balanced, "NO" otherwise.
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return "NO"
        else:
            stack.append(char)

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    inputs = input().split(',')  # Read input as a comma-separated list of strings

    for string in inputs:
        result = is_balanced(string.strip())  # Check if each string of brackets is balanced
        print(result)
                                                                                                                            


def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n  # -1 represents uncolored, 0 and 1 represent two different colors
    visited = set()

    def dfs(node, color):
        if node in visited:
            return colors[node] == color

        visited.add(node)
        colors[node] = color

        for neighbor in graph[node]:
            if not dfs(neighbor, 1 - color):
                return False

        return True

    for node in range(n):
        if node not in visited and not dfs(node, 0):
            return False

    return True

if __name__ == "__main__":    
    num_nodes = int(input("Enter the number of nodes: "))
    graph = []
    for i in range(num_nodes):
        neighbors = list(map(int, input(f"Enter the neighbors for node {i}: ").split()))
        graph.append(neighbors)

    # Evaluate and print the result
    result = is_bipartite(graph)
    print("The graph is bipartite." if result else "The graph is not bipartite.")