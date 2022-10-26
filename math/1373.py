# Title : 2진수 8진수
# Date : 2022/10/26
# https://www.acmicpc.net/problem/1373

import sys

x = sys.stdin.readline().strip()
answer = ''

if len(x)%3 == 1:
  answer += x[0]
elif len(x)%3 == 2:
  answer += str((int(x[0]) * 2) + int(x[1]))
for i in range(len(x)%3,len(x),3):
  tmp = str((int(x[i])*4) + (int(x[i+1])*2) + int(x[i+2]))
  answer += str(tmp)

print(answer)