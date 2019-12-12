# 반복 구조의 dfs

# 7 8 # V: 노드, E: 간선
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


def dfs2(n, V): # 각 노드를 1번씩만 방문
    print(n, end=' ')
    visited[n] = 1
    # n에 인접하고, 방문하지 않은 노드로 이동
    for i in range(1, V + 1):
        print(i)
        if adj[n][i] == 1 and visited[i] == 0:  # i가 n에 인접하고 방문하지 않은 노드면
            dfs2(i, V)


V, E = map(int, input().split())
g = list(map(int, input().split())) # 간선 정보 읽기

# 인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]

visited = [0]*(V+1)

for i in range(E): # 간선 정보로부터 인접행렬 만들기
    n1 = g[2*i]
    n2 = g[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우 필요

dfs2(1, V)