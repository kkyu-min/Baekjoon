# Title : 2×n 타일링
# Date : 2022/10/26
# https://www.acmicpc.net/problem/11726

import sys

num = int(sys.stdin.readline())
dp = [0] * (num+1)

dp[0] = 1
dp[1] = 1
for i in range(2,num+1):
  dp[i] = dp[i-1] + dp[i-2]
  dp[i] %= 10007

print(dp[num])
