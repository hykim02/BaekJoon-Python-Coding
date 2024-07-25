# 최댓값
n = []
for i in range(9):
    a = int(input())
    n.append(a)

print(max(n), n.index(max(n)) + 1)