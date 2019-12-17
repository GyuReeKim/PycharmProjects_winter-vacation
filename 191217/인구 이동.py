# 백준 16234번


def f(i, j, g):
    q = []
    add = 0
    cnt = 0

    q.append((i, j))
    add += A[i][j]
    cnt += 1
    visited[i][j] = 1
    group[i][j] = g

    while q:
        i, j = q.pop(0)
        # print(q, start, end)
        # print(i, j)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N and group[ni][nj] == 0:
                # print(abs(A[i][j] - A[ni][nj]))
                if visited[ni][nj] == 0 and L <= abs(A[i][j] - A[ni][nj]) <= R:
                    q.append((ni, nj))
                    add += A[ni][nj]
                    cnt += 1
                    visited[ni][nj] = visited[i][j] + 1
                    group[ni][nj] = g
    # print(group)

    average = int(add/cnt)
    if cnt > 1:
        for r in range(N):
            for c in range(N):
                if group[r][c] == g:
                    A[r][c] = average


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)

cycle = 0
idxG = 0
while idxG != N*N:
    group = [[0]*N for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    idxG = 0
    for i in range(N):
        for j in range(N):
            if group[i][j] == 0:
                idxG += 1
                f(i, j, idxG)

    # print(group)
    # if idxG == N*N:
    #     break
    cycle += 1
print(cycle-1)