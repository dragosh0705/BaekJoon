import sys
dic = {}
input = sys.stdin.readline
n = int(input())
for i in range(n):
    a = int(input())
    if a in dic.keys():
        dic[a] += 1
    else:
        dic[a] = 1

dic = sorted(dic.items(), key = lambda x: (-x[1], x[0]))
print(dic[0][0])