# 바구니 뒤집기

# 새로운 리스트 만든 버전,,-> 시간초과

# N, M = map(int, input().split())
# ls = [i for i in range(1, N+1)] # 리스트 생성

# for a in range(M):
#     i, j = map(int, input().split())
#     new_ls = []

#     for n in range(i, j+1):
#         new_ls.append(ls[n-1])

#     print(new_ls)
#     new_ls.reverse() # 역순
#     print(new_ls)

#     for num in new_ls:
#         print(num)
#         if(i <= j):
#             ls[i-1] = num
#             i += 1
#         print(ls)
        
# for num in ls:
#     print(num, end = " ")

# 더 간단한 방법은 슬라이싱하기

N, M = map(int, input().split())

ls = [i for i in range(1, N+1)]

for a in range(M):
    i, j = map(int, input().split())

    temp = ls[i-1: j]
    temp.reverse()
    ls[i-1: j] = temp

for i in ls:
    print(i, end = " ")
