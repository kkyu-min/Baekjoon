# Title : 조합 0의 개수
# Date : 2022/10/27
# https://www.acmicpc.net/problem/2004

import sys

a,b = map(int ,sys.stdin.readline().split())

def count2(n):
  cnt = 0
  if n < 2:
    return 0
  while n >= 2:
    cnt += n // 2
    n //= 2
  return cnt

def count5(n):
  cnt = 0
  if n < 5:
    return 0
  while n >= 5:
    cnt += n // 5
    n //= 5
  return cnt

two = count2(a) - count2(a-b) -count2(b)
five = count5(a) - count5(a-b) -count5(b)

print(min(two,five))