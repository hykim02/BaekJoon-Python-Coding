# 평균
# 과목수
num = int(input())
score_list = list(map(int, input().split()))
max_score = max(score_list) # 최대 점수

new_score = []
for score in score_list:
    new_score.append(score/max_score*100) 

avg = sum(new_score)/num
print(avg)





