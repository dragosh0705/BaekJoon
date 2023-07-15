n = int(input())
plist = []
qlist = []
result = []
cnt = 2
for i in range(n):
    p, q = map(int, input().split())
    plist.append(p)
    qlist.append(q)
    result.append(i)
for i in range(n):
    if plist[i] == max(plist) and qlist[i] == max(qlist):
        result[i] = 1
    elif plist[i] == min(plist) and qlist[i] == min(qlist):
        result[i] = cnt
    elif plist[i] != max(plist) or qlist[i] != max(qlist) or plist[i] != min(plist) or qlist[i] != min(qlist):
        result[i] = 2
        cnt += 1
print(*result, sep = ", ")