#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        
        start = 0
        visited[start] = True
        stack = [0]
        ans=[0]
        while stack:
            node = stack.pop()
            
            for adjnode in adj[node]:
                if not visited[adjnode]:
                    stack.append(adjnode)
                    visited[adjnode]=True
                    # ans.append(adjnode)
        return ans
                

#{ 
#  Driver Code Starts
if __name__ == '__main__':
    T=int(input())
    while T>0:
        '''
        V,E=map(int,input().split())
        adj=[[] for i in range(V+1)]
        for i in range(E):
            u,v=map(int,input().split())
            adj[u].append(v)
            adj[v].append(u)
        '''
        V, E = 5, 4
        adj = [[1, 2, 3], [0], [0, 4], [0], [2], []]
        print(adj)
        
        ob=Solution()
        ans=ob.dfsOfGraph(V,adj)
        for i in range(len(ans)):
            print(ans[i],end=" ")
        print()
        T-=1
# } Driver Code Ends