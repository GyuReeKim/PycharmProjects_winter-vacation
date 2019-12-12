# 백준 2569번


def bfs(i, j):
    global maxV
    q = []
    visited = [[0]*M for _ in range(N)]

    q.append((i, j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if land[ni][nj] == 'L':
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    if visited[ni][nj] > maxV:
                        maxV = visited[ni][nj]
    # print(visited)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
land = [list(input()) for _ in range(N)]
# print(land)

maxV = 0
for i in range(N):
    for j in range(M):
        if land[i][j] == 'L':
            # print(i, j)
            bfs(i, j)
print(maxV-1)