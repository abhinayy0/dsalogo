import implement_graph 
Vertices=5
Edges=[[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]


class NewGraph(implement_graph.Graph):

    def modified_dfs(self,root, visited, stack):
        visited[root]=True
        for ele in self.graph[root]:
            if not visited[ele]:
                self.modified_dfs(ele,visited,stack)
        
        stack.append(root)

    def topological_sort(self, start_node):
        visited =[False] * (len(self.vertices) +1)
        stack =[]
        self.modified_dfs(start_node,visited,stack)
        print(stack[::-1])


if __name__=="__main__":
    graph = NewGraph()
    for edge in Edges:
        u,v = edge
        graph.add_edge(u,v)
    
    graph.display()
    graph.topological_sort(4)
    # graph.bfs(4)