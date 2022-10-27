# Title : 팩토리얼 0의 개수
# Date : 2022/10/27
# https://www.acmicpc.net/problem/1676

import sys

num = int(sys.stdin.readline())

answer = 0
for i in range(1,num+1):
  while i % 5 == 0:
    answer += 1
    i //= 5
    
print(answer)