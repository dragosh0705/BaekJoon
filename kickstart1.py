import math

def FindEvenDigits(n):
    arr = []
    even = []
    arr = list(map(int, str(n)))
    for i in arr:
        if i%2 == 0 or i == 0:
            even.append(i)
    return even

def FindOddDigits(n):
    arr = []
    odd = []*(len(arr)+1)
    plusednum = 0 # 맨 앞자리수에서 1을 더한 수
    rest = 0 # 앞자리를 제외한 나머지 수
    arr = list(map(int, str(n)))

    if arr[0]%2 != 0:
        plusednum = arr[0]+1
        rest = abs(arr[0]*math.pow(10, len(arr)-1)-1) # 가장 큰 수의 자리수
        return rest

    '''x
    for i in range(1, len(arr)+1):
        if arr[0]%2 != 0 or arr[0] != 0:
            n = arr[i]*math.pow(10, len(arr)-i)
            return n
            '''

T = int(input())
plus = 0
minus = 0
arr = []
cnt = 0

for i in range(T):
    N = int(input())
    plus = N
    minus = N
    print(FindOddDigits((N)))

    while plus >=1:
        if len(FindEvenDigits(plus)) != len(str(plus)):
            #cnt += 1
            #print(FindOddDigits(N))
            plus += 1
            #cnt += 1 # 디버깅 용
            #print(len(FindEvenDigits(N)), len(str(plus)), plus)
        else:
            break

    while minus >= 1:
        if len(FindEvenDigits(minus)) != len(str(minus)):
            minus -= 1

        else:
            break

    print(plus, minus)
    case = "Case #"
    neun = ": "
    print(case+ str(i+1)+neun+ str(min(abs(N-plus), abs(N-minus))))