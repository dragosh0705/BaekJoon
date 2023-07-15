import re

n = int(input())
for i in range(n):
    inf_list = input().split() # 리스트 형식으로 넣기

    age = re.sub(r'[^0-9]', '', str(inf_list)) # 숫자만 추출
    name = [j for j in inf_list if j.isalpha()] # 문자만 추출
    name = ''.join(name)

    k = ''
    l = ''
    k[i] = list(age)
    l[i] = list(name)
    saved_l = ''
    age1 = ''
    name1 = ''

    if k[i] > k[i+1]:
        k[i], k[i+1] = k[i+1], k[i]
        l[i], l[i+1] = l[i+1], l[i]
        age1 = k[i]
        name1 = l[i]
        print(age1 + name1, end=' ')

    elif k[i] <= k[i+1]:
        saved_l = l[i]
        l.sort()
        if saved_l == l[i]:
            age1 = k[i]
            name1 = saved_l
            print(age1 + saved_l, end=' ')
        elif saved_l != l[i]:
            l[i], l[i+1] = l[i+1], l[i]
            k[i], k[i + 1] = k[i + 1], k[i]
            age1 = k[i]
            name1 = l[i]
            print(age1 + name1, end=' ')



