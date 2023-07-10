
# 창고 정리

def solution():
    answer = 0
    '''
    설명 듣고 품
    '''
    inp.sort()
    print(inp)

    for i in range(M):
        inp[0] +=1
        inp[L-1] -= 1
        inp.sort()

    print(inp[L-1] - inp[0])

    return answer


L= 10   # 창고 가로의 길이

inp = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]

M = 50  # 높이 조정 횟수

re = solution()
print('re :', re)
#=>
print('==============================')

