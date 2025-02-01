# 다이얼
word = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0

for a in word:
    for d in dial:
        if a in d:
            sum += dial.index(d) + 3
    
print(sum)