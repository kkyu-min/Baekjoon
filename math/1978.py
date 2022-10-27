# Title : 소수 찾기
# Date : 2022/10/27
# https://www.acmicpc.net/problem/1978

import sys

cnt = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

answer = 0

for a in arr:
  cnt = 0
  if a < 2:
    cnt += 1
  for i in range(2,a):
    if a % i == 0:
      cnt += 1
  if cnt == 0:
    answer += 1
  
print(answer)