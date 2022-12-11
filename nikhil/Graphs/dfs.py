# User function Template for python3

class Solution:

    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        self.V = V
        visited = [False for i in range(V)]
        # code here
        ans = []


        self.dfs(0,visited,ans)
        return ans

    def dfs(self, node, visited,ans):
        print(str(node) + " ",end=" ")

        visited[node] = True
        neighbors = adj[node]
        for child in neighbors:
            if visited[child] == False:
                self.dfs(child,visited,ans)
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        adj = [[] for i in range(V + 1)]
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
        ob = Solution()
        ans = ob.dfsOfGraph(V, adj)
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
# } Driver Code Ends