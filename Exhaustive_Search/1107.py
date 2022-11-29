# Title : 리모컨
# Date : 2022/11/17
# https://www.acmicpc.net/problem/1107

import sys

channel  = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = abs(100-channel)

for i in range(1000000):
  num = str(i)
  for j in range(len(num)):
    if int(num[j]) in arr:
      break
    elif len(num) == j + 1:
      answer = min(answer, abs(i-channel)+len(num))
print(answer)