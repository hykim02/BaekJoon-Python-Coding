# # 킹, 퀸, 룩, 비숍, 나이트, 폰

# before
# # 필요한 피스 개수 정의
# piece = [1, 1, 2, 2, 2, 8]
# # 흰색 피스 개수 입력받기
# white = input().split()

# for i in range(len(piece)):
#     result = int(piece[i]) - int(white[i])
#     print(result, end = " ")

# after
piece = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))

for i in range(6):
    print(piece[i] - white[i], end=" ")