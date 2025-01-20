T = int(input()) # 테스트 케이스 개수

ls = []
for i in range(T):
    ls.append(input())

for word in ls:
    print(word[0] + word[-1])
