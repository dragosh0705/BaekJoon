N, L, W, H = map(int, input().split())
outerbox = L * W * H
innerbox = outerbox // N
A = innerbox ** (1/3)
print(A)