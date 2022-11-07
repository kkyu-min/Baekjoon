# Title : DFS와 BFS
# Date : 2022/11/07
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque

def dfs(v):
  check[v] = 1
  print(v,end=' ')
  for i in range(1,n+1):
    if check[i] == 0 and graph[v][i] == 1:
      dfs(i)

def bfs(v):
  de = deque()
  de.append(v)
  check[v] = 1
  while de:
    v = de.popleft()
    print(v,end=' ')
    for i in range(1,n+1):
      if check[i] == 0 and graph[v][i]==1:
        de.append(i)
        check[i]=1
  
n,m,v = map(int,sys.stdin.readline().split())

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
check = [0 for _ in range(n+1)]

for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graph[a][b] = graph[b][a] = 1
  
dfs(v)
check =[0 for _ in range(n+1)]
print()
bfs(v)