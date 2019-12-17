# 백준 14888번


def f(a, n):
    global maxV, minV
    if n == N-1:
        if a > maxV:
            maxV = a
        if a < minV:
            minV = a
    else:
        if calc[0] > 0:
            calc[0] -= 1
            f(a + A[n+1], n+1)
            calc[0] += 1
        if calc[1] > 0:
            calc[1] -= 1
            f(a - A[n+1], n+1)
            calc[1] += 1
        if calc[2] > 0:
            calc[2] -= 1
            f(a * A[n+1], n+1)
            calc[2] += 1
        if calc[3] > 0:
            calc[3] -= 1
            if a < 0:
                f(-((-a)//A[n+1]), n+1)
            else:
                f(a // A[n+1], n+1)
            calc[3] += 1


N = int(input())
A = list(map(int, input().split()))
calc = list(map(int, input().split()))

maxV = -1000000000
minV = 1000000000

f(A[0], 0)
print(maxV)
print(minV)
