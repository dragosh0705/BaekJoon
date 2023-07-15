nums = list(input())
cnt = 0
arr = []
for i in nums:
    if i == '1':
        cnt += 1
        arr.append(cnt)
    elif i != '1':
        cnt = 0
        continue
if len(arr) != 0:
    print(max(arr))