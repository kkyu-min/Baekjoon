# Title : 일곱 난장이
# Date : 2022/11/17
# https://www.acmicpc.net/problem/2309

import sys

arr = []
for _ in range(9):
  arr.append(int(sys.stdin.readline()))
  
sum_arr = sum(arr)
tmp1 = 0
tmp2 = 0
for i in range(len(arr)):
  for j in range(i+1,len(arr)):
    if sum_arr - arr[i] - arr[j] == 100:
      tmp1 = arr[i]
      tmp2 = arr[j]
      
arr.remove(tmp1)
arr.remove(tmp2)
arr = sorted(arr)
for a in arr:
  print(a)