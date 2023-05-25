
# 프로그래머스 스타일 로 ...
def solution(n, inp):
    answer = 0
    # 많이 하는 게 중요하므로,
    # 빨리 끝나는 시간이 중요
    slist = sorted(inp, key=lambda x : x[1])
    print(slist)
    prev_end = 0
    for i in range(len(slist)):
        print(slist[i])
        if slist[i][0]  >= prev_end :
            answer += 1
            prev_end = slist[i][1]  # 끝나는 시간
    return answer

n = 5

inp = [(1,4), (2,3), (3,5), (4,6), (5,7)]

re = solution(n, inp)
print('re :', re)
#=>
print('==============================')

n = 20

inp = [(18 , 19),  (2  ,20 ),  (4  ,21 ),  (2  ,22 ),  (12 , 15),  (12 , 23),  (2  ,8  ),  (5  ,20 ),  (22 , 23),  (1  ,5  ),  (13 , 21),  (16 , 20),  (9  ,19 ),  (5  ,9  ),  (14 , 20),  (16 , 22),  (11 , 12),  (4  ,16 ),  (21 , 23),  (11 , 13)]

re = solution(n, inp)
print('re :', re)
#=>
print('==============================')


'''
그리디 : 단계에서 가장 좋은 것 선택

대부분 정렬 
'''