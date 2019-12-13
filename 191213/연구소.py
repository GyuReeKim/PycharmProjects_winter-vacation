# 백준 14502번
# 푸는중


def f(n, s, k, l): # n 고른 벽 번호의 순서, s 고를 수 있는 벽의 번호, k 전체 벽의 수, l 골라야 할 벽의 수
    if n == l:
        # print(choice)
        f2(choice, k)
    else:
        for i in range(s, k-(l-n)+1):
            choice[n] = walls[i]
            f(n+1, i+1, k, l)


def f2(choice, k):
    # print(choice, k)
    for i in range(N):
        for j in range(M):
            if (i, j) in choice:
                lab[i][j] = 1
    copy_lab = [[0] * M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            copy_lab[r][c] = lab[r][c]
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                bfs(i, j, copy_lab)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if copy_lab[i][j] == 0:
                cnt += 1
    print(cnt)

    for i in range(N):
        for j in range(M):
            if (i, j) in choice:
                lab[i][j] = 0


def bfs(i, j, copy_lab):
    # copy_lab = [[0]*M for _ in range(N)]
    # for r in range(N):
    #     for c in range(M):
    #         copy_lab[r][c] = lab[r][c]
    visited = [[0]*M for _ in range(N)]
    q = []
    q.append((i, j))
    visited[i][j] = 1

    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if copy_lab[ni][nj] == 0:
                    copy_lab[ni][nj] = 2
                    q.append((ni, nj))
                    visited[ni][nj] = 1


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
# print(lab)

k = 0
walls = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            k += 1
            walls.append((i, j))
# print(k)
print(walls)
choice = [0]*3
f(0, 0, k, 3)