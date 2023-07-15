from math import sqrt

n = int(input())

for i in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    if x1 == x2:
        distance = abs(y2-y1)
    elif y1 == y2:
        distance = abs(x2-x1)
    else:
        distance = sqrt((x2-x1)**2 + (y2-y1)**2)

    if distance == 0 and r1 == r2:
        print(-1)
    elif r1+r2 < distance or abs(r2-r1) > distance:
        print(0)
    elif r1+r2 == distance or abs(r2-r1) == distance:
        print(1)
    else:
        print(2)