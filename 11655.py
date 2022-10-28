# Title : ROT13
# Date : 2022/10/28
# https://www.acmicpc.net/problem/11655

import sys

s = sys.stdin.readline().rstrip()
answer = ''

for i in range(len(s)):
  if s[i] == " ":
    answer += s[i]
  elif s[i].isupper():
    if ord(s[i]) + 13 > 90:
      tmp = ord(s[i]) + 13 - 91 + 65
      answer += chr(tmp)
    else:
      answer += chr(ord(s[i])+13)
  elif s[i].islower():
    if ord(s[i]) + 13 > 122:
      tmp = ord(s[i]) + 13 - 123 + 97
      answer += chr(tmp)
    else:
      answer += chr(ord(s[i])+13)
  elif s[i].isdigit():
    answer += s[i]
    
print(answer)