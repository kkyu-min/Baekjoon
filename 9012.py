# Title : 괄호
# Date : 2022/10/27
# https://www.acmicpc.net/problem/9012

import sys

def check(bracket):
  res = 'YES'
  stack = []
  for i in range(len(bracket)):
    if bracket[i] == "(":
      stack.append(bracket[i])
    else:
      if len(stack) == 0:
        res = "NO"
        return res
      else:
        stack.pop()
  if len(stack) > 0:
    res = "NO"
  return res
    
num = int(sys.stdin.readline())

for i in range(num):
  oper = sys.stdin.readline().strip()
  print(check(oper))