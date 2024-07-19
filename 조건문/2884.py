# 알람 시계
# 45분 일찍 알람 설정하기 (0 ≤ H ≤ 23, 0 ≤ M ≤ 59)

h, m = map(int, input().split())

if(m >= 45):
    m -= 45
else:
    gap = 45 - m # 시간 차
    m = 60 - gap
    if(h >= 1):
        h -= 1
    else: # h가 0인 경우
        h = 23

print(h, m)

