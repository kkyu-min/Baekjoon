# Title : 반복수열
# Date : 2022/11/10
# https://www.acmicpc.net/problem/2331

import sys

def next(num , p):
  res = 0
  for i in range(len(str(num))):
    tmp = 1
    for _ in range(p):
      tmp *= int(str(num)[i])
    res += tmp
  return res

a,p = map(int, sys.stdin.readline().split())

arr = [a]
answer = 0
mid = 0

while 1 :
  tmp = arr[-1]
  mid = next(tmp,p)
  arr.append(mid)
  s = set(arr)
  if len(arr) != len(s):
    break

for i in range(len(arr)):
  if mid == arr[i]:
    answer = i
    break
print(answer)