# 4012번 [모의 SW 역량테스트] 요리사


def f(n, k):
    global minV
    if n == k:
        # print(A, B)
        s1 = 0
        s2 = 0
        for i in range(k//2-1):
            for j in range(i+1, k//2):
                s1 += S[A[i]][A[j]] + S[A[j]][A[i]]
                s2 += S[B[i]][B[j]] + S[B[j]][B[i]]
        if abs(s1 - s2) < minV:
            minV = abs(s1 - s2)
    else:
        if len(A) < k//2:
            A.append(n)
            f(n+1, k)
            A.pop()
        if len(B) < k//2:
            B.append(n)
            f(n+1, k)
            B.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    A = []
    B = []
    minV = 1000000
    f(0, N)
    print('#{} {}'.format(tc, minV))