# 별 찍기 - 2
# 오른쪽을 기준으로 정렬한 별
num = int(input())

for i in range(1, num + 1):
    print(" " * (num-i) +  "*" * i)
    

