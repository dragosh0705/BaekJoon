import time # 시간측정

start = time.time() #시간측정


def fibonacci (n):
    if n==0:
        #print(0)
        fibarray.append(0)
        return 0
    elif n==1:
        #print(1)
        fibarray.append(1)
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


global one
global zero
fibarray = []
cnt = int(input())
for i in range(cnt):
    n = int(input())
    fibonacci(n)
    zero = fibarray.count(0)
    one = fibarray.count(1)
    print(zero, one)
    fibarray.clear()
    print("time :", time.time() - start) # 시간측정







    #if fibonacci(n) == 0:
      #  zero += 1
        #print(zero)
    #elif fibonacci(n) == 1:
     #   one += 1
        #print(one)
   # print(zero, one)