# 백준 14889번
# 내가 푼 것

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

minV = 1000000
for i in range(1, (1<<N)//2):
    start = []
    link = []
    for j in range(N):
        if i & (1<<j):
            start.append(j)
        else:
            link.append(j)

    if len(start) == N//2:
        # print(start, link)
        start_ability = 0
        link_ability = 0
        for r in range(N//2-1):
            for c in range(r+1, N//2):
                start_ability += (S[start[r]][start[c]] + S[start[c]][start[r]])
                link_ability += (S[link[r]][link[c]] + S[link[c]][link[r]])
        if abs(start_ability - link_ability) < minV:
            minV = abs(start_ability - link_ability)
print(minV)
