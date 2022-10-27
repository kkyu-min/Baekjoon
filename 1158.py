# Title : 요세푸스 문제
# Date : 2022/10/27
# https://www.acmicpc.net/problem/1158

# import sys
# from collections import deque

# n, k = map(int,sys.stdin.readline().split())
# q = deque(range(1,n+1))
# answer = []

# while len(q) > 1:
#   for _ in range(k-1):
#     q.append(q.popleft())
#   answer.append(q.popleft())
# answer.append(q[0])

# print(str(answer).replace('[','<').replace(']','>'))
