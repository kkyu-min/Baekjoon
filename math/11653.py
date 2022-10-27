# Title : 소인수분해
# Date : 2022/10/27
# https://www.acmicpc.net/problem/11653

import sys
import math

num = int(sys.stdin.readline())

if num != 1:
  for i in range(2,int(math.sqrt(num))+1):
    while num % i == 0:
      print(i)
      num //= i
  if num > 1:
    print(num)