# 상수
A, B = input().split()

# 수 역전시키기
A = int(A[2] + A[1] + A[0])
B = int(B[2] + B[1] + B[0])

# sol1)리스트 max함수수
# ls = [A,B]
# print(max(ls))

# sol2)조건문
if A > B:
    print(A)
else:
    print(B)
