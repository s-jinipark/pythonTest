
# 침몰하는 타이타닉(그리디)

def solution():
    answer = 0
    '''
    설명 듣고 품
    비슷한데 pop 하는 걸로 ..
    
    '''
    inp.sort()
    cnt = 0

    while inp :
        if len(inp) == 1:
            cnt += 1
            break
        if inp[0] + inp[-1] > M :
            inp.pop()
            cnt += 1
        else :
            inp.pop()
            inp.pop(0)   # 맨 앞.. => 맨 앞을 빼면 줄줄이 이동 [비효율적] => deque 써야..
            cnt +=1
    print(cnt)
    return answer


N= 5   # N 명의 승객
M = 140  # 몸무게 제한
inp = [90, 50, 70, 100, 60]

re = solution()
print('re :', re)
#=> 3
print('==============================')

N= 100
M = 130
inp = [30,78,83,62,51,60,68,115,109,20,38,42,44,43,118,25,46,38,56,87,112,22,21,38,40,44,100,56,52,60,82,70,51,55,32,83,83,91,97,100,95,74,83,89,57,70,22,48,110,68,83,59,45,102,43,23,50,110,33,64,108,44,96,26,44,63,24,96,99,65,70,51,46,60,62,65,109,103,112,115,86,48,87,108,114,117,30,59,40,82,55,80,113,75,112,94,116,38,112,67]

re = solution()
print('re :', re)
#=> 58
