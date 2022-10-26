# Title : 8진수 2진수
# Date : 2022/10/26
# https://www.acmicpc.net/problem/1212

import sys

num = sys.stdin.readline().strip()
answer = ''

if len(num) == 1 and num[0] == '0':
  print('0')
else:
  for n in num:
    tmp = ''
    n = int(n)
    for _ in range(3):
      tmp += str(n % 2)
      n //= 2
    tmp = tmp[::-1]
    answer += tmp
  
  if answer[0] == "0":
    answer = answer[1:]
    if answer[0] == '0':
      answer = answer[1:]
  
  print(answer)