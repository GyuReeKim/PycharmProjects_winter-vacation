# 총잡이

# 2
# 5 7
# T 0 T 0 G 0 G
# 0 W T W W W 0
# T W G 0 T W T
# 0 0 0 T G W 0
# 0 0 T 0 0 W 0
# 2 10
# T W 0 G 0 W 0 G 0 W
# G 0 T W T 0 T W T 0


def dfs(i, j, startI, startJ):
    visited = [[0]*M for _ in range(N)]
    s = []
    for k in range(4):
        s.append((startI, startJ))
        visited[i][j] = 1
        while s:
            i, j = s.pop()
            ni = i + di[k]
            nj = j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if room[ni][nj] == '0' and visited[ni][nj] == 0:
                    s.append((ni, nj))
                    visited[ni][nj] = 1
                elif room[ni][nj] == 'G' and visited[ni][nj] == 0:
                    return 1
    return 0


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    room = [list(input().split()) for _ in range(N)]
    # print(room)

    startI, startJ = 0, 0
    target = 0
    for i in range(N):
        for j in range(M):
            if room[i][j] == 'T':
                startI, startJ = i, j
                target += dfs(i, j, startI, startJ)
    print('#{} {}'.format(tc, target))