# 백준 1260번


def dfs(V, N):
    print(V, end=' ')
    dfs_visited[V] = 1
    for i in range(1, N+1):
        if adj[V][i] == 1 and dfs_visited[i] == 0:
            dfs(i, N)


def dfs2(V, N):
    s = []
    s.append(V)
    dfs2_visited[V] = 1
    while s:
        V = s.pop()
        print(V, end=' ')
        for i in range(1, N+1):
            if adj[V][i] == 1 and dfs2_visited[i] == 0:
                s.append(i)
                dfs2_visited[i] = dfs2_visited[V] + 1


def bfs(V, N):
    q = []
    q.append(V)
    bfs_visited[V] = 1
    while q:
        V = q.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if adj[V][i] == 1 and bfs_visited[i] == 0:
                q.append(i)
                bfs_visited[i] = bfs_visited[V] + 1




N, M, V = map(int, input().split()) # 정점의 개수, 간선의 개수, 탐색을 시작할 정점의 번호
adj = [[0]*(N+1) for _ in range(N+1)]
dfs_visited = [0]*(N+1)
dfs2_visited = [0]*(N+1)
bfs_visited = [0]*(N+1)
for k in range(M):
    n1, n2 = map(int, input().split())
    adj[n1][n2] = 1
    adj[n2][n1] = 1
# print(adj)

dfs(V, N)
print()
dfs2(V, N)
print()
bfs(V, N)