# 공 바꾸기

N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]
# basket = [0] * N
# for i in range(N):
#     basket[i] = i+1 

for i in range(M):
    i, j = map(int, input().split())
    
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp
    # a = basket[i-1]
    # b = basket[j-1]
    # basket[i-1] = b
    # basket[j-1] = a

for i in range(N):
    print(basket[i], end = " ")