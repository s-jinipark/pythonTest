
def chk_count(n, inp):
    tmp_cnt = 0
    tmp_sum = 0
    for i in inp:
        tmp_sum += i
        if tmp_sum >= n :   # 주의 : = 가 있어야...
            tmp_cnt += 1
            tmp_sum = i  # 새로운 값 셋팅
            print(i, end=' ')
            print()
        else:
            print(i, end=' ')
    print()
    return tmp_cnt


# 프로그래머스 스타일 로 ...
def solution(N, M, inp):
    answer = 0

    start = 1
    end = sum(inp)
    print('s, e : ', start, end)

    cnt = 0
    #while cnt < 7:
    while start <= end:
        mid = (start+ end) //2
        #print(mid, chk_count(mid, inp))
        tmp_cnt = chk_count(mid, inp)
        print('mid, tmp_cnt' , mid, tmp_cnt)
        print('-----')

        if tmp_cnt <= M :  # M 이 나와도 계속 가본다는...
            # 갯수가 적다는 것은 길이를 줄여야 한다는
            end = mid -1

            if tmp_cnt == M :
                answer = max(answer, mid)
        else :
            # 그 밖에 갯수가 많다면, 길이를 늘여야...
            start = mid +1

        cnt += 1

    return answer

N = 9
M = 3

inp = [1, 2, 3, 4, 5, 6, 7, 8, 9]

re = solution(N, M, inp)
print('re :', re)
#=> 17
print('==============================')

N = 5
M = 4

inp = [1, 1, 1, 1, 1]

re = solution(N, M, inp)
print('re :', re)
#=> 2
print('==============================')

N = 10
M = 3

inp = [6, 5, 8, 5, 6, 8, 7, 6, 6, 7 ]

re = solution(N, M, inp)
print('re :', re)
#=> 24
print('==============================')

N = 100
M = 10

inp = [8,6,7,6,8,7,8,9,5,7,5,7,5,7,7,7,8,5,7,9,7,5,9,8,6,6,8,7,5,5,5,8,7,5,9,7,8,6,6,8,5,9,7,5,7,8,9,7,5,7,5,8,9,5,8,9,6,9,7,6,7,6,9,7,6,9,7,5,7,5,6,8,5,7,9,9,6,8,9,6,5,8,6,9,6,8,8,6,9,7,8,8,7,7,6,8,6,9,5,9]

re = solution(N, M, inp)
print('re :', re)
#=> ??
print('==============================')