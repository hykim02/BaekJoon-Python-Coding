# 공 넣기

N, M = map(int, input().split())

basket = [0] * N

for a in range(M):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        basket[b-1] = k

for i in range(N):
    print(basket[i], end = " ")