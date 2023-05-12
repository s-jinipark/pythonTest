def solution(dartResult):
    answer = 0
    '''
    1. 다트 게임은 총 3번의 기회로 구성된다.
    '''
    su = [0] * 3
    comp = [0] * 3  # 3개라고 정해져 있음
    #print(su)
    cnt = 0
    # [가변 길이를 분리하는게 어려움]
    start = 0
    for i in range(3):
        tmp = []
        for j in range(start, start+3):
            tmp2 = dartResult[j]
            # [1]
            # print(tmp2, tmp2.isdecimal())
            # if j == start+2 and tmp2.isdecimal() :  # 넘 지저분하지만
            #     start = start+2  # start 위치 업데이트
            #     break  # 빠져나감
            # elif j == start+2 and tmp2 == '*' :
            #     start = start+2  # start 위치 업데이트
            #     break  # 빠져나감
            # elif j == start+2 and tmp2 == '#' :
            #     start = start+2  # start 위치 업데이트
            #     break  # 빠져나감
            if j == start  :
                su[i] = int(dartResult[j])
            elif j == start + 1 :
                comp[i] = dartResult[j]
                if dartResult[j] == 'D':
                    su[i] = su[i] * su[i]
                elif dartResult[j] == 'T':
                    su[i] = su[i] * su[i] * su[i]
            elif j == start + 2:
                if tmp2.isdecimal() :
                    start = start + 2
                    break
                elif tmp2 == '*' :
                    start = start + 3
                    #su[i] = su[i] * 2
                    for k in range(i, -1, -1):
                        print(k)
                        su[k] = su[k] * 2
                    break
                elif tmp2 == '#' :
                    start = start + 3
                    su[i] = su[i] * -1
                    break

            if j == len(dartResult)-1:
                break

    print(su)
    print(comp)
    print(sum(su))
    return answer


#d = '1S2D*3T'
d = '1D2S#10S'

re = solution(d)
print(re)

print("====================")
