# Title : 순열 사이클
# Date : 2022/11/10
# https://www.acmicpc.net/problem/10451

import sys
sys.setrecursionlimit(1000000)

def dfs(start):
  check[start] = 1
  tmp = graph[1][start]
  if check[tmp] == 0:
    dfs(tmp)


testcase = int(sys.stdin.readline())

for _ in range(testcase):
  n = int(sys.stdin.readline())
  check = [0 for _ in range(n+1)]
  graph = [[0 for _ in range(n+1)]]
  arr = [0] + list(map(int, sys.stdin.readline().split()))
  graph.append(arr)
  answer = 0
  for i in range(1,n+1):
    if check[i] == 0:
      dfs(i)
      answer+=1
  print(answer)