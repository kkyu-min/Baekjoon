# Title : 별 찍기(2)
# Date : 2022/10/26
# https://www.acmicpc.net/problem/2439

import sys

num = int(sys.stdin.readline())

for i in range(1,num+1):
  print(" "*(num-i) + "*"*i)