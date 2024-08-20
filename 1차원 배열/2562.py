# 최댓값
import sys

n = []
for i in range(9):
    a = int(sys.stdin.readline())
    n.append(a)

print(max(n))
print(n.index(max(n)) + 1)