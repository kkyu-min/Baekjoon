# Title : 연결 요소의 개수
# Date : 2022/11/07
# https://www.acmicpc.net/problem/11724

import sys
sys.setrecursionlimit(100000)

def dfs(v):
  check[v] = 1
  for i in range(1,n+1):
    if check[i] == 0 and graph[v][i] == 1:
      dfs(i)
  
 
n,m = map(int, sys.stdin.readline().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
check = [0 for _ in range(n+1)]
cnt = 0

for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1
  
for i in range(1,n+1):
  if check[i] == 0:
    cnt += 1
    dfs(i)
    
print(cnt)