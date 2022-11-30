# Title : 포도주 시식
# Date : 2022/11/30
# https://www.acmicpc.net/problem/2156

import sys

num = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(num)]
dp = [0 for _ in range(num)]

dp[0] = arr[0]
if num > 1:
  dp[1] = arr[0] + arr[1]
if num > 2:
  dp[2] = max(dp[1], arr[0]+arr[2], arr[1]+arr[2])
if num > 3:
  for i in range(3,num):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i], dp[i-3]+arr[i-1]+arr[i])

print(max(dp))