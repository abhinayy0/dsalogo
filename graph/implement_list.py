from collections import deque
class Graph:
    def __init__(self, v):
        self.vertices =v
        self.matrix = [[0 for i in range(v)] for j in range(v)]
    
    def add_edge(self, u, v):
        self.matrix[u][v] = self.matrix[v][u] =1
    def display(self):
        print()
        for row in self.matrix:
            print(row)
        print()

    def bfs(self, start):

        visited = [False]*self.vertices

        q = deque()
        visited[start]=True
        q.append(start)
        while q:
            ele = q.popleft()
            print(ele, end=" ")
            
            for i in range(self.vertices):

                if self.matrix[ele][i] == 1 and not visited[i]:
                    q.append(i)
                    visited[i]=True
            

graph = Graph(5)
graph.add_edge(4,3)
graph.add_edge(1,2)
graph.display()
graph.bfs(4)


"""
a. BFS - https://www.geeksforgeeks.org/breadth...
b. DFS - https://www.geeksforgeeks.org/depth-f...
c. Dijkstra - https://www.geeksforgeeks.org/dijkstr...
d. Prim's - https://www.geeksforgeeks.org/prims-m...
e. Kruskal - https://www.geeksforgeeks.org/kruskal...
f. Floyd-Warshall - https://www.geeksforgeeks.org/floyd-w...
g. Union Find - https://www.geeksforgeeks.org/union-f...

"""