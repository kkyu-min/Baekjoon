# Title : 날짜 계산
# Date : 2022/11/17
# https://www.acmicpc.net/problem/1476

import sys

arr = list(map(int, sys.stdin.readline().split()))

start = [1,1,1]
answer = 1

while start != arr:
  start[0] += 1
  start[1] += 1
  start[2] += 1
  if start[0] == 16:
    start[0] = 1
  if start[1] == 29:
    start[1] = 1
  if start[2] == 20:
    start[2] = 1
  answer += 1
print(answer)