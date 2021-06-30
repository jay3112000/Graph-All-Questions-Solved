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


def main():
    t = int(input())
    for i in range(t):
        V, e = map(int, input().split())
        g = Graph(V)
        for i in range(e):
            u, v = map(int, input().split())
            g.add_edge(u, v)

        g.dfs(0)


if __name__ == '__main__':
    main()