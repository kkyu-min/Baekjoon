# Title : 미로 탐색
# Date : 2022/11/19
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

def bfs(x,y):
    # 상, 하, 좌, 우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    de = deque()
    de.append((x,y))
    check[x][y] = 1

    while de :
        tx, ty = de.popleft()

        if tx == n-1 and ty == m-1 :
            return check[tx][ty]
             
        for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if arr[nx][ny] == 0:
                continue
            if arr[nx][ny] == 1 and check[nx][ny] == 0:
                check[nx][ny] = check[tx][ty] + 1
                de.append((nx,ny))
    
    
    

n, m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
check = [[0 for _ in range(m)] for _ in range(n)]

print(bfs(0,0))