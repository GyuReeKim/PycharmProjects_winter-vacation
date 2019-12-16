# 백준 17822번


def bfs(i, j, t):
    q = []
    visited = [[0]*M for _ in range(N)]
    q.append((i, j))
    visited[i][j] = 1
    cnt = 1
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if nj < 0:
                nj += M
            elif nj > M-1:
                nj -= M
            if 0 <= ni < N and visited[ni][nj] == 0:
                if plates[ni][nj] == t:
                    q.append((ni, nj))
                    visited[ni][nj] = 1
                    cnt += 1
    if cnt > 1:
        for r in range(N):
            for c in range(M):
                if visited[r][c] == 1:
                    plates[r][c] = 'x'
    # print(visited)


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M, T = map(int, input().split())
plates = [list(map(int, input().split())) for _ in range(N)]
cntX = 0
for t in range(T):
    # print('t')
    x, d, k = map(int, input().split())
    start_idx = [[j for j in range(M)] for i in range(N)]
    # print(start_idx)
    for i in range(N):
        # 원판 번호가 x의 배수라면
        if (i+1) % x == 0:
            # 시계방향으로 회전
            if d == 0:
                for m in range(M):
                    start_idx[i][m] -= k
                    if start_idx[i][m] < 0:
                        start_idx[i][m] += M
            # 반시계방향으로 회전
            elif d == 1:
                for m in range(M):
                    start_idx[i][m] += k
                    if start_idx[i][m] > M-1:
                        start_idx[i][m] -= M
    # print('start_idx')
    # print(start_idx)
    # temp = [[0]*M for _ in range(N)]
    # for i in range(N):
    #     for j in range(M):
    #         temp[i][j] = plates[i][start_idx[i][j]]
    # print(temp)
    plates = [[plates[i][start_idx[i][j]] for j in range(M)] for i in range(N)]
    # print(plates)

    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if plates[i][j] != 'x':
                bfs(i, j, plates[i][j])
    # print(plates)

    newX = 0
    all = 0
    for i in range(N):
        for j in range(M):
            if plates[i][j] == 'x':
                newX += 1
            else:
                all += plates[i][j]
    # print(cntX, newX)
    if newX == N*M:
        all = 0
        break
    average = all / (N*M - newX)
    # print(average)

    # 인접한 수가 없는 경우
    if cntX == newX:
        for i in range(N):
            for j in range(M):
                if plates[i][j] != 'x':
                    if plates[i][j] > average:
                        plates[i][j] -= 1
                        all -= 1
                    elif plates[i][j] < average:
                        plates[i][j] += 1
                        all += 1
        # print(plates)
    cntX = newX
print(all)