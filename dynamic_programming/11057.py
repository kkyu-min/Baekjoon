# Titel : 오르막수
# Date : 2022/10/28
# https://www.acmicpc.net/problem/11057

import sys

mod = 10007
n = int(sys.stdin.readline())
dp = [ [0] * 10 for i in range(n+1) ]
answer = 0

for i in range(10):
  dp[1][i] = 1
  
for i in range(2,n+1):
  for j in range(10):
    for k in range(j,10):
      dp[i][j] += dp[i-1][k]
      dp[i][j] %= mod
      
for i in range(10):
  answer += dp[n][i]
print(answer % mod)