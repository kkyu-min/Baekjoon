# Title : 별 찍기(1)
# Date : 2022/10/26
# https://www.acmicpc.net/problem/2438

import sys

num = int(sys.stdin.readline())

for i in range(1,num+1):
  print("*" * i)