# Title : 최대공약수와 최소공배수
# Date : 2022/10/26
# https://www.acmicpc.net/problem/2609

import sys

a, b = map(int, sys.stdin.readline().split())

def gcd_1(a,b):
  if b == 0:
    return a
  else:
    return gcd_1(b,a%b)
  
def gcd_2(a,b):
  while b != 0:
    r = a%b
    a = b
    b = r
  return a

g = gcd_2(a,b)
print(gcd_1(a,b))
print(int(g * (a/g) * (b/g)))