def solution(lottos, win_nums):
    answer = []
    win_cnt = 0
    zero_cnt = 0
    for l in lottos:
        if l in win_nums:
            print(l)
            win_cnt += 1
        if l == 0:
            zero_cnt += 1
    print(win_cnt, zero_cnt)
    # 최대는 win_cnt + zero_cnt 인경우
    # 최소는 win_cnt 만 본 경우
    '''
    1	6개 번호가 모두 일치
    2	5개 번호가 일치
    3	4개 번호가 일치
    4	3개 번호가 일치
    5	2개 번호가 일치
    6(낙첨)	그 외
    '''
    answer.append( show_ranking(win_cnt + zero_cnt) )
    answer.append( show_ranking(win_cnt ) )
    return answer

def show_ranking(cnt):
    rtn = 6
    if cnt == 6 :
        rtn = 1
    elif cnt == 5 :
        rtn = 2
    elif cnt == 4 :
        rtn = 3
    elif cnt == 3 :
        rtn = 4
    elif cnt == 2 :
        rtn = 5
    return rtn

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

re = solution(lottos, win_nums)
print(re)


'''
[기존]

def solution(lottos, win_nums):
    answer = []
    high = 0
    low = 0
    lank = 7
    for l in lottos :
        #print(l)
        if l in win_nums:
            #print(l)
            low += 1
        elif l == 0 :
            high += 1

    tmp_num = lank-(high+low)
    if tmp_num > 6:
        answer.append(6)
    else :
        answer.append(tmp_num)
        
    tmp_num = lank -  low
    if tmp_num > 6:
        answer.append(6)
    else :
        answer.append(tmp_num)

    #print(high)
    #print(low)

    return answer
'''
