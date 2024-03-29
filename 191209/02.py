# 반복 구조의 dfs

# 7 8 # V E
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7


def dfs1(n, V): # 반복구조, 각 노드를 1번씩만 방문
    visited = [0]*(V+1)
    s = [] # 스택 생성
    s.append(n) # 시작노드 push(), 방문할 노드를 저장...
    visited[n] = 1 # push()한 노드를 표시

    # 스택이 비어있지 않으면... while len(s) != 0:
    while s: # 방문하지 않은 노드가 있으면(갈림길에서 남겨놓은 노드가 있으면)
        n = s.pop() # 갈림길에서 하나를 선택
        print(n) # 처리 순서를 출력
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: # i가 n에 인접하고 방문하지 않은 노드면
                s.append(i)
                visited[i] = 1


V, E = map(int, input().split())
g = list(map(int, input().split())) # 간선 정보 읽기

# 인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]

for i in range(E): # 간선 정보로부터 인접행렬 만들기
    n1 = g[2*i]
    n2 = g[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우 필요

dfs1(1, V)