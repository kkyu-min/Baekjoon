# Title : 단지번호붙이기
# Date : 2022/11/10
# https://www.acmicpc.net/problem/2667

import sys
from collections import deque
sys.setrecursionlimit(1000000)

def bfs(i,j):
  de = deque()
  de.append([i,j])
  cnt = 1
  check[i][j] = 1
  while de:
    apt = de.popleft()
    if check[apt[0]-1][apt[1]] == 0 and graph[apt[0]-1][apt[1]]:
      de.append([apt[0]-1,apt[1]])
      check[apt[0]-1][apt[1]] = 1
      cnt += 1
    if check[apt[0]+1][apt[1]] == 0 and graph[apt[0]+1][apt[1]]:
      de.append([apt[0]+1,apt[1]])
      check[apt[0]+1][apt[1]] = 1
      cnt += 1
    if check[apt[0]][apt[1]-1] == 0 and graph[apt[0]][apt[1]-1]:
      de.append([apt[0],apt[1]-1])
      check[apt[0]][apt[1]-1] = 1
      cnt += 1
    if check[apt[0]][apt[1]+1] == 0 and graph[apt[0]][apt[1]+1]:
      de.append([apt[0],apt[1]+1])
      check[apt[0]][apt[1]+1] = 1
      cnt += 1
      
  return cnt

n = int(sys.stdin.readline())
graph = [[0 for _ in range(n+2)] for _ in range(n+2)]
check = [[0 for _ in range(n+2)] for _ in range(n+2)]

for i in range(n):
  line = sys.stdin.readline().strip()
  for j in range(len(line)):
    if line[j] == '1':
      graph[i+1][j+1] = 1

answer = [0]

for i in range(1,n+2):
  for j in range(1,n+2):
    if check[i][j] == 0 and graph[i][j] == 1:
      answer[0] += 1
      answer.append(bfs(i,j))
      
print(answer[0])
answer = answer[1:]
answer.sort()
for i in answer:
  print(i)