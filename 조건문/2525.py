# 오븐 시계
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 
# 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

h, m = map(int, input().split())
t = int(input()) 

# t를 시간, 분으로 계산
# 1시간 이상인 경우
if(t / 60 >= 1):
    ph = int(t / 60)
    pm = t % 60
    h += ph
    if(m + pm >= 60):
        m = 60 - (m + pm)
        h += 1
    else:
        m += pm
# 1시간 이내인 경우
else:
    if(m + t >= 60):
        m = t - (60 - m)
        h += 1
    else:
        m += t

if(h > 23):
    h -= 24

print(h, m)


