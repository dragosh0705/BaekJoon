p, k = map(int, input().split())
prime = []

for i in range(1, 1000):
    for j in range(1, i):
        if i % j == 0:
            print(j)