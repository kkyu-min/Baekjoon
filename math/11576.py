# Title : Base Conversion
# Date : 2022/10/27
# https://www.acmicpc.net/problem/11576

import sys

a,b = map(int, sys.stdin.readline().split())
cnt = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr = arr [::-1]
ten = 0

for i in range(cnt):
  ten += arr[i]*(a**i)
  
answer = []

while ten > 0:
  answer.append(str(ten%b))
  ten //= b
  
answer = answer[::-1]
answer = ' '.join(answer)
print(answer)