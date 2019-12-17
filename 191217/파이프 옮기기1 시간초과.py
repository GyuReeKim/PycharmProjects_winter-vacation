# 백준 17070번
# 시간초과


def f(i, j, s):
    global cnt
    # print(i, j)
    if (i, j) == (N-1, N-1):
        cnt += 1
    else:
        if s == 0:
            for k in range(2):
                ni = i + ri[k]
                nj = j + rj[k]
                if ni < N and nj < N and house[ni][nj] == 0:
                    if k == 1:
                        wall = 0
                        for l in range(2):
                            wi = i + xi[l]
                            wj = j + xj[l]
                            if wi < N and wj < N and house[wi][wj] == 1:
                                wall += 1
                        if wall == 0:
                            f(ni, nj, 2)
                    else:
                        f(ni, nj, s)
        if s == 1:
            for k in range(2):
                ni = i + ci[k]
                nj = j + cj[k]
                if ni < N and nj < N and house[ni][nj] == 0:
                    if k == 1:
                        wall = 0
                        for l in range(2):
                            wi = i + xi[l]
                            wj = j + xj[l]
                            if wi < N and wj < N and house[wi][wj] == 1:
                                wall += 1
                        if wall == 0:
                            f(ni, nj, 2)
                    else:
                        f(ni, nj, s)
        if s == 2:
            for k in range(3):
                ni = i + di[k]
                nj = j + dj[k]
                if ni < N and nj < N and house[ni][nj] == 0:
                    if k == 0:
                        f(ni, nj, k)
                    elif k == 1:
                        f(ni, nj, k)
                    else:
                        wall = 0
                        for l in range(2):
                            wi = i + xi[l]
                            wj = j + xj[l]
                            if wi < N and wj < N and house[wi][wj] == 1:
                                wall += 1
                        if wall == 0:
                            f(ni, nj, s)


ri = [0, 1]
rj = [1, 1]
ci = [1, 1]
cj = [0, 1]
di = [0, 1, 1]
dj = [1, 0, 1]
xi = [0, 1]
xj = [1, 0]

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
status = 0
cnt = 0
f(0, 1, status)
print(cnt)