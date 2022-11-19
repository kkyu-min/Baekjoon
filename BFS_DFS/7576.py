# Title : 토마토
# Date : 2022/11/19
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

def bfs():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    de = deque()

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                de.append((i,j))

    while de:
        tx, ty = de.popleft()

        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if nx>=0 and nx<n and ny >= 0 and ny < m:
                if arr[nx][ny] == 0:
                    de.append((nx,ny))
                    arr[nx][ny] = arr[tx][ty] + 1


m,n = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]

bfs()

flag = False
for i in range(n):
    for j in range(m):
        if arr[i][j]==0:
            flag = True
            break

if flag:
    print(-1)
else:
    print(max(map(max,arr))-1)
