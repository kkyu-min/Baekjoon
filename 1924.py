# Title : 2007년
# Date : 2022/10/26
# https://www.acmicpc.net/problem/1924

import sys 

mon_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_list = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

a,b = map(int, sys.stdin.readline().split())
day = 0

for i in range(a-1):
  day += mon_list[i]
day = (day + b) % 7

print(week_list[day])