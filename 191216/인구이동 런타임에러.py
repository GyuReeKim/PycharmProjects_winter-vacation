# 백준 16234번


def dfs(i, j, g, a):
    # print(a)
    visited[i][j] = g
    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            # print(abs(a - A[ni][nj]))
            if visited[ni][nj] == 0 and L <= abs(a - A[ni][nj]) <= R:
                visited[ni][nj] = g
                dfs(ni, nj, g, A[ni][nj])


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
# print(A)

idxG =0
cycle = 0
while idxG != N*N:
    cycle += 1
    if cycle > 2000:
        break
    visited = [[0]*N for _ in range(N)]
    idxG = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                idxG += 1
                dfs(i, j, idxG, A[i][j])
                sum = 0
                cnt = 0
                for r in range(N):
                    for c in range(N):
                        if visited[r][c] == idxG:
                            sum += A[r][c]
                            cnt += 1
                # print(sum, cnt)
                # print(idxG)
                average = int(sum / cnt)
                for r in range(N):
                    for c in range(N):
                        if visited[r][c] == idxG:
                            A[r][c] = average
                # print(A)
print(cycle-1)