# 백준 2573번


def sea_cnt(i, j):
    cnt = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if arctic[ni][nj] == 0:
            cnt += 1
    return cnt


def f(i, j):
    q = []
    q.append((i, j))
    visited[i][j] = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if melt[ni][nj] != 0:
                    q.append((ni, nj))
                    visited[ni][nj] = 1


def melting(melt):
    for i in range(N):
        for j in range(M):
            arctic[i][j] = melt[i][j]


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arctic = [list(map(int, input().split())) for _ in range(N)]

cycle = 0
while True:
    cycle += 1
    melt = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arctic[i][j] != 0:
                diff = arctic[i][j] - sea_cnt(i, j)
                if diff < 0:
                    diff = 0
                melt[i][j] = diff
    # print(melt)
    visited = [[0]*M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if melt[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                f(i, j)
    if cnt == 0:
        cycle = 0
        break
    elif cnt > 1:
        break

    melting(melt)
    # print(arctic)

print(cycle)

