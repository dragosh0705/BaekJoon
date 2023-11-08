n, m = map(int, input().split())
basket = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for j in range(i, j+1):
        basket[j] = k
for i in range(1, n + 1):
    print(basket[i], end = ' ')