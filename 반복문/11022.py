# A+B - 8
import sys

num = int(input())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    sum = a + b
    print("Case #%d: %d + %d = %d" %(i+1, a, b, sum))