
# 회의실 배정(그리디)

def solution(n, inp):
    answer = 0
    #inp.sort()
    print(inp)
    # b = sorted(inp, key=lambda x: x[1])
    # print(b)
    # 그럼 첫번째 오른차순, 두번째 내림차순
    # d = sorted(inp, key=lambda x: (x[0], -x[1]))
    # print(d)
    # prv_ed = b[0][1]
    # cnt = 1
    # for i in range(1, len(b)):
    #     print(b[i])
    #     if prv_ed <= b[i][0]:
    #         cnt +=1
    #         prv_ed = b[i][1]
    # print(cnt)

    # 강사는 ?
    inp.sort(key=lambda x : (x[1], x[0]))  # 두번째 먼저 정렬
    print(inp)
    et = 0
    cnt = 0
    for s, e in inp:
        print(s, e)
        if s >= et :
            et = e
            cnt += 1
    print(cnt)

    '''
    이거(회의실) 기억에 끝나는 시간으로 sort 해서...

    [강사] 보통 그리디는 정렬
    '''
    return answer

n = 5

inp = [(1,4), (2,3), (3,5), (4,6), (5,7)]
# 테스트용 : (1,4) 와 (1,3) 테스트
#inp = [(1,4), (1,3), (2,3), (3,5), (4,6), (5,7)]


re = solution(n, inp)
print('re :', re)
#=>
print('==============================')

