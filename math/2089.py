# Title : 2089
# Date : 2022/10/27
# https://www.acmicpc.net/problem/2089

import sys

num = int(sys.stdin.readline())
answer = ""
if num == 0:
  answer += '0'
else:
  while num !=0 :
    if num % -2 != 0:
      answer += "1"
      num = num//-2 + 1
    else:
      answer += "0"
      num //= -2
  
answer = answer[::-1]
print(answer)