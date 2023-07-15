import math



x = int(input())
j = 0
cnt = 0
while x > 1:
    if x%2 == 0:
        cnt += 1
        x = x / 2
        print(x)
    elif x%3 == 0:
        cnt += 1
        x = x / 3
        print(x)
    elif x%6 == 0:
        cnt += 2
        x = x / 6
        print(x)
    else:
        if math.sqrt(x) % 2 != 0:
            cnt +=1
            x-= 1
            print(x)
        elif math.sqrt(x) %3 != 0:
            cnt += 1
            x -= 1
            print(x)

print(cnt)

'''
while x > 1:
    if n % 2 == 0:
        print(x)
    else:
        print(x)
        x -= 1
'''
