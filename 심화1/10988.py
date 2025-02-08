# 팰린드롬인지 확인하기
word = input()
word_list = list(word)

# 역전시키기
word_list.reverse()

print(word)
print(word_list)
# 비교
if(word == word_list):
    print(1)
else:
    print(0)