# bfs
# 거리와 관련한 문제는 bfs로 푼다.
# bfs는 속도가 빠른 편이다.


def bfs(n, V): # bfs(n, k, V): k번 노드에 도착하는지 확인하는 탐색
    global visited
    visited = [0] * (V+1)
    q = []
    q.append(n) # 시작노드 인큐
    visited[n] = 1 # 인큐한 노드 표시
    cnt = 0
    while q: # 큐에 노드가 남아있으면 반복
        n = q.pop(0) # 디큐 (처리할 노드 꺼냄)
        cnt += 1 # 방문한 노드의 개수 (노드에 대한 처리 위치)
        # if n == k:
        #     return 1
        for i in range(1, V+1):
            if adj[n][i] == 1 and visited[i] == 0: # n에 인접하고 처리안한 노드면
                q.append(i)
                visited[i] = visited[n] + 1 # 방문표시와 거리정보 동시 저장
    return cnt
    # return 0 # bfs(n, k, V) # k 노드에 도착하지 못한 경우


V, E = map(int, input().split())
g = list(map(int, input().split())) # 간선 정보 읽기

# 인접행렬
adj = [[0]*(V+1) for _ in range(V+1)]

for i in range(E): # 간선 정보로부터 인접행렬 만들기
    n1 = g[2*i]
    n2 = g[2*i+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1 # 무방향 그래프인 경우 필요

print(bfs(1, V))
print(visited)