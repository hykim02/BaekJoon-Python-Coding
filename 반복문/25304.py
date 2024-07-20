# 영수증
# 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

total = int(input())
num = int(input())
sum = 0

for i in range(num):
    a, b = map(int, input().split())
    sum += (a*b)

if(total == sum):
    print("Yes")
else:
    print("No")