

n = int(input())
arr = []
allarr = []
result = []



for i in range(n):
    num = int(input())
    arr.append(num)

for i in range(min(arr), max(arr)+1):
    allarr.append(i)

for i in allarr:
    for j in arr:
        if i == j:
            result.append(i)

for i in result:
    print(i)