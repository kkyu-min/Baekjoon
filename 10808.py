# Title : 알바펫 개수
# Date : 2022/10/28
# https://www.acmicpc.net/problem/10808

import sys
s = sys.stdin.readline().strip()

alpha = [0 for _ in range(26)]

for i in s:
  alpha[ord(i) - 97] += 1

for i in alpha:
  print(i, end=" ")