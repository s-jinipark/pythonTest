def solution(gawibawibo):
    answer = []
    len_g = len(gawibawibo[0])
    yh_cnt = 0
    cs_cnt = 0
    for i in range(len_g):
        yh = gawibawibo[0][i]
        cs = gawibawibo[1][i]
        print(yh, cs)
        if yh == cs :
            continue
        if (yh == 5 and cs == 0 )  or (yh == 0 and cs == 5 ) :
            if yh == 5:
                yh_cnt += 1
            elif cs == 5:
                cs_cnt += 1
        else:
            if yh  < cs :
                yh_cnt += 1
            else :
                cs_cnt += 1

    answer.append(yh_cnt)
    answer.append(cs_cnt)
    return answer

gawibawibo = [[2,0,5],[5,0,2]]
ans= solution(gawibawibo)

print('ans:', ans)