import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])
s_arr = sorted(arr)
for y, x in s_arr:
    print(x, y)
