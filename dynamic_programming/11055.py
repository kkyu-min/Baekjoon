# Title : 가장 큰 증가 부분 수열
# Date : 2022/11/30
# https://www.acmicpc.net/problem/11055

import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(num)]
dp[0] = arr[0]

for i in range(num):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[i],dp[j]+arr[i])
    else:
      dp[i] = max(dp[i],arr[i])

print(max(dp))