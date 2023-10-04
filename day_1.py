#Code for implementation of BFS traversal
#Used GFG as resource 

from collections import defaultdict

class traversal:
    def __init__(self) -> None:
        self.graph = defaultdict(list) #we use defaultdict to create a dictionary that doesnt send error when key kept empty

    def add_edge(self,x,y):
        self.graph[x].append(y)

    def bfs(self, s):
        visited = [False] * (max(self.graph) + 1)
 
        queue = []
        
        queue.append(s)
        visited[s] = True
 
        while queue:

            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# if __name__ == '__main__':
    # adding and traversing code ...