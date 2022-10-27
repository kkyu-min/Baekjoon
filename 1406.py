# Title : 에디터
# Date : 2022/10/27
# https://www.acmicpc.net/problem/1406

import sys

leftstack = list(sys.stdin.readline().strip())
num = int(sys.stdin.readline())

rightstack = []

for i in range(num):
  cmd = sys.stdin.readline().split()
  if cmd[0] == "L":
    if len(leftstack) != 0:
      rightstack.append(leftstack.pop())
  elif cmd[0] == "D":
    if len(rightstack) != 0:
      leftstack.append(rightstack.pop())
  elif cmd[0] == "B":
    if len(leftstack) != 0:
      leftstack.pop()
  elif cmd[0] == "P":
    leftstack.append(cmd[1])
  

answer = leftstack + rightstack[::-1]
print(''.join(answer))