T = int(input())
for i in range(T):
    h, w, n = map(int, input().split())
    flr = 0
    rooms = 0

    if n % h == 0:
        flr = h*100
        rooms = n // h
    else:
        flr = (n%h)*100
        rooms = 1 +n//h
    print(flr+rooms)