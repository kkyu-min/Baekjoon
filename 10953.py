# Title : A + B (6)
# Date : 2022/10/26
# https://www.acmicpc.net/problem/10953

import sys

cnt = int(sys.stdin.readline())

for i in range(cnt):
  a,b = map(int, sys.stdin.readline().split(','))
  print(a+b)