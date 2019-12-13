# 백준 15686번


def f2(M):
    s = 0 # 도시치킨거리(각 집에서 치킨집까지 최소거리의 합)
    for i in range(len(home)): # 각 집에 대해
        minH = 1000000
        for j in range(len(comb)): # 선택한 각 치킨집까지
            dis = abs(home[i][0] - bbq[comb[j]][0]) + abs(home[i][1]-bbq[comb[j]][1])
            if dis < minH: # 어떤 집에서 치킨집까지의 최소거리
                minH = dis
        s += minH
    return s


def f(n, s, k, M): # n 순서, s 고를 수 있는 치킨집 시작번호, k 전체 치킨집 수, M 고를 치킨집 수
    global minV
    if n == M: # M개의 치킨집을 고르면
        # print(comb)
        r = f2(M) # 도시 치킨거리 계산
        if r < minV:
            minV = r
    else:
        for i in range(s, k-(M-n)+1):
            comb[n] = i # i번 치킨집을 선택
            f(n+1, i+1, k, M)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
k = 0
minV = 1000000
home = []
bbq = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            k += 1
            bbq.append((i, j))
        elif arr[i][j] == 1:
            home.append((i, j))
comb = [0]*M
f(0, 0, k, M)
print(minV)
