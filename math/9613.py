# Title : GCD 합
# Date : 2022/10/26
# https://www.acmicpc.net/problem/9613

import sys

cnt = int(sys.stdin.readline())
def gcd(a,b):
  if b == 0:
    return a
  else:
    return gcd(b,a%b)

for i in range(cnt):
  arr = list(map(int, sys.stdin.readline().split()))
  answer = 0
  for j in range(1,len(arr)):
    for k in range(j+1,len(arr)):
      answer += gcd(arr[j],arr[k])
  print(answer)