def gugudan1(dan, depth):
    if depth > 9:
        return

    print(dan, '*', depth, "=", dan * depth)
    gugudan1(dan, depth+1)


dan = 2
gugudan1(dan, 1)


'''
이건 똑같은 결과지만
print 를 먼저했음(전처리)

[ 흠.. 이전거와 비교하면 자신 호출 전/후 의 차이를 보여줌.. ]
'''