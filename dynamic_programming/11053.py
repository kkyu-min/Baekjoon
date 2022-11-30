# Title : 가장 긴 증가하는 부분 수열
# Date : 2022/11/30
# https://www.acmicpc.net/problem/11053

import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(num)]


for i in range(num):
  for j in range(i):
    if arr[i] > arr[j]:
      dp[i] = max(dp[j]+1, dp[i])

print(max(dp)+1)