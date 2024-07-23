# A+B - 7
import sys

num = int(input())

for i in range(num):
    a, b = map(int, sys.stdin.readline().split())
    sum = a + b
    print("Case #%d: %d" %(i+1, sum))