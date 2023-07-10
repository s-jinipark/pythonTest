
# 가장 큰 수
def solution():
    answer = 0
    '''
    문자로 바꿔서 비교해야 겠다는 생각
    
    '''
    s_su = str(su)
    print(s_su)
    stk = []
    cnt = 0

    for i in range(len(s_su)):
        if len(stk) == 0 :
            stk.append(s_su[i])
        else :
            # stack 에 값이 있다는 얘기
            while stk:
                tmp = stk[-1]  # 맨 뒤
                if tmp < s_su[i]   and  cnt < m :  # 뺄 수 있는 수 m
                    stk.pop()  # 빼고
                    cnt +=1
                else :
                    stk.append(s_su[i])
                    break

    print(stk)

    # 1st 시도 .. 잘 안됨
    # stk.append(s_su[0])  # 셋팅
    # for i in range(1, len(s_su)):
    #     print(s_su[i])
    #     #stk.append()
    #     if len(stk) == 0:
    #         stk.append(s_su[i])
    #         continue
    #
    #     if stk[0] >= s_su[i] :
    #         stk.append(s_su[i])
    #
    #     elif stk[0] < s_su[i]: # 새로운 애가 더 커
    #         # stack 과 비교 -> stack 에 있는 값이 적으면 다 꺼내야 함
    #         while stk:
    #             if stk[0] < s_su :
    #                 stk.pop()
    #                 cnt  +=1
    #             if cnt == m :
    #                 break
    # return answer


su = 5276823
m = 3   # 제거할 m개 숫자


re = solution()
print('re :', re)
#=>
print('==============================')

