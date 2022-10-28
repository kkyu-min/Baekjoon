# Title : 스티커
# Date : 2022/10/28
# https://www.acmicpc.net/problem/9465

import sys

case = int(sys.stdin.readline())

for i in range(case):
  num = int(sys.stdin.readline())
  arr = [list(map(int, sys.stdin.readline().split())) for i in range(2)]
  dp = [[0] * 3 for i in range(num+1)]
  for i in range(1,num+1):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + arr[0][i-1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + arr[1][i-1]
    # print(dp)
  print(max(dp[num][0], dp[num][1], dp[num][2]))