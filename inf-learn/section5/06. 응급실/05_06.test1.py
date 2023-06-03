from collections import deque

# 프로그래머스 스타일 로 ...
def solution(N, M, inp):
    answer = 0

    qu = deque()

    for i in range(len(inp)):
        #qu.append((i+1, inp[i]))
        qu.append((i, inp[i]))  # 여기 잘 못 했던

    print(qu)

    # 대기목록에 자기보다 위험도가 높은 환자가 없을 때
    # 자신이 진료를 받는 구조

    ## 첫번째가 0 번째라며....  문제 잘 읽어야... ㅠ.ㅠ

    t_cnt = 0
    t_num = 0

    while qu :  #t_cnt < 10 : # 임시로 사용
        tmp = qu.popleft()
        print(tmp)
        for i in range(len(qu)):
            print('>', qu[i])
            if qu[i][1] > tmp[1]:
                qu.append(tmp)
                break
        else: # for 문 후에 수행
            # 여기오면 진료 받는다는 소리
            t_cnt +=1
            print('=', tmp[0], t_cnt)
            # if qu[i][0] == M:
            #     # t_num = answer + 1
            #     print('ans:', answer)
            if tmp[0] == M:
                answer = t_cnt
                break

        print(qu)

    ########## first (이상하게 답이 틀림)
    # 진료
    # cnt = 0
    # while len(qu) >  0 :
    #     tmp = qu.popleft()
    #     pri = tmp[1]
    #     flag = True
    #     for q in qu:
    #         print('>', q)
    #         if pri < q[1] :  # 우선 순위 높은 애가 있다
    #             flag = False
    #             break
    #     print('-----')
    #     print(qu)
    #     # # 진료 여부 결정
    #     if flag :
    #         cnt += 1
    #         if tmp[0] == M :
    #             print('cnt:', cnt)
    #
    #     else :
    #         qu.append(tmp)
    #
    #     print('2:', qu)
    # answer = cnt
    return answer

N = 5  # 대기 목록
M = 2  # 목록상의 M 번째 환자..
inp = [60, 50, 70, 80, 90]

re = solution(N, M, inp)
print('re :', re)
#=> 5
print('==============================')


N = 6
M = 0
inp = [60, 60, 90, 60, 60, 60]

re = solution(N, M, inp)
print('re :', re)
#=> 5
print('==============================')
