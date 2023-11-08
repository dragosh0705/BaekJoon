n = int(input())
arr = []
result = ""
for i in range(n):
    s = input()
    for j in s:
        arr.append(j)
        if len(arr) == 1 :
            result = s + s
        else:
            result = arr[0] + arr[len(arr) - 1]
    print(result)
    arr.clear()