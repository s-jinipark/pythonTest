def solution(X, Y):
    answer = ''
    xdic = {}
    ydic = {}
    # 셋팅
    for xx in X:
        print(xx)
        if xx in xdic :
            xdic[xx] += 1
        else :
            xdic[xx] = 1

    for yy in Y:
        if yy in ydic :
            ydic[yy] += 1
        else :
            ydic[yy] = 1

    #
    print(xdic, ydic)
    tmplist = []
    # 공통 부분 만들기
    for i in xdic :
        for j in ydic :
            if i == j :
                print(i)
                print(min(xdic[i], ydic[j]))
                tmp = min(xdic[i], ydic[j])
                for k in range(tmp):
                    tmplist.append(i)
    print(tmplist)
    if len(tmplist) == 0 :
        return "-1"
    tmplist.sort(reverse=True)
    if len(tmplist) > 1 and tmplist[0] =='0':
        return '0'
    for t in tmplist:
        answer += t
    return answer

#X = "100"
#Y = "2345"
#X = "100"
#Y = "203045"
X = "100"
Y = "123450"

re = solution(X, Y)
print(re)

'''
[기존] 시간 초과

def solution(X, Y):
    answer = ''
    연습 = []
    xlist = list(X)
    ylist = list(Y)

    for i in range(len(xlist)) :
        for j in range(len(ylist)) :
            if xlist[i] == ylist[j] :
                #print('>', ylist[j])
                #ylist.pop(j)  # 오류남
                연습.append(ylist[j])
                ylist[j] = '-1'
                break
    if len(연습) == 0 :
        return "-1"
    #print(xlist)
    연습.sort(reverse=True)
    #print(연습)
    if len(연습) > 1 and 연습[0] =='0':
        return '0'
    for t in 연습:
        answer += t
    return answer
    
'''