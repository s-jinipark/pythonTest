
# 프로그래머스 스타일 로 ...
def solution(n, inp):
    answer = 0

    # 정렬 테스트 =>
    b = sorted(inp)
    print(b)
    # [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

    c = sorted(inp, key= lambda x : x[0])
    print(c)
    # [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]

    d = sorted(inp, key = lambda x : x[1])
    print(d)
    # [(3, 0), (0, 1), (5, 1), (1, 2), (5, 2)]

    # 첫번째 인자를 기준으로 오름차순으로 먼저 정렬
    # 그 다음 두번째 인자를 기준으로 내림차순으로 정렬
    e = sorted(inp, key= lambda x : (x[0], -x[1]))
    print(e)
    # [(0, 1), (1, 2), (3, 0), (5, 2), (5, 1)]

    # < = 정렬 테스트

    # b 를 사용

    maxVal = 0
    for i in range(len(b)):
        print(b[i])
        start = b[i][0]
        end = b[i][1]
        #print('end>', end)
        cnt = 1
        for j in range(i+1, len(b)):
            #print('>', b[j])
            if start == b[j][0] :
                start = b[j][0]
                continue

            start = b[j][0]

            if end <= b[j][0]:
                end = b[j][1]
                #print('end>>', end)
                cnt += 1
        #print(cnt)
        if maxVal < cnt :
            maxVal = cnt
    answer = maxVal
    return answer

n = 5

# 정렬 테스트 용
#inp = [(1,2), (0,1), (5,1), (5,2), (3,0)]

inp = [(1,4), (2,3), (3,5), (4,6), (5,7)]

re = solution(n, inp)
print('re :', re)
#=>
print('==============================')

n = 20

inp = [(18 , 19),  (2  ,20 ),  (4  ,21 ),  (2  ,22 ),  (12 , 15),  (12 , 23),  (2  ,8  ),  (5  ,20 ),  (22 , 23),  (1  ,5  ),  (13 , 21),  (16 , 20),  (9  ,19 ),  (5  ,9  ),  (14 , 20),  (16 , 22),  (11 , 12),  (4  ,16 ),  (21 , 23),  (11 , 13)]

re = solution(n, inp)
print('re :', re)
#=> 6 (틀림)
print('==============================')