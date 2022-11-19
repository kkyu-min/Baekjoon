# Title : 적록색약
# Date : 2022/11/19
# https://www.acmicpc.net/problem/10026

import sys

def dfs(tx,ty):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    check[tx][ty] = 1
    color = arr[tx][ty]

    for i in range(4):
        nx = tx + dx[i]
        ny = ty + dy[i]
        if (0 <= nx < n) and (0 <= ny < n):
            if check[nx][ny]==0 and arr[nx][ny]==color:
                dfs(nx,ny)


n = int(sys.stdin.readline())

arr = [list(map(str,sys.stdin.readline().strip())) for _ in range(n)]
check = [[0 for _ in range(n)] for _ in range(n)]
answer = [0,0]

for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            dfs(i,j)
            answer[0]+= 1

for i in range(n):
    for j in range(n):
        check[i][j] = 0
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

print(check)
for i in range(n):
    for j in range(n):
        if check[i][j] == 0:
            dfs(i,j)
            answer[1]+= 1

print(answer[0],answer[1])