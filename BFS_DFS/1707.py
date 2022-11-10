# Title : 이분 그래프
# Date : 2022/11/10
# https://www.acmicpc.net/problem/1707

# 이분 그래프 : 인접한 정점끼리 서로 다른 색으로 칠해서 모든 정점을 두가지 색으로만 칠할 수 있는 그래프

import sys

sys.setrecursionlimit(100000)

def dfs(start, color):
  check[start] = color
  for i in graph[start]:
    if check[i] == 0:
      tmp = dfs(i,-color)
      if not tmp:
        return False
    elif check[i] == check[start]:
      return False
  return True

testcase = int(sys.stdin.readline())

for i in range(testcase):
  v,e = map(int, sys.stdin.readline().split())
  graph = [[] for _ in range(v+1)]
  check = [0 for _ in range(v+1)]
  for _ in range(e):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
  for i in range(1,v+1):
    if check[i] == 0:
      res = dfs(i,1)
      if not res:
        break
  if res:
    print('YES')
  else:
    print('NO')