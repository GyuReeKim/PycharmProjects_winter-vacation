# 백준 2667번
# 풀이중

N = int(input())
arr = [list(input()) for _ in range(N)]
v = [[0]*N for _ in range(N)] # 단지에 이미 포함된 위치 표시
cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and v[i][j] == 0: # 단지에 속하지 않은 건물을 찾으면
            f(i, j, N)
            cnt += 1 # 단지의 수
