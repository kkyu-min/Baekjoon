# Title : N과 M (2)
# Date : 2022/11/19
# https://www.acmicpc.net/problem/15650

import sys

def dfs(x):
    if len(s) == m:
        print(" ".join(map(str,s)))
        return
    
    for i in range(x,n+1):
        if check[i] == 1:
            continue
        check[i] = 1
        s.append(i)
        dfs(i)
        s.pop()
        check[i] = 0

n,m = map(int,sys.stdin.readline().split())
s = []
check = [0 for _ in range(n+1)]

dfs(1)
