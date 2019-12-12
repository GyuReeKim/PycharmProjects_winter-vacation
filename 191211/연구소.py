# 백준 14502번
# 푸는중

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
print(lab)

places = []
for i in range(N):
    for j in range(M):
        places.append([i, j])
print(places)


for i in range(len(places)-2):
    if lab[places[i][0]][places[i][1]] == 0:
        lab[places[i][0]][places[i][1]] = 1
        for j in range(i+1, len(places)-1):
            if lab[places[j][0]][places[j][1]] == 0:
                lab[places[j][0]][places[j][1]] = 1
                for k in range(j+1, len(places)):
                    if lab[places[k][0]][places[k][1]] == 0:
                        lab[places[k][0]][places[k][1]] = 1

                        q = ['']*N*M
                        for r in range(N):
                            for c in range(M):
                                pass
                        lab[places[k][0]][places[k][1]] = 0
                lab[places[j][0]][places[j][1]] = 0
        lab[places[i][0]][places[i][1]] = 0
