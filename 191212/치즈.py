# 백준 2636번


def air(i, j):
    q = []
    q.append((i, j))
    plate[i][j] = 2
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if plate[ni][nj] == 0:
                    q.append((ni, nj))
                    plate[ni][nj] = 2


def cheeze(i, j):
    q = []
    q.append((i, j))
    plate[i][j] = 3
    while q:
        i, j = q.pop(0)
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if plate[ni][nj] == 1:
                q.append((ni, nj))
                plate[ni][nj] = 4
                for l in range(4):
                    pi = ni + di[l]
                    pj = nj + dj[l]
                    if plate[pi][pj] == 2:
                        plate[ni][nj] = 3


def last():
    cnt = 0
    for i in range(N):
        for j in range(M):
            if plate[i][j] == 2:
                plate[i][j] = 0
            elif plate[i][j] == 3:
                cnt += 1
                plate[i][j] = 0
            elif plate[i][j] == 4:
                plate[i][j] = 1
    return cnt


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N, M = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    time += 1
    air(0, 0)
    # print(plate)
    for i in range(N):
        for j in range(M):
            if plate[i][j] == 1:
                cheeze(i, j)
    last_cheeze = last()
    # print(last_cheeze)
    # print(plate)

    cheeze_left = 0
    for i in range(N):
        for j in range(M):
            if plate[i][j] == 1:
                cheeze_left = 1
                break
        if cheeze_left == 1:
            break

    if cheeze_left == 0:
        break
print(time)
print(last_cheeze)
