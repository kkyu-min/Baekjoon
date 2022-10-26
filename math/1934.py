# Title : 최소공배수
# Date : 2022/10/26
# https://www.acmicpc.net/problem/1934

import sys

cnt = int(sys.stdin.readline())

def gcd(a,b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a

for i in range(cnt):
  a,b = map(int, sys.stdin.readline().split())
  g = gcd(a,b)
  print(int(g * (a/g) * (b/g)))