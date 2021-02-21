def chess_desk(n):
    desk = [k + 10*i for i in range (1, n) for k in range (1, n)]
    print(desk)



chess_desk(9)
