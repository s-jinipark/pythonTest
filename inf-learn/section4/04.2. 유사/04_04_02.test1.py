
# 프로그래머스 스타일 로 ...
def solution(N, inp):
    answer = 0
    lt = min(inp)
    rt = max(inp) * N
    print(lt, rt)

    while lt <= rt:
        mid = (lt+rt)//2
        print(mid)
        checked = 0
        for time in inp:
            checked += mid //time

        # 2명이 mid 값에 얼마나 처리하는지

        if checked >= N :  # 심사 받은 사람이 더 많네.. 그럼 줄여야지..
            answer = mid
            rt = mid -1
        elif checked < N :
            lt = mid +1

    '''
    # 가장 큰 값을 찾고 하는 .. 그런 건 없나??
    
    https://happy-obok.tistory.com/10
    
    문제 출처:

    https://programmers.co.kr/learn/courses/30/lessons/43238

    '''
    # 1st 잘 안되서, 구글링
    # 연습 = []
    # for i in inp:
    #     for j in range(1, N):
    #         #print(i * j)
    #         연습.append(i*j)
    # 연습.sort()
    # print(연습)
    #
    # start = 연습[0]
    # end = 연습[-1]
    #
    # count = 0
    # # 변경 필요
    # while count < 5:
    #     mid = (start + end) // 2
    #     print(mid)
    #
    #     count += 1

    return answer

N = 6

inp = [7, 10]

re = solution(N, inp)
print('re :', re)
#=>
print('==============================')
