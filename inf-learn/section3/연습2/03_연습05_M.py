
##### 수들의 합
def solution():
    answer = 0
    #tmp = 0
    for i in range(N):
        tmp = 0   # [2] 위치 중요
        for j in range(i, N):
            tmp += inp[j]
            if tmp == M :
                answer += 1
                break
            if tmp > M :
                break
    #-> 이거슨 내가 풀은 것

    # 문제에서 원하는 건 이게 아님

    # 이 문제 스타일을 알고 있어야 (괄호를 넣을 수 있음)
    ''''
    풀이 봄. 
    lt , rt 를 이용해서. . .
    '''
    # lt = 0
    # rt = 1
    # tot = inp[0]  # 흠..
    # cnt = 0
    # while True:
    #     if tot == M :
    #         #print(lt, rt, tot)
    #         cnt += 1
    #         tot -= inp[lt]
    #         lt +=1
    #     elif tot < M :
    #         if rt < N:
    #             tot += inp[rt]
    #             rt += 1
    #         else :
    #             break
    #     else :
    #         tot -= inp[lt]
    #         lt += 1
    # print('cnt:', cnt)


    # 한번 더 풀어보고 넘어간다
    lt = 0
    rt = 1
    #tot = 0
    tot = inp[0]  # [2] 으아.. 0 번째를 넣어놔야 함
    cnt = 0
    while True:
        if tot < M :
            # 추가로 더해줘야지
            if rt < N :  # 여기 중요
                tot += inp[rt]
                rt += 1
            else :
                break
        elif tot == M :
            cnt += 1
            tot -= inp[lt]   # 여긴 lt 임
            lt += 1   # 여기도 lt
        else :
            tot -= inp[lt]
            lt += 1
    print('cnt', cnt)
    return answer

'''
슬라이딩 윈도우로..
'''

N=8
M=3
inp = [1,2,1,3,1,1,1,2]
re = solution()
print(re)
#=> 5

N=1000
M=100
inp = [4,5,5,3,5,3,1,5,2,1,2,4,5,3,3,1,2,3,2,1,2,2,5,2,1,1,2,1,3,2,1,5,5,4,2,5,2,4,1,1,2,3,4,4,1,2,5,4,4,5,1,5,3,5,3,3,1,4,3,1,1,4,1,3,2,5,5,4,3,2,4,3,2,3,5,3,2,4,2,2,5,4,1,2,5,2,4,3,4,3,4,4,3,3,1,1,1,5,3,4,4,4,5,5,1,2,5,5,5,1,3,5,3,3,5,5,2,4,5,3,5,1,5,1,3,3,5,1,1,4,1,1,3,2,2,4,5,3,2,3,4,1,2,2,5,4,4,2,3,3,3,1,1,4,5,2,2,5,1,4,1,1,5,5,5,1,4,3,3,1,1,3,1,1,5,5,4,4,3,4,5,4,2,3,5,2,3,1,1,1,4,1,2,1,1,1,2,3,3,3,1,2,2,4,4,2,1,5,5,5,2,5,1,5,1,5,2,4,4,2,4,3,2,5,5,1,1,3,3,5,1,4,4,1,5,2,1,1,3,4,2,4,1,4,4,4,1,5,2,3,1,2,3,2,2,1,4,5,2,5,2,3,2,1,5,2,5,1,5,3,4,2,3,5,5,3,4,5,4,5,5,4,4,4,2,3,2,3,3,5,3,5,4,1,5,5,3,5,2,1,1,5,4,2,1,1,3,4,2,5,4,3,1,4,3,4,2,3,3,2,4,1,4,4,5,4,1,4,3,4,1,5,1,3,4,3,5,5,3,1,2,4,5,5,2,2,3,2,5,5,4,2,1,1,2,5,1,5,2,1,2,1,4,1,4,5,5,4,1,3,4,1,5,1,2,5,5,4,3,4,4,5,5,5,4,5,5,5,3,3,1,3,2,2,2,2,1,1,3,1,3,4,4,4,1,4,3,4,1,5,3,5,2,2,3,4,3,5,2,4,4,3,1,5,1,1,1,5,5,2,5,4,4,2,4,4,2,2,1,4,5,1,2,2,2,5,3,2,2,1,4,5,1,1,2,2,1,1,1,2,4,3,4,1,3,1,1,5,5,2,3,3,1,2,2,5,2,1,4,5,5,1,2,4,3,5,5,4,4,4,3,1,1,3,1,4,1,5,1,2,3,5,4,1,1,4,4,1,1,3,4,2,1,1,5,2,3,5,2,5,3,4,3,2,5,3,3,2,5,5,5,2,2,4,4,5,4,2,2,2,5,5,3,3,1,2,3,3,4,2,3,5,5,4,1,2,5,1,4,1,1,3,1,1,3,3,1,3,5,2,4,4,3,5,2,2,3,4,3,2,5,4,5,1,2,4,1,5,1,2,2,2,1,1,1,2,4,4,4,5,2,1,2,4,5,1,4,5,3,3,3,3,5,4,2,2,3,5,1,5,4,5,1,1,1,4,4,2,2,3,3,3,1,3,4,4,4,3,1,1,2,5,4,2,2,4,3,5,5,2,1,5,1,4,3,1,1,3,2,2,5,4,3,3,4,1,4,2,4,1,5,2,5,3,2,4,1,4,5,3,2,2,3,2,2,5,4,4,1,4,3,4,1,4,3,4,5,2,5,4,3,4,3,5,4,5,2,4,2,3,3,1,3,2,3,2,2,2,2,5,1,5,4,5,3,5,2,1,5,5,1,2,3,3,2,2,4,3,1,2,5,5,2,5,2,2,1,4,1,4,4,3,2,5,5,3,2,1,4,3,5,3,5,5,5,1,2,2,3,1,4,3,3,2,1,5,5,5,3,4,1,2,2,3,3,3,4,1,3,5,3,1,3,4,5,3,4,3,1,3,4,1,2,1,2,2,2,4,2,3,3,2,5,2,2,1,4,1,5,2,3,1,3,4,1,4,2,4,3,2,5,1,2,1,3,4,5,4,4,1,5,1,3,3,1,5,3,4,4,2,2,3,3,5,4,5,1,4,5,1,5,4,3,4,2,5,2,4,1,2,5,5,5,5,1,2,2,5,2,1,3,5,2,4,3,5,5,2,1,3,4,5,1,4,4,4,4,2,4,1,5,4,5,2,2,5,3,2,1,1,4,1,1,3,2,2,1,4,5,2,1,2,1,4,2,5,3,4,1,4,4,5,1,2,3,5,4,5,2,2,2,2,5,2,3,4,1,2,2,5,2,2,1,3,5,3,2,1,3,2,3,2,3,2,3,3,5,4,4,3,3,1,2,3,2,5,3,5,5,4,1,3,2,2,1,2,5,3,1,2,3,4,3,5,2,1,3,4,1,4]
re = solution()
print(re)
#=> 312

