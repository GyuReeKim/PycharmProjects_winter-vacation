# 백준 16234번
# 푸는중


def f(i, j, g):
    q = []
    sum = 0
    visited = [[0]*N for _ in range(N)]

    q.append((i, j))
    sum += A[i][j]
    visited[i][j] = 1
    group[i][j] = g

    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and group[ni][nj] == 0:
                if visited[ni][nj] == 0 and L <= abs(A[i][j] - A[ni][nj]) <= R:
                    q.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                    group[ni][nj] = g
    # print(visited)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)

cycle = 0
while cycle <= 2:
    cycle += 1
    group = [[0]*N for _ in range(N)]
    idxG = 0
    for i in range(N):
        for j in range(N):
            if group[i][j] == 0:
                idxG += 1
                f(i, j, idxG)
    print(group)
