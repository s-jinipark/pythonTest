
# 프로그래머스 스타일 로 ...
def solution(inp):
    answer = 0

    # 카드 20 개 고정
    cards = []
    for i in range(21):
        cards.append(i)
    print(cards)

    for i in inp:
        #print(i)
        tmp = []
        for j in range(i[0], i[1]+1):
            #print(j)
            tmp.append(cards[j])
        # print(tmp)
        # tmp.sort(reverse=True)
        # print(tmp)
        cnt = len(tmp)-1
        for k in range(i[0], i[1]+1):
            cards[k] = tmp[cnt]
            cnt -= 1

        print('>', cards)
    print('>>', cards[1:])
    return answer


inp = [(5,10),(9,13),(1,2),(3,4),(5,6),(1,2),(3,4),(5,6),(1,20),(1,20)]
re = solution(inp)
print(re)
#=> 1 2 3 4 10 9 8 7 13 12 11 5 6 14 15 16 17 18 19 20
print('==============================')

inp = [(1,10),(3,3),(1,2),(3,7),(5,6),(1,9),(3,4),(5,6),(1,3),(1,9)]
re = solution(inp)
print(re)
#=> 9 10 4 7 5 8 2 3 6 1 11 12 13 14 15 16 17 18 19 20
print('==============================')

inp = [(2,8),(7,9),(1,2),(3,7),(1,1),(1,9),(2,9),(5,6),(1,3),(1,9)]
re = solution(inp)
print(re)
#=> 2 7 6 4 5 9 3 8 1 10 11 12 13 14 15 16 17 18 19 20
print('==============================')
