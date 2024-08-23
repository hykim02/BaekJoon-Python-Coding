# 나머지

rests = []

for i in range(10):
    num = int(input())
    rest = num % 42
    rests.append(rest)

rests = set(rests) # 중복 제거
print(len(rests))