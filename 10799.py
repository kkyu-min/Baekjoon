# Title : 쇠막대기
# Date : 2022/10/27
# https://www.acmicpc.net/problem/10799

import sys

stick = sys.stdin.readline().strip()
s = []
answer = 0

for i in range(len(stick)):
  if stick[i] == '(':
    s.append('(')
  else:
    if stick[i-1] == '(':
      s.pop()
      answer += len(s)
    else:
      s.pop()
      answer += 1
      
print(answer)