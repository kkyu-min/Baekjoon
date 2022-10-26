# Title : 구구단
# Date : 2022/10/26
# https://www.acmicpc.net/problem/2739

import sys

num = int(sys.stdin.readline())

for i in range(1,10):
  print("%d * %d = %d" %(num,i,num*i))