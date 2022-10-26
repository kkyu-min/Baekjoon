# Title : 쉬운 계단 수
# Date : 2022/10/26
# https://www.acmicpc.net/problem/10844

import sys

mod = 1000000000
num = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(num+1)]

for i in range(1,10):
  dp[1][i] = 1
  
for i in range(2,num+1):
  for j in range(10):
    if j == 0:
      dp[i][j] = dp[i-1][j+1]
    elif j == 9:
      dp[i][j] = dp[i-1][j-1]
    else:
      dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
      
print(sum(dp[num]) % mod)
      