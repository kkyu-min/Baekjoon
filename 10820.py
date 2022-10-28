# Title : 문자열 분석
# Date : 2022/10/28
# https://www.acmicpc.net/problem/10820

import sys

while 1:
  s = sys.stdin.readline().rstrip('\n')
  if len(s) == 0:
    break
  up, low , num, space = 0, 0, 0, 0
  
  for i in range(len(s)):
    if s[i].isspace():
      space += 1
    elif s[i].islower():
      low += 1
    elif s[i].isupper():
      up += 1
    elif s[i].isdigit():
      num += 1
  print("%d %d %d %d" %(low,up,num,space))