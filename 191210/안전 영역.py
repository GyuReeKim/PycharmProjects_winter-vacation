# 백준 2468번

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(i, j, N):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if land[ni][nj] > rain and visited[ni][nj] == 0:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1


N = int(input())
land = [list(map(int, input().split())) for _ in range(N)]
# print(land)

maxH = 0
minH = 1000000
for i in range(N):
    for j in range(N):
        if land[i][j] > maxH:
            maxH = land[i][j]
        if land[i][j] < minH:
            minH = land[i][j]

maxV = 0
for rain in range(minH-1, maxH+1):
    cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if land[i][j] > rain and visited[i][j] == 0:
                cnt += 1
                bfs(i, j, N)
    if cnt > maxV:
        maxV = cnt
print(maxV)