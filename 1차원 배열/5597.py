# 과제 안 낸 사람

num = [i for i in range(1,31)]

for i in range(28):
    a = int(input())
    num.remove(a)

num.sort()

for i in num:
    print(i)