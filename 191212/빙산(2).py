# 백준 2573번
# 푸는중


def bfs(i, j, melt):
    visited = [[0]*M for _ in range(N)]
    q = []

    q.append((i, j))
    visited[i][j] = 1

    # 빙산이 녹는 높이
    melt_height = arctic[i][j] - sea_cnt(i, j)
    if melt_height < 0:
        melt_height = 0
    melt[i][j] = melt_height

    while q:
        i, j = q.pop()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if arctic[ni][nj] != 0 and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = 1

                melt_height = arctic[ni][nj] - sea_cnt(ni, nj)
                if melt_height < 0:
                    melt_height = 0
                melt[ni][nj] = melt_height

    # # 녹이기
    # melting(melt)
    # print(melt)
    # # print(arctic)


def melting(melt):
    for i in range(N):
        for j in range(M):
            arctic[i][j] = melt[i][j]



def sea_cnt(i, j):
    cnt = 0
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if arctic[ni][nj] == 0:
            cnt += 1
    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
arctic = [list(map(int, input().split())) for _ in range(N)]
# print(arctic)
# 녹이기
melt_cnt = 0
startI = 0
startJ = 0
melt = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arctic[i][j] != 0:
            melt_cnt += 1
            startI, startJ = i, j
            bfs(startI, startJ, melt)
print(arctic)
melting(melt)
print(arctic)
print()
            # print(arctic)
            # 한 덩어리인지 확인
