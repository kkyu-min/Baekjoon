# Title : 진법 변환 2
# Date : 2022/10/26
# https://www.acmicpc.net/problem/11005

import sys

num, b = map(int, sys.stdin.readline().split())
mod = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = ""

while num != 0:
  tmp = num % b
  answer += mod[tmp]
  num //= b

print(answer[::-1])