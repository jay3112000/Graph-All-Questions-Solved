class Graph:
    def __init__(self, size):
        self.adj = []
        for i in range(size):
            self.adj.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, u, v):
        self.adj[u][v] = 1
        self.adj[v][u] = 1

    def remove_edge(self, u, v):
        self.adj[u][v] = 0
        self.adj[v][u] = 0

    def print_matrix(self):
        for row in self.adj:
            for val in row:
                print('{:4}'.format(val)),
            print

    def dfsutil(self, v, visited):
        visited.add(v)
        print(v)
        for i in range(len(self.adj)):
            if self.adj[v][i] == 1 and i not in visited:
                self.dfsutil(i, visited)

    def dfs(self, v):
        visited = set()
        self.dfsutil(v, visited)

    def bfs(self, s):
        q = []
        q.append(s)
        visited = set()
        visited.add(s)
        while len(q) > 0:
            s = q.pop(0)
            print(s)
            for i in range(self.size):
                if i not in visited and self.adj[s][i] == 1:
                    q.append(i)
                    visited.add(i)
    def topological_sort_util(self,v,visited,stack):
        visited.add(v)
        for i in range(self.size):
            if i not in visited:
                self.topological_sort_util(i,visited,stack)
        stack.append(v)

    def topological_sort(self):
        stack=[]
        visited=set()
        for i in range(self.size):
            if i not in visited:
                self.topological_sort_util(i,visited,stack)
        print(stack[::-1])

    def isPath(self,src,dest):
        visited=set()
        q=[]
        visited.add(src)
        q.append(src)
        while len(q)>0:
            temp = q.pop(0)
            for i in range(self.size):
                if temp == dest:
                    return True
                if i not in visited and self.adj[temp][i] == 1:
                    q.append(i)
                    visited.add(i)
        return False
    def allPathsUtil(self,src,dest,visited,path):
        visited.add(src)
        path.append(src)
        if src==dest:
            print(path)

        for i in range(self.size):
            if self.adj[src][i] == 1 and i not in visited:
                self.allPathsUtil(i,dest,visited,path)
        path.pop()
        visited.remove(src)

    def allPaths(self,src,dest):
        visited = set()
        path=[]
        self.allPathsUtil(src,dest,visited,path)
    def shortes_path_util(self,src,dest,visited,path,ans):
        visited.add(src)
        path.append(src)
        if src==dest:
            ans.append((len(path)))
        for i in range(self.size):
            if self.adj[src][i]==1 and i not in visited:
                self.shortes_path_util(i,dest,visited,path,ans)
        path.pop()
        visited.remove(src)
        return(min(ans))


    def shortest_path(self,src,dest):
        visited=set()
        path=[]
        ans=[]
        print(self.shortes_path_util(src,dest,visited,path,ans))

    def detect_util(self,s,visited,parent):
        visited.add(s)
        parent.append(s)
        for i in range(self.size):
            if self.adj[s][i]==1:
                if i not in visited:
                    parent[i]=s
                    self.detect_util(i,visited,parent)
                elif parent[s]!=i:
                    return True
        return False

    def detect_cycle(self,s):
        visited=set()
        flag=0
        parent = [-1] * self.size
        for i in range(self.size):
            if i not in visited and self.detect_util(i,visited,parent):
                flag=1
                break
        if flag==1:
            return('Yes')
        else:
            return('No')


    def isValid(self,visited,i,j,N,M,mat):
        if i>=0 and j>=0 and i<N and j<M and visited[i][j]==False and mat[i][j]==1:
            return  True
        return False


    def Number_Islands_Util(self,visited,i,j,N,M,mat):
        row=[1,1,0,-1,-1,0,-1,1]
        col=[-1,0,-1,0,-1,1,1,1]
        q=[]
        q.append((i,j))
        visited[i][j]=True
        while len(q)>0:
            x,y=q.pop(0)
            for k in range(8):
                if self.isValid(visited,x+row[k],y+col[k],N,M,mat):
                    visited[x+row[k]][y+col[k]]=True
                    q.append((x+row[k],y+col[k]))







    def Number_Islands(self):
        mat=[
            [1,1,1,0],
            [0,1,0,0],
            [1,1,0,0],
            [0,0,1,1],
            [0,0,0,0],
            [1,0,0,0]
        ]
        N=6
        M=4
        islands=0
        visited=[[False for x in range(M)] for y in range(N)]
        for i in range(N):
            for j in range(M):
                if visited[i][j]==False and mat[i][j]==1:
                    self.Number_Islands_Util(visited,i,j,N,M,mat)
                    islands+=1
        print(islands)





def main():
    t = int(input())
    for i in range(t):
        V, e = map(int, input().split())
        g = Graph(V)
        for i in range(e):
            u, v = map(int, input().split())
            g.add_edge(u, v)
        g.Number_Islands()



if __name__ == '__main__':
    main()
