def gugudan1(dan, depth):
    if depth < 1:
        return

    gugudan1(dan, depth-1)
    print(dan, '*', depth, "=", dan*depth)


dan = 2
gugudan1(dan, 9)


'''
자기자신 호출
호출 시 depth 가 하나씩 줄어 듬
프린트는 아직...

[ 흠.. 빠져나오는 형식을 볼 수 있네.. ]
'''