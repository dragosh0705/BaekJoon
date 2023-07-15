def Find_RoomNum(flr, rooms,custnum):
    find_flr = []
    #find_rooms = []

    for i in range(flr):
        if flr < 1 or custnum < 1:
            break
        elif (flr * rooms < custnum):
            break

        elif (custnum % flr == 0 or custnum % rooms == 0):
            if rooms < 10:
                print(flr,0, custnum // flr, sep ='')
                break
            elif rooms >= 10:
                print(flr,custnum // flr, sep = '')
                break
        elif custnum < flr:
            if flr < 10:
                print(custnum, '01', sep = '')
                break
            elif flr >= 10:
                print(custnum, '01', sep ='')
                break



        elif custnum >= flr:
            find_newflr = int(custnum % flr)
            find_newrooms = int(custnum // flr+1)

            if(find_newrooms < 10):
                print(find_newflr, 0, find_newrooms, sep = '')
                break
            elif (find_newrooms >= 10):
                print(find_newflr, find_newrooms, sep = '')
                break




T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    Find_RoomNum(H, W, N)