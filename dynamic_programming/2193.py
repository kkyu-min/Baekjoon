# Title : 이친수
# Date : 2022/10/28
# https://www.acmicpc.net/problem/2193

import sys

num = int(sys.stdin.readline())
dp = [0 for _ in range(num+2)]

dp[1] = 1
dp[2] = 1
for i in range(3,num+1):
  dp[i] = dp[i-2] + dp[i-1]
  
print(dp[num])