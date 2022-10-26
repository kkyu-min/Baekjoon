# Title : 나머지
# Date : 2022/10/26
# https://www.acmicpc.net/problem/10430

import sys

a,b,c = map(int, sys.stdin.readline().split())

a %= c
b %= c

print((a+b)%c)
print((a+b)%c)
print((a*b)%c)
print((a*b)%c)