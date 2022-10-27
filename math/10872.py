# Title : 팩토리얼
# Date : 2022/10/27
# https://www.acmicpc.net/problem/10872

import sys

num = int(sys.stdin.readline())
answer = 1

for i in range(1,num+1):
  answer *= i

print(answer)