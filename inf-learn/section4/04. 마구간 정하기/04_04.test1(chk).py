
def chk_cnt(x, M, inp):
    xlst = [0] * M
    # n 값만큼 띄어서..
    print(xlst)
    cnt = 0
    xlst[cnt] = inp[cnt]

    for i in range (1, len(inp)):
        flag = False
        if (inp[i] - xlst[cnt]) < x :
            continue
        else :
            if cnt > len(inp)-1 :
                break
            else :
                cnt += 1
                print('cnt:', cnt)
                xlst[cnt] = inp[i]

    print(xlst, cnt)
    return xlst

# 프로그래머스 스타일 로 ...
def solution(N, M, inp):
    answer = 0

    # 이건 소트 하고 시작해야...
    inp.sort()
    print(inp)

    start = inp[0]
    end = inp[-1]
    print(start, end)

    cnt = 0
    top_min = 0
    #while cnt < 5:
    while start < end :
        mid = (start+end)//2
        print(mid)
        xlst = chk_cnt(mid, M, inp)
        print(min(xlst))
        if min(xlst) < 1 :  # 0 이 있다는 것은 범위가 크다는 얘기
            end = mid-1
        else:
            # 가장 가까운 두 말의 거리가 최대가 되는 그 최대 값
            # 우선 가장 거리가 가까운 값을 찾는다
            minVal = 999999
            for i in range(1, len(xlst)):
                diff = xlst[i] - xlst[i-1]
                if minVal > diff :
                    minVal = diff
            print('minVal: ' , minVal)
            if top_min < minVal:
                top_min = minVal

            # 그리고 계속 찾는다..
            start = mid +1

        cnt += 1
    print('top_min:', top_min)
    answer = top_min
    return answer

N = 5
M = 3

inp = [1, 2, 8, 4, 9]

re = solution(N, M, inp)
print('re :', re)
#=> 3
print('==============================')

N = 3
M = 2

inp = [1, 5, 9]

re = solution(N, M, inp)
print('re :', re)
#=> 8
print('==============================')

N = 64
M = 19

inp = [8,11,18,37,57,65,83,101,112,115,129,130,146,149,153,159,166,167,172,191,201,205,227,228,234,272,273,282,295,319,340,394,398,399,436,446,453,481,499,503,611,655,680,692,718,725,726,735,739,778,811,839,841,852,867,882,907,915,923,943,956,967,970,989]

re = solution(N, M, inp)
print('re :', re)
#=>
print('==============================')