# 백준 2667번

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


def bfs(i, j, N):
    q = []
    q.append((i, j))
    v2[i][j] = 1
    cnt2 = 0
    while q: # 남은 칸이 있으면
        i, j = q.pop(0)
        cnt2 += 1 # 탐색 목적이 방문한 칸 수 세기
        for k in range(4): # 주변 칸(4방향)에 대해
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == '1' and v2[ni][nj] == 0: # 건물이 있고, 표시안한 칸이면
                    q.append((ni, nj))
                    v2[ni][nj] = v2[i][j] + 1
    return cnt2


def f(i, j, N):
    global homecnt
    v[i][j] = 1 # 방문표시
    homecnt += 1
    # # 유효한 인덱스인지 먼저 검사한 후 내용을 검사해야한다.
    # if j+1 < N and arr[i][j+1] == '1 and v[i][j+1] == 0:
    #     f(i, j+1, N)
    # # 독립적으로 움직이므로 elif가 아닌 if문을 사용해야 한다.
    # if i+1 < N and arr[i+1][j] == '1 and v[i+1][j] == 0:
    #     f(i+1, j, N)

    for k in range(4):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == '1' and v[ni][nj] == 0:
                f(ni, nj, N)


N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[0]*N for _ in range(N)] # 단지에 이미 포함된 위치 표시
v2 = [[0]*N for _ in range(N)] # 단지에 이미 포함된 위치 표시
home = []
home2 = []
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and v[i][j] == 0: # 단지에 속하지 않은 건물을 찾으면
            homecnt = 0
            f(i, j, N)
            cnt += 1 # 단지의 수
            home.append(homecnt)
        if arr[i][j] == '1' and v2[i][j] == 0: # 단지에 속하지 않은 건물을 찾으면
            home2.append(bfs(i, j, N))

home.sort()
home2.sort()
print(cnt)
for x in home:
    print(x)
print(cnt)
for x in home2:
    print(x)