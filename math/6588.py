# Title : 골드바흐의 추측
# Date : 2022/10/27
# https://www.acmicpc.net/problem/6588

import sys
import math
n = 1000000
prime = [True for i in range(n+1)]
prime[1] = False

for i in range(2, int(math.sqrt(n))+1):
  if prime[i] == True:
    j = 2
    while i*j<=n:
      prime[i*j] = False
      j += 1
      
while 1:
  num = int(sys.stdin.readline())
  if num == 0:
    break
  check = 1
  for i in range(3,num//2+1):
    if prime[i] == True:
      if prime[num-i] == True:
        print("%d = %d + %d" %(num,i,num-i))
        check += 1
        break
  if check == 1:
    print("Goldbach's conjecture is wrong.")