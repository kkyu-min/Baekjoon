# Title : 1,2,3 더하기
# Date : 2022/10/26
# https://www.acmicpc.net/problem/9095

import sys

case  = int(sys.stdin.readline())
dp = [0] * 11

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,11):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(case):
  num = int(sys.stdin.readline())
  print(dp[num])