# X보다 작은 수
n, x = map(int, input().split())
a_list = list(map(int, input().split()))

for i in n:
    if(a_list[i] < x):
        print(a_list[i], end = " ")