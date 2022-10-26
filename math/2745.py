# Title : 진법 변환
# Date : 2022/10/26
# https://www.acmicpc.net/problem/2745

import sys

num,b = map(str, sys.stdin.readline().split())

mod = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
answer = 0

num = num[::-1]
for i in range(len(num)):
  tmp = mod.find(num[i])
  answer += (tmp * (int(b)**i))


print(answer)