def gugudan1(dan, depth):
    if depth < 1 :
        return
    #print(dan , ' * ', depth , ' = ' , dan * depth) # 여기 놓으면 2 * 9 부터 나옴
    gugudan1(dan, depth-1)
    print(dan , ' * ', depth , ' = ' , dan * depth)

dan = 2
gugudan1(dan, 9)


