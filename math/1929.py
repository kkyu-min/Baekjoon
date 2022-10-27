# Title : 소수 구하기
# Date : 2022/10/27
# https://www.acmicpc.net/problem/1929

import sys
import math

a, b = map(int,sys.stdin.readline().split())

prime = [True for i in range(b+1)]
prime[1] = False

for i in range(2,int(math.sqrt(b))+1):
  if prime[i] == True:
    j = 2
    while i * j <= b:
      prime[i*j] = False
      j += 1
      
for i in range(a,b+1):
  if prime[i] == True:
    print(i)