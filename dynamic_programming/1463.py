# Title : 1로 만들기
# Date : 2022/10/26
# https://www.acmicpc.net/problem/1463

import sys
num = int(sys.stdin.readline())
d = [0] * (num+1)

d[1] = 0

for i in range(2,num+1):
  d[i] = d[i-1] + 1
  if i % 2 == 0:
    if d[i] > d[i//2] + 1:
      d[i] = d[i//2] + 1
  if i % 3 == 0:
    if d[i] > d[i//3] + 1:
      d[i] = d[i//3] + 1
    
print(d[num])